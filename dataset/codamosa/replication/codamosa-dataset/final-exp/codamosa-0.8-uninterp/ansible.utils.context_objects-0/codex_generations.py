

# Generated at 2022-06-13 15:59:37.060333
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class Test(object):
        pass

    assert issubclass(Test, _ABCSingleton)

# Generated at 2022-06-13 15:59:42.554863
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton
    class C(A):
        pass
    class D(B):
        pass
    assert A() == A()
    assert A() != B()
    assert C() != D()
    assert C() != B()
    assert D() != A()
    assert type(C()) == C
    assert type(D()) == D


# Generated at 2022-06-13 15:59:49.878523
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    d = {
        'foo': 'bar',
        'banana': 5,
    }

    gc1 = GlobalCLIArgs.from_options_dictionary(d)
    gc2 = GlobalCLIArgs.from_options_dictionary(d)

    assert gc1 is gc2

    assert isinstance(gc1, GlobalCLIArgs)
    assert isinstance(gc2, GlobalCLIArgs)

    assert gc1['foo'] == 'bar'
    assert gc1['banana'] == 5

# Generated at 2022-06-13 16:00:01.112097
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys

    import pytest

    from ansible.cli.arguments import options as opt

    orig_sys_argv = sys.argv

    def _factory(args):
        """
        Create a new instance of the argparse arg structure and parse the cli args into it, returning it.

        We have to do this here rather than passing in opt because opt has already been parsed at this
        point in the program.
        """
        sys.argv = args
        parser = opt(args)
        return parser.parse_args(args[1:])


# Generated at 2022-06-13 16:00:02.982286
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
        foo = 1



# Generated at 2022-06-13 16:00:07.668098
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object):
        def __init__(self, test_value):
            self.ansible_connection = test_value

    options = Options("local")
    global_cli_args = GlobalCLIArgs.from_options(options)

    assert options.ansible_connection == "local"
    assert global_cli_args.ansible_connection == "local"

# Generated at 2022-06-13 16:00:17.724054
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 1, 'bar': 'two', 'baz': {'n': 3, 'm': 'four'}, 'nested': ['one', 'two', 3, 'four', {'five': [6, 7]}]})
    assert args['foo'] == 1
    assert args['bar'] == 'two'
    assert args['baz']['n'] == 3
    assert args['baz']['m'] == 'four'
    assert args['nested'][0] == 'one'
    assert args['nested'][1] == 'two'
    assert args['nested'][2] == 3
    assert args['nested'][3] == 'four'
    assert args['nested'][4]['five'][0] == 6

# Generated at 2022-06-13 16:00:20.600251
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(_ABCSingleton):
        pass

    assert issubclass(TestClass, Singleton)

# Generated at 2022-06-13 16:00:30.107518
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils._text import to_text
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w+') as tmpfile:
        tmpfile.write("""Foo:
  bar:
  - 1
  - 2
  - 3
""")
        tmpfile.flush()
        tmpfile.seek(0)
        import yaml
        opts = yaml.load(tmpfile)
        assert isinstance(opts, dict)
        opts = CLIArgs(opts)
        assert isinstance(opts, ImmutableDict)
        assert to_text(opts) == to_text({'Foo': {'bar': [1, 2, 3]}})



# Generated at 2022-06-13 16:00:32.323473
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs({"test": "ing"}) == CLIArgs({"test": "ing"})

# Generated at 2022-06-13 16:00:38.182691
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # This imports ansible.constants, which is a Singleton, and therefore tests if our singleton is
    # one of a kind
    import ansible.constants

    # If this import doesn't result in an exception, we are good.
    import ansible.constants.__main__

# Generated at 2022-06-13 16:00:46.131713
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli = CLIArgs({
        "a": "1",
        "b": [
            "2",
            "3"
        ],
        "c": {
            "d": "4",
            "e": [
                "5",
                "6"
            ]
        }
    })

    assert isinstance(cli, Mapping)
    assert isinstance(cli, ImmutableDict)
    assert not isinstance(cli, Set)
    assert not isinstance(cli, Sequence)

    assert isinstance(cli["c"], Mapping)
    assert isinstance(cli["c"], ImmutableDict)
    assert not isinstance(cli["c"], Set)
    assert not isinstance(cli["c"], Sequence)

    assert isinstance(cli["b"], Sequence)
    assert isinstance(cli["b"], tuple)
   

# Generated at 2022-06-13 16:00:53.490957
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class DummyABCMeta(object):
        __metaclass__ = ABCMeta

        def __init__(self):
            pass

    class DummySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    class DummyABCSingleton(DummyABCMeta, DummySingleton):
        pass

    assert isinstance(DummyABCSingleton(), DummyABCSingleton)

# Generated at 2022-06-13 16:01:04.395980
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test that subclasses are allowed
    class TempCLIArgs(CLIArgs):
        pass

    options = dict(test=dict(test2="test2", test3=dict(test4="test4")))
    # Ensure that the correct type is returned from from_options
    options_cliargs = CLIArgs.from_options(options)
    options_temp_cliargs = TempCLIArgs.from_options(options)
    # Ensure that the dict is converted to the correct internal format
    assert isinstance(options_cliargs, ImmutableDict)
    assert isinstance(options_cliargs, Mapping)
    assert isinstance(options_temp_cliargs, ImmutableDict)
    assert isinstance(options_temp_cliargs, Mapping)
    # Ensure that the dict is converted to the correct internal format even on subclasses
   

# Generated at 2022-06-13 16:01:15.508375
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
    # Create the first instance
    test_class1 = TestClass()
    # assert that test_class1 was created by an instance of the Singleton metaclass
    assert(isinstance(test_class1, Singleton))
    # assert that __new__ was called on the Singleton metaclass and that it returned the test_class1 object
    assert(test_class1 is Singleton.__new__(TestClass))
    # Create the second instance
    test_class2 = TestClass()
    # assert that the first instance is the same as the second instance
    assert(test_class1 is test_class2)
    # assert that the singleton metaclass returns the same instance for all constructors
    assert(test_class1 is TestClass())

# Generated at 2022-06-13 16:01:17.377467
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.release import __version__
    mapping = {'module_path': '.', 'version': __version__}
    args = CLIArgs(mapping)
    assert args['module_path'] == mapping['module_path']



# Generated at 2022-06-13 16:01:19.038004
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():  # pragma: no cover
    class TestClass(object):
        __metaclass__ = _ABCSingleton

    assert TestClass() is TestClass()

# Generated at 2022-06-13 16:01:29.666273
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import json
    import unittest

    class TestGlobalCLIArgs(unittest.TestCase):
        def test_GlobalCLIArgs(self):
            g_args = GlobalCLIArgs({u'one': u'1', u'two': u'2', u'three': u'3'})
            self.assertEqual(json.dumps(g_args), u'{"one": "1", "two": "2", "three": "3"}')

    # Expected output:
    #
    # [root@ansible ansible]# python3 -m ansible.module_utils.common.cli_args
    # test_GlobalCLIArgs
    # .
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.000s
    #
    # OK
    unittest.main()

# Generated at 2022-06-13 16:01:38.778828
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict
    mydict = {}
    mydict["k1"] = [1, 2, 3]
    mydict["k2"] = (4, 5)
    mydict["k3"] = {6: 7, 8: 9}
    mydict["k4"] = "this is a string"
    mydict["k5"] = {0: {1: {2: 3}}}
    mydict["k6"] = (1, 2, {10: 20})
    mydict["k7"] = {10: {20: {30: 40}}}
    mydict["k8"] = "another string"
    mydict["k9"] = ["one list", ("one tuple", "one tuple")]

# Generated at 2022-06-13 16:01:40.363544
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonABC(metaclass=_ABCSingleton):
        pass
    assert SingletonABC() is SingletonABC()

# Generated at 2022-06-13 16:01:50.570964
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.data import ensure_text
    from ansible.module_utils.common.collections import CollectionModule
    from ansible.module_utils.ansible_release import __version__

    class OptionParser(object):
        def __init__(self):
            self.a = 'a'
            self.b = 'b'

    options = OptionParser()
    options.module_lang = 'en'
    options.module_default_lang = 'de'

    # Set object vars to something different than the option values.
    # If these two assignments were not there, the test might pass
    # because both object vars and option values are the same values.
    cli_args = CLIArgs.from_options(options)
    cli_args.module_lang = 'en'
    cli_args.module_default

# Generated at 2022-06-13 16:02:00.549332
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test the patching of Singleton and ABCMeta together
    """
    from ansible.module_utils.common.text.converters import (to_native, to_text)

    # pylint: disable=E0110
    class TestClass1(object):
        """Dummy class"""

        def __init__(self, val1, val2=None):
            self._val1 = to_text(val1)
            self._val2 = to_text(val2)

        def __unicode__(self):
            if self._val2 is None:
                return self._val1
            return '{0} {1}'.format(self._val1, self._val2)


# Generated at 2022-06-13 16:02:04.919954
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    from ansible.utils.loader import DataLoader
    from ansible.utils.path import ANSIBLE_LIB_ROOT

    display = Display()
    loader = DataLoader(path_list=[ANSIBLE_LIB_ROOT])

    cli_options = CLIArgs.from_options(loader.options)
    assert isinstance(cli_options, CLIArgs)


# Generated at 2022-06-13 16:02:11.640411
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    a1 = A()
    a2 = A()
    assert a1 is a2

    class B(object):
        __metaclass__ = _ABCSingleton
    b1 = B()
    b2 = B()
    assert b1 is b2
    assert b1 is not a1 and b1 is not a2 and b2 is not a1 and b2 is not a2

# Generated at 2022-06-13 16:02:19.668172
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Arrange
    testargs = {'test': 'test',
                'test_mapping': {'test_mapping_item1': [1, 2, 3],
                                 'test_mapping_item2': {'test_mapping_item2_level2': True}},
                'test_list': [1, 2, 3],
                'test_set': set([4, 5, 6]),
                'test_tuple': (7, 8, 9),
                }
    # Act
    obj = CLIArgs(testargs)
    # Assert
    assert obj == testargs
    assert id(obj) != id(testargs)
    assert isinstance(obj['test_mapping'], ImmutableDict)
    assert id(obj['test_mapping']) != id(testargs['test_mapping'])

# Generated at 2022-06-13 16:02:22.128719
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    test1 = Test()
    test2 = Test()
    assert test1 is test2

# Generated at 2022-06-13 16:02:28.264565
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:33.331617
# Unit test for constructor of class CLIArgs
def test_CLIArgs():  # pragma: no cover
    args = CLIArgs({'a': 'alpha', 'b': {'bravo': {'charlie' : 'delta'}}})

    assert isinstance(args, ImmutableDict)
    assert isinstance(args['b'], ImmutableDict)
    assert isinstance(args['b']['bravo'], frozenset)
    assert isinstance(args['b']['bravo'].pop(), text_type)

    # Make sure these are immutable.
    try:
        args['c'] = 'charlie'
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        args['b']['bravo'].pop()
    except Exception as e:
        assert isinstance(e, AttributeError)


# Unit

# Generated at 2022-06-13 16:02:43.852139
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import argparse
    from ansible.errors import AnsibleError

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    parser.add_argument('--bar', action='store_true')
    parser.add_argument('--baz', action='append')
    parser.add_argument('--qux', action='append')

    sys.argv.append('--foo')
    sys.argv.append('bar')
    sys.argv.append('--bar')
    sys.argv.append('--baz')
    sys.argv.append('1')
    sys.argv.append('--baz')
    sys.argv.append('2')
    sys.argv.append('--qux')
    sys.argv.append('quux')


# Generated at 2022-06-13 16:02:49.441312
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    input_args = {
        'input_str': 'str',
        'input_int': 1,
    }
    input_args['input_dict'] = input_args
    args = CLIArgs(input_args)
    assert isinstance(args['input_str'], text_type)
    assert isinstance(args['input_int'], int)
    assert not isinstance(args['input_int'], text_type)
    assert isinstance(args['input_dict'], ImmutableDict)
    assert not isinstance(args['input_dict'], ImmutableDict)

# Generated at 2022-06-13 16:02:55.165845
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {'foo': 'bar'}
    ga = GlobalCLIArgs.from_options(args)
    assert isinstance(ga, CLIArgs)
    assert isinstance(ga, GlobalCLIArgs)
    assert ga['foo'] == 'bar'



# Generated at 2022-06-13 16:02:58.459040
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    b = Singleton()
    c = Singleton()
    assert b is c

    d = _ABCSingleton()
    e = _ABCSingleton()
    assert d is e


# Generated at 2022-06-13 16:03:04.354928
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test presence of the Singleton class in _ABCSingleton.

    If _ABCSingleton does not work, this will fail because it will try to create two instances
    of the same class.
    """
    class Test(object):
        __metaclass__ = _ABCSingleton

    class TestTwo(object):
        __metaclass__ = _ABCSingleton

    test = Test()
    testtwo = TestTwo()
    assert test == testtwo

# Generated at 2022-06-13 16:03:07.096687
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest

    global_cli_args = GlobalCLIArgs({'foo': 'bar'})
    with pytest.raises(TypeError):
        global_cli_args['foo'] = 'baz'

# Generated at 2022-06-13 16:03:08.677229
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({'foo': 'bar'})

# Generated at 2022-06-13 16:03:13.017706
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestAbstractClass(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass
    class TestClass(TestAbstractClass):
        def __init__(self):
            pass
    # test that the constructor does not prevent the subclasses from being instantiated
    _ = TestClass()

# Generated at 2022-06-13 16:03:16.089401
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(*_ABCSingleton.__bases__):
        def __init__(self, test):
            self.test = test

    assert Foo('test').test == 'test'

# Generated at 2022-06-13 16:03:20.987323
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    class CLIOptions(collections.namedtuple('CLIOptions', ('foo', 'bar'))):
        pass

    options = CLIOptions(foo='foo', bar=['bar', 'bar', 'bar'])
    cli_args = CLIArgs.from_options(options)
    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args['foo'], text_type)
    assert isinstance(cli_args['bar'], tuple)

# Generated at 2022-06-13 16:03:28.854766
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.module_utils.common.collections import GlobalCLIArgs
    dict1 = {'a': 'A', 'b': ['B0', 'B1', 'B2']}
    dict2 = {'b': ['B0', 'B1', 'B2'], 'a': 'A'}
    dict3 = {'b': ['B1', 'B0', 'B2'], 'a': 'A'}
    dict4 = {'b': ['B1', 'B2', 'B0'], 'c': dict(d='D', e=['E0', 'E1', 'E2'])}
    dict5 = {'b': [('B0', 'B3'), ('B1', 'B4'), ('B2', 'B5')], 'a': 'A'}


# Generated at 2022-06-13 16:03:35.611303
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    foo = {'keys': ['one', 'two', 'three'], 'values': [1, 2, 3]}
    bar = {'keys': ['four', 'five'], 'values': [4, 5], 'dict': foo}
    test = {'foo': foo, 'bar': bar}
    cliargs = CLIArgs(test)
    assert cliargs.foo.values[1] == 2

# Generated at 2022-06-13 16:03:41.438868
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        GlobalCLIArgs({'a': 'a'})
    except TypeError:
        pass

# Generated at 2022-06-13 16:03:47.427816
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            self.value = True

    # Only one instance can be created of the above class and value will remain True
    instance1 = Foo()
    instance1.value = False
    instance2 = Foo()
    assert instance2.value == instance1.value

# vim: set expandtab shiftwidth=4 tabstop=4 smartindent autoindent:

# Generated at 2022-06-13 16:03:49.732059
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class C(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(C, Singleton)
    assert issubclass(C, ABCMeta)

# Generated at 2022-06-13 16:03:52.743494
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass

    a1 = Test()
    a2 = Test()

    assert a1 is a2

# Generated at 2022-06-13 16:04:01.383544
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test the constructor of class CLIArgs to ensure the cli arguments are immutable
    """
    from ansible.utils.context_objects import CLIArgs
    from ansible.module_utils.common.collections import ImmutableDict
    cli_args = CLIArgs({
        'connection': 'smart',
        'host_key_checking': True,
        'verbosity': 1,
        'check': True,
        'roles_path': [],
        'force_handlers': False
    })
    assert isinstance(cli_args, ImmutableDict)

# Generated at 2022-06-13 16:04:10.428243
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class Options(object):
        def __init__(self):
            self.listtags = False
            self.listtasks = False
            self.listhosts = False
            self.syntax = False
            self.connection = ''
            self.module_path = ''
            self.forks = 10
            self.private_key_file = ''
            self.ssh_common_args = ''
            self.ssh_extra_args = ''
            self.sftp_extra_args = ''
            self.scp_extra_args = ''
            self.become = True
            self.become_method = 'sudo'
            self.become_user = 'root'
            self.become_ask_pass = False
            self.verbosity = 1
            self.check = False
            self.check_mode = ''

# Generated at 2022-06-13 16:04:16.142830
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # This class is a Singleton so this should always be the same object
    assert GlobalCLIArgs() is GlobalCLIArgs()
    # This class is also an ImmutableDict so this should always raise AttributeError
    try:
        GlobalCLIArgs().foo = 32
    except AttributeError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-13 16:04:19.795871
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class DoubleMeta(Singleton, ABCMeta):
        """
        WARNING: Intentional bad code for unit test
        This class has two metaclasses mixed, and it should fail to create class
        """
        pass

    try:
        class BadSingleton(object, metaclass=DoubleMeta):
            pass
        if True:
            assert False, "Test _ABCSingleton failed. Class DoubleMeta should not create class"
    except TypeError:
        pass

    return True


# Generated at 2022-06-13 16:04:30.579554
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.collections import MutableSequence
    from ansible.module_utils.common.collections import MutableSet

    # Create the arguments that would be parsed by optparse
    options = type('Values', (), {'debug': False, 'foo': 'bar'})

    # Create a GlobalCLIArgs instance
    args = GlobalCLIArgs.from_options(options)

    # Make sure we can get the arguments as long as they were returned toplevel
    assert args.get('debug') is False
    assert args.get('foo') == 'bar'

    # We should not be able to set anything in the GlobalCLIArgs
    assert not hasattr(args, '__setitem__')
    assert not hasattr

# Generated at 2022-06-13 16:04:38.782472
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.runner.connection_plugins.network_cli import \
        Connection as network_cli
    from ansible.cli.argparser import CLIArgParser
    # initializing class CLIArgParser
    cli_arg_parser = CLIArgParser()
    # getting arguments using parse_cli_args function in class CLIArgParser
    parsed_cli_args = cli_arg_parser.parse_cli_args()

    # Checking if class CLIArgs accepts a text argument as first argument
    assert CLIArgs("sample").keys()

    # Creating a mapping with keys as module_name and connection as values of keys
    mapping = {"module_name": network_cli.__name__,
               "connection": network_cli}
    # initializing class CLIArgs with mapping as argument
    cli_args = CLIArgs(mapping)

    # Checking if class CLIArgs

# Generated at 2022-06-13 16:04:49.958243
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonTest(object, metaclass=_ABCSingleton):
        pass

    test = ABCSingletonTest()
    assert isinstance(test, ABCSingletonTest)

# Generated at 2022-06-13 16:04:51.881912
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyClass(object):
        __metaclass__ = _ABCSingleton
    assert MyClass() is MyClass()

# Generated at 2022-06-13 16:05:00.261681
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:05:03.403654
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(metaclass=_ABCSingleton):
        pass

    assert A is B


# Generated at 2022-06-13 16:05:13.624235
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # pylint: disable=protected-access
    args = CLIArgs._make_immutable({'one': 1})
    assert isinstance(args, CLIArgs)
    assert isinstance(args, ImmutableDict)
    assert args.one == 1
    assert not hasattr(args, 'two')

    # Test that our immutable wrapper converts the object to be immutable
    assert isinstance(args, Mapping)
    test_list_default = ['one', 'two', 'three']
    test_list = ['one', 'two', 'three']
    test_tuple = ('one', 'two', 'three')
    test_dict_default = {'one': 1, 'two': 2, 'three': 3}
    test_dict = {'one': 1, 'two': 2, 'three': 3}

# Generated at 2022-06-13 16:05:18.463569
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {}
    args['a'] = 'b'
    args['c'] = 'd'

    args_obj = CLIArgs(args)
    assert args_obj['a'] == 'b'
    assert args_obj['c'] == 'd'

    args['c'] = 'e'
    assert args_obj['c'] == 'd'

# Generated at 2022-06-13 16:05:22.248112
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    expected_value = "-vvvv"
    args = CLIArgs.from_options(object(ANSIBLE_DEBUG=expected_value))
    assert args['ANSIBLE_DEBUG'] == expected_value, "Value not stored"


# Generated at 2022-06-13 16:05:25.933799
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    import unittest

    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    with unittest.TestCase() as test_case:
        test_case.assertIsInstance(A(), A)
        test_case.assertIsInstance(B(), A)
        test_case.assertIsInstance(A(), Singleton)
        test_case.assertEqual(id(A()), id(B()))


# Generated at 2022-06-13 16:05:28.754701
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class B(object):
        pass

    class A(_ABCSingleton):
        _instances = {}

    A()
    B()
    B()

# Generated at 2022-06-13 16:05:32.043870
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'a': [1, 2, 3]})
    assert args['a'][2] == 3
    args['a'][2] = 4
    assert args['a'][2] == 3

# Generated at 2022-06-13 16:05:58.395000
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.parsing import vault
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude

    # Instantiate an immutable dictionary
    immutable_dict_instance = ImmutableDict(var='var')
    # Instantiate a GlobalCLIArgs object

# Generated at 2022-06-13 16:06:04.646113
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test1(object):
        __metaclass__ = _ABCSingleton

    class Test2(object):
        __metaclass__ = _ABCSingleton

    def func():
        pass

    # Test that classes with the same name inherit the singleton
    assert Test1.__name__ == Test2.__name__
    assert Test1() is Test2()
    assert Test1() is not Test2

    # Test that classes with different names have different objects
    assert Test1.__name__ != func.__name__
    assert Test1() is not func

# Generated at 2022-06-13 16:06:10.241954
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    class C(object):
        __metaclass__ = _ABCSingleton

    assert A is B
    assert A is not C
    assert issubclass(B, A)
    assert issubclass(C, A)

# Generated at 2022-06-13 16:06:13.034645
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass
    assert Foo() is Foo()

    class Bar(Foo):
        pass
    assert Foo() is not Bar()

# Generated at 2022-06-13 16:06:16.072340
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'debug': True, 'check': False}
    cli_args = CLIArgs(args)
    assert cli_args['debug'] == True
    assert cli_args['check'] == False


# Generated at 2022-06-13 16:06:26.504282
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys

    from ansible.module_utils.six import PY3

    opt = GlobalCLIArgs.from_options(None)
    assert opt is GlobalCLIArgs()
    assert isinstance(opt, CLIArgs)

    # Check for top-level and first level keys
    assert 'ansible_version' in opt
    assert isinstance(opt['ansible_version'], (text_type, binary_type))
    assert 'command_line' in opt
    assert isinstance(opt['command_line'], list)
    assert 'python_version' in opt
    assert isinstance(opt['python_version'], int)

    # check that the version is in the format:  (#, #, #)
    assert len(opt['ansible_version'].split('.')) == 3

    # Check for top-

# Generated at 2022-06-13 16:06:36.895063
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    c = CLIArgs({u"a": {u"b": u"1", u"d": u"3"}, u"e": u"5"})
    assert isinstance(c, ImmutableDict)
    assert isinstance(c, Mapping)
    assert not isinstance(c, GlobalCLIArgs)
    assert isinstance(c, CLIArgs)
    assert c == {u"a": {u"b": u"1", u"d": u"3"}, u"e": u"5"}
    assert isinstance(c[u"a"], ImmutableDict)
    assert isinstance(c[u"a"], Mapping)
    assert not isinstance(c[u"a"], GlobalCLIArgs)
    assert isinstance(c[u"a"], CLIArgs)

# Generated at 2022-06-13 16:06:39.689526
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'
    assert args.get('foo') == 'bar'

# Generated at 2022-06-13 16:06:41.579054
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    result = GlobalCLIArgs({'verbosity': 5})
    expected = CLIArgs({'verbosity': 5})
    assert result == expected

# Generated at 2022-06-13 16:06:53.699149
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import ansible.cli.playbook
    import ansible.cli.adhoc

    test_input = dict(
        test_input=dict(
            test_input_1=dict(test_input_2=dict(test_input_3=dict())),
            test_input_4=set([]),
            test_input_5=tuple(["foo", "bar"]),
        ),
        test_input_6=list(["baz", "baj"]),
    )
    args = CLIArgs(test_input)

    assert args.test_input_6 == list(["baz", "baj"])
    assert args.test_input.test_input_1.test_input_2.test_input_3 == dict()
    assert args.test_input.test_input_4 == set()

# Generated at 2022-06-13 16:07:36.123930
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:07:40.497523
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Simple example class TestCLIArgs is subclass of CLIArgs 
    class TestCLIArgs(CLIArgs):
        pass
    # Dict Data
    data = {"name": "ansible", "age": 18}
    # TestCLIArgs instance
    test_cli_args = TestCLIArgs(data)
    # Assert the data and test_cli_args is equal
    assert data == test_cli_args


# Generated at 2022-06-13 16:07:46.190112
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    dummy_cli_args = CLIArgs({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(dummy_cli_args, ImmutableDict)
    assert len(dummy_cli_args) == 2
    assert dummy_cli_args == {'key1': 'value1', 'key2': 'value2'}
    assert dummy_cli_args == ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert dummy_cli_args is not CLIArgs({'key1': 'value1', 'key2': 'value2'})
    assert dummy_cli_args is not ImmutableDict({'key1': 'value1', 'key2': 'value2'})

# Generated at 2022-06-13 16:07:53.583638
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys

    out = []
    class Stream(object):
        def __init__(self, name, out=[]):
            self.name = name
            self.out = out

        def write(self, data):
            self.out.append(data)

    real_stdout = sys.stdout
    sys.stdout = Stream('stream', out=out)
    args = CLIArgs({'verbosity': 1})
    print()
    sys.stdout = real_stdout
    assert args.verbosity == 1, 'Argument not set correctly'

# Generated at 2022-06-13 16:07:55.865582
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton


# Generated at 2022-06-13 16:07:59.950437
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    class Bar(Foo):
        pass

    assert issubclass(Bar, ABCMeta)
    assert issubclass(Bar, Singleton)

# Generated at 2022-06-13 16:08:00.801636
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    pass

# Generated at 2022-06-13 16:08:09.830466
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from ansible.module_utils.common.tests.unit.compat.mock import MagicMock
    class A(metaclass=_ABCSingleton):
        pass
    a = A()
    assert id(a) == id(A())
    assert a.__class__ is A
    class B(A):
        pass
    assert id(b) == id(B())
    assert b.__class__ is B
    class C(B):
        pass
    assert id(c) == id(C())
    assert c.__class__ is C
    class D(A):
        pass
    assert id(d) == id(D())
    assert d.__class__ is D
    assert id(a) == id(D())
    assert not isinstance(D(), A)
    class E(D):
        pass


# Generated at 2022-06-13 16:08:12.125432
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(object):
        pass

    TestSingleton()

    class TestSingleton(object, metaclass=_ABCSingleton):
        pass

    TestSingleton()

# Generated at 2022-06-13 16:08:22.218702
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test CLIArgs class convert dict to ImmutableDict
    cli_args = CLIArgs({'a': {'b': {'c': 'd'}}})
    assert type(cli_args) == ImmutableDict
    assert type(cli_args['a']) == ImmutableDict
    assert type(cli_args['a']['b']) == ImmutableDict
    assert type(cli_args['a']['b']['c']) == text_type
    assert cli_args['a']['b']['c'] == 'd'
    cli_args = CLIArgs({'a': {'b': ['c']}})
    assert type(cli_args) == ImmutableDict
    assert type(cli_args['a']) == ImmutableDict

# Generated at 2022-06-13 16:09:31.378876
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Constructor of class CLIArgs

    This is used to validate that this class is able to be instantiated
    with a given input, and that it fails as expected when given the
    wrong input.
    """

    mapping = {"foo": "bar"}
    instance = CLIArgs(mapping)
    assert isinstance(instance, ImmutableDict)