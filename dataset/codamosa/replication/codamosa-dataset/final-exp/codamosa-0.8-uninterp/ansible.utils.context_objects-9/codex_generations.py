

# Generated at 2022-06-13 15:59:35.395550
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.config.manager
    from ansible.module_utils.common.collections import ImmutableDict

    cfg = ansible.config.manager.ConfigManager(None)._options
    gca = GlobalCLIArgs.from_options(cfg)
    assert isinstance(gca, ImmutableDict)

# Generated at 2022-06-13 15:59:43.683262
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    This unit test is a smoke test, to make sure that we have the new metaclass defined correctly
    so we don't accidentally add a metaclass that breaks the functionality.

    Without this test, it is very easy to accidentally add something like the following to the
    _ABCSingleton class:

        class __metaclass__(type):
            pass

    This is incorrect because it causes an infinite loop at runtime, where meta objects are
    created from this class, which then evokes the __metaclass__ of this class, which then creates
    another meta object, and so on.

    The goal of this unit test is to make sure that we create a class that is a Singleton and is
    an ABC, and is an instance of the Singleton class.  If we create the above infinite loop by
    mistake, this test will catch it.
    """

# Generated at 2022-06-13 15:59:53.702129
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    old_type = GlobalCLIArgs
    GlobalCLIArgs = _ABCSingleton('GlobalCLIArgs', (object,), {})

# Generated at 2022-06-13 16:00:02.754219
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import types

    def _test_sys_modules(name, value):
        if hasattr(types, 'ModuleType'):
            assert isinstance(value, types.ModuleType), "%s is not a module" % name
        else:
            assert isinstance(value, types.ModuleType), "%s is not a module" % name

    arg = GlobalCLIArgs({'foo': 'bar'})
    assert arg == {'foo': 'bar'}, "GlobalCLIArgs does not store an ImmutableDict"

    if sys.version_info < (3,):
        builtins_name = '__builtin__'
    else:
        builtins_name = 'builtins'

    _test_sys_modules(builtins_name, sys.modules[builtins_name])

# Generated at 2022-06-13 16:00:05.345774
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton

    t1 = TestClass()
    t2 = TestClass()
    assert t1 is t2

# Generated at 2022-06-13 16:00:14.509394
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--test1')
    parser.add_option('--test2')
    (options, args) = parser.parse_args(['--test1', '3'])
    args = GlobalCLIArgs.from_options(options)
    assert args['test1'] == '3'
    # Test that you can't change the immutable object
    try:
        args.pop('test1')
    except AttributeError:
        # Expected
        pass
    else:
        assert False, 'Changing immutable CLIArgs unexpectedly succeeded'
    # Test that GlobalCLIArgs is a singleton
    args_2 = GlobalCLIArgs.from_options(options)
    assert id(args) == id(args_2)

# Generated at 2022-06-13 16:00:19.089336
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    test_dict = {'foo': 'bar', 'fiz': ['baz', 'bip'], 'bop': ImmutableDict({'qux': 'quux'})}
    global_args = GlobalCLIArgs(test_dict)
    assert isinstance(global_args, GlobalCLIArgs)
    assert global_args == ImmutableDict(test_dict)


# Generated at 2022-06-13 16:00:29.906499
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest

    class TestClass:
        def __init__(self, a):
            self.a = a

    options = TestClass(a={"abc": 10})
    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args.a['abc'] == 10

    options = TestClass(a=["abc", 10])
    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args.a[1] == 10

    options = TestClass(a={'key1': {}})
    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args.a['key1'] == {}

    # Test set as an argument
    options = TestClass(a={"abc": {1, 2, 3}})
   

# Generated at 2022-06-13 16:00:41.010806
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        def __init__(self):
            self.foo = 'foo'
            self.bar = [1, 2, 3]
            self.baz = {'hello': 'world'}
    options = Options()
    a = CLIArgs.from_options(options)
    assert isinstance(a, ImmutableDict)
    assert a['foo'] == 'foo'
    assert a['bar'] == (1, 2, 3)
    assert a['baz'] == ImmutableDict({'hello': 'world'})
    options.foo = 'bar'
    options.bar = ['hello']
    options.baz = {'world': 'hello'}
    assert a['foo'] == 'foo'
    assert a['bar'] == (1, 2, 3)

# Generated at 2022-06-13 16:00:45.101141
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Set up test
    test_args = {"foo": {"bar": ["abc", 123], "baz": {"1": "xxx", "2": "yyy"}}}
    # Run test
    test_cli_args = CLIArgs(test_args)
    # Check results
    assert isinstance(test_cli_args, ImmutableDict)
    assert isinstance(test_cli_args['foo'], ImmutableDict)
    assert isinstance(test_cli_args['foo']['bar'], tuple)
    assert isinstance(test_cli_args['foo']['baz'], ImmutableDict)


# Generated at 2022-06-13 16:00:50.248528
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(A, _ABCSingleton)

# Generated at 2022-06-13 16:01:01.778540
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest
    from collections import Mapping, Sequence
    from ansible.module_utils.common.collections import ImmutableDict

    # We want our objects back to be hashable and immutable
    class MyImmutableDict(ImmutableDict):
        pass

    class MyMapping(Mapping):
        def __init__(self, data):
            self._data = data

        def __len__(self):
            return len(self._data)

        def __iter__(self):
            return iter(self._data)

        def __getitem__(self, key):
            return self._data[key]

    class MySequence(Sequence):
        def __init__(self, data):
            self._data = data

        def __len__(self):
            return len(self._data)


# Generated at 2022-06-13 16:01:02.538880
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({})
    GlobalCLIArgs.from_options(None)

# Generated at 2022-06-13 16:01:09.152304
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.constants
    import ansible.module_utils.common.arguments

    options = ansible.module_utils.common.arguments.AnsibleCoreCLIArgs()
    options.module_path = 'test/module_path'

    options.python_interpreter_selection = '1'
    ansible.constants.DEFAULT_PYTHON_INTERPRETER = options.python_interpreter_selection
    global_cli_args = GlobalCLIArgs.from_options(options)

    # Boolean constants can be used
    assert global_cli_args['private_data_dir']

    # Set immutable options can not be modified
    with pytest.raises(TypeError):
        global_cli_args['private_data_dir'] = 'test/private_data_dir'

    # Sequences of constants

# Generated at 2022-06-13 16:01:17.889490
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse

    parser = argparse.ArgumentParser(description="test parsing args for testing")

    parser.add_argument("--name", default="default_value")
    parser.add_argument("--max-children", default=100, type=int)

    try:
        parsed_args = parser.parse_args()
    except SystemExit:
        from ansible.utils.display import Display
        display = Display()
        display.display("Cannot parse arguments for test.  Skipping test.")
        return

    args = GlobalCLIArgs.from_options(parsed_args)
    assert isinstance(args, GlobalCLIArgs)
    assert args["name"] == "default_value"
    assert args["max_children"] == 100


# Generated at 2022-06-13 16:01:28.413482
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    
    import collections
    import ansible.module_utils.common.collections 

    # Create the CLIArgs object
    options = collections.namedtuple(
        'options', 
        'foo,bar,baz,abc,xyz'
    ) 
    options.foo=True
    options.bar='bar'
    options.baz=1
    options.abc=[1, 'foo']
    options.xyz={'k1' : 1, 'k2' : 'foo'} 
    cli_args = CLIArgs.from_options(options)

    # Create a second CLIArgs instance
    cli_args_2 = CLIArgs(cli_args)

    # Test if items from options are set
    assert(isinstance(cli_args, ImmutableDict))

# Generated at 2022-06-13 16:01:35.702856
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Make sure that class _ABCSingleton works as it should"""
    class TestClass(object):
        pass

    class TestClass1(TestClass):
        pass

    class TestClass2(TestClass):
        pass

    class TestClass3(TestClass):
        pass

    class TestClass4(TestClass):
        pass

    class TestClass5(TestClass):
        pass

    assert issubclass(TestClass1, TestClass)
    assert issubclass(TestClass2, TestClass)
    assert issubclass(TestClass3, TestClass)
    assert issubclass(TestClass4, TestClass)
    assert issubclass(TestClass5, TestClass)

    assert isinstance(TestClass1(), TestClass)
    assert isinstance(TestClass2(), TestClass)

# Generated at 2022-06-13 16:01:39.382034
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        def __str__(self):
            return 'Test'

    assert Test() is Test()

# Generated at 2022-06-13 16:01:41.410081
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class foo(_ABCSingleton):
        pass

    class bar(_ABCSingleton):
        pass

    assert foo is foo()
    assert bar is bar()

# Generated at 2022-06-13 16:01:45.365028
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        pass
    class C(object):
        __metaclass__ = _ABCSingleton
    A()
    B()
    C()
    B()
    C()

# Generated at 2022-06-13 16:01:54.914299
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        'abc': text_type('foo'),
        'def': text_type('bar'),
        'ghi': ['foo', 'bar'],
        'jkl': ['foo', ['bar', 'baz'], 'qux'],
    }
    cli_args = CLIArgs(mapping)
    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args, Mapping)

    for key, value in mapping.items():
        assert cli_args[key] == value

# Generated at 2022-06-13 16:02:00.476795
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Opt(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    opt = Opt(
        password=dict(
            required=False,
            no_log=True
        ),
        identifiers=dict(
            required=False,
            type="list"
        )
    )
    GlobalCLIArgs.from_options(opt)

# Generated at 2022-06-13 16:02:03.206980
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    _dict = {
        'a': '1'
    }
    _immutable = ImmutableDict(_dict)
    _CLIArgs = CLIArgs(_immutable)
    assert isinstance(_CLIArgs, CLIArgs)

# Generated at 2022-06-13 16:02:03.888793
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({'a': 1})

# Generated at 2022-06-13 16:02:06.958157
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        _value = 5

        def __init__(self, value):
            self._value = value

        def __repr__(self):
            return u'<A: value=%s>' % self._value

    a1 = A(1)
    a2 = A(2)
    assert a1 == a2
    assert repr(a1) == repr(a2) == u'<A: value=2>'

# Generated at 2022-06-13 16:02:13.805824
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    print('test_GlobalCLIArgs:'.ljust(80, '-'), end='')
    a = GlobalCLIArgs({'test': {'test': 'test'}})
    assert isinstance(a, ImmutableDict)
    b = GlobalCLIArgs({'test': {'test': 'test'}})
    assert id(a) == id(b)
    try:
        a['new'] = 1
    except TypeError:
        print(' passed')
        pass
    else:
        print(' failed')
        assert False

test_GlobalCLIArgs()

# Generated at 2022-06-13 16:02:25.074179
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Return a list of error messages.

    :returns: List of error messages.
    :rtype: list[str]
    """
    errors = []

    class TestOptions(object):
        def __init__(self):
            self.foo = None
            self.bar = 1
            self.baz = {'a': 'b'}
            self.qux = ['c', 'd']

    # Create a dictionary and set of command line args.
    args_dict = vars(TestOptions())

    # Check that a valid input is returned as-is.
    cli_args = CLIArgs(args_dict)
    if not isinstance(cli_args, ImmutableDict):
        errors.append('CLIArgs(<dict>) did not return an ImmutableDict')


# Generated at 2022-06-13 16:02:27.105811
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """Create a GlobalCliArgs object and ensure the reference is the same"""
    c = CLIArgs.from_options(CLIArgs({}))
    assert id(c) == id(GlobalCLIArgs)

# Generated at 2022-06-13 16:02:29.436523
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """ Tests constructor of class GlobalCLIArgs

    :return: Nothing
    """
    got_exception = False

    try:
        GlobalCLIArgs()
    except TypeError:
        got_exception = True

    assert got_exception

# Generated at 2022-06-13 16:02:35.619498
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    import types

    class MyABCMeta(object):
        __metaclass__ = _ABCSingleton
        pass

    x = MyABCMeta()
    y = MyABCMeta()
    assert x is y
    assert isinstance(x, MyABCMeta)
    assert isinstance(x, types.TypeType)
    assert issubclass(MyABCMeta, MyABCMeta)

# Generated at 2022-06-13 16:02:40.711175
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs.from_options(GlobalCLIArgs.from_options(None))

# Generated at 2022-06-13 16:02:49.022205
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from collections import OrderedDict
    import pytest

    dict1 = OrderedDict()
    dict1['type'] = 'user'
    dict1['user'] = 'ansible'

    dict2 = OrderedDict()
    dict2['level'] = 'error'
    dict2['stdout'] = 1

    dict3 = OrderedDict()
    dict3['src'] = '/etc/hosts'
    dict3['dest'] = '/tmp/hosts'

    args = GlobalCLIArgs(vars(dict1))
    with pytest.raises(TypeError):
        args['type'] = 'admin'

    with pytest.raises(TypeError):
        args.update(dict2)

    with pytest.raises(TypeError):
        args.update(dict3)

# Generated at 2022-06-13 16:02:57.702993
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    from ansible.errors import AnsibleError
    from ansible.utils.color import colorize, stringc
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.handler import Handler

# Generated at 2022-06-13 16:03:03.251301
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonABC(object):
        __metaclass__ = _ABCSingleton

    class SingletonABCDerived(SingletonABC):
        pass

    assert isinstance(SingletonABC(), SingletonABC)
    assert isinstance(SingletonABCDerived(), SingletonABCDerived)
    assert not isinstance(SingletonABCDerived(), SingletonABC)
    assert isinstance(SingletonABC().__class__, SingletonABCMeta)

# Generated at 2022-06-13 16:03:06.205692
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    # Two references to the same object
    a = A()
    b = A()
    assert a is b

# Generated at 2022-06-13 16:03:11.674996
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {
        "debug": True,
        "verbosity": 0,
        "version": False,
        "help": False,
        "not_a_real_option": False,
    }

    args = CLIArgs(mapping)
    for key, value in mapping.items():
        assert args[key] == value



# Generated at 2022-06-13 16:03:12.552174
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs(vars())


# Generated at 2022-06-13 16:03:16.612176
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options = CLIArgs({'foo': 'bar'})
    assert options == {'foo': 'bar'}
    with pytest.raises(TypeError):
        options['foo'] = 'baz'
    assert options == {'foo': 'bar'}

# Generated at 2022-06-13 16:03:26.332416
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class TempClass(object):
        pass

    options = TempClass()
    options.foo = 'asdf'
    options.bar = 'hjkl'
    options.baz = TempClass()
    options.baz.a = [1, 2, 3]
    options.baz.b = {'a': [4, 5, 6], 'b': ['four', 'five', 'six']}
    options.baz.c = {'a': [7, 8], 'b': ['seven', 'eight']}

    args = GlobalCLIArgs.from_options(options)

    assert args.foo == 'asdf'
    assert args.bar == 'hjkl'
    assert args.baz.a == (1, 2, 3)

# Generated at 2022-06-13 16:03:38.063034
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    argv = ['first', 'argv', 'element', '--option', 'value',
            '--spaces', 'in value', '--comma,separated,args', '--empty',
            '--bool_true', '--bool_false', '--bool_auto']
    from ansible.cli.arguments import Options
    options = Options(args=argv)
    parser = options.parser

    # This test is effectively calling this function too
    GlobalCLIArgs.from_options(options)

    # Add a non-options argument to the parser.  This lets us test that
    # the parser doesn't slurp up non-options args.
    parser.add_argument('non_options')
    non_options = getattr(options.args, 'non_options')

# Generated at 2022-06-13 16:03:53.195258
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:04:04.854160
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Structure(object):
        pass
    mapping = {
        'key1': 'string',
        'key2': ['string1', 'string2'],
        'key3': {'subkey': 'subvalue'},
        'key4': 2,
    }
    mapping2 = {
        'key5': Structure(),
        'key6': 4,
    }
    toplevel = {
        'key1': 'string',
        'key2': ('string1', 'string2'),
        'key3': ImmutableDict({'subkey': 'subvalue'}),
        'key4': 2,
        'key5': Structure(),
        'key6': 4,
    }
    args = CLIArgs(mapping)
    for key, value in mapping.items():
        assert args[key] == tople

# Generated at 2022-06-13 16:04:12.445061
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 3
    loader = DataLoader()

    class Options:
        tags = ['all']
        skip_tags = []
        run_hosts = ''
        step = None
        start_at = None
        inventory = None
        subset = None
        extra_vars = {'var_to_test': 'value'}
        private_key_file = '~/.ssh/id_rsa'
        ask_pass = False
        ask_sudo_pass = False
        ask_su_pass = False
        ask_vault_pass = False
        vault_password_file = None
        new_vault

# Generated at 2022-06-13 16:04:23.964364
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    import argparse
    class TestCase(unittest.TestCase):
        def test_constructor(self):
            # Arrange
            parser = argparse.ArgumentParser()
            parser.add_argument('--flag', default=False, type=bool)
            parser.add_argument('--int', default=0, type=int)
            parser.add_argument('--str', default='', type=str)
            options = parser.parse_args(['--str', 'hello'])

            # Act
            args = CLIArgs(vars(options))
            global_args = GlobalCLIArgs.from_options(options)

            # Assert
            self.assertEqual(args['flag'], False)
            self.assertEqual(args['int'], 0)

# Generated at 2022-06-13 16:04:35.265824
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class myABCSingleton(Singleton, ABCMeta):
        """
        Combine ABCMeta based classes with Singleton based classes

        Combine Singleton and ABCMeta so we have a metaclass that unambiguously knows which can
        override the other.  Useful for making new types of containers which are also Singletons.
        """
        pass

    class mySingleton(object):
        __metaclass__ = myABCSingleton
        pass

    class mySubSingleton(mySingleton):
        pass

    assert issubclass(mySingleton, object)
    assert issubclass(myABCSingleton, Singleton)
    assert issubclass(myABCSingleton, ABCMeta)
    assert issubclass(mySubSingleton, object)
    assert issubclass(mySubSingleton, mySingleton)



# Generated at 2022-06-13 16:04:40.571973
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = {'test': {'test1': {'value1': 'abc', 'value2': '123'}, 'test2': 'def'}}
    cli_args = CLIArgs(data)
    assert cli_args['test']['test1']['value1'] == 'abc'
    assert cli_args['test']['test1']['value2'] == '123'
    assert cli_args['test']['test2'] == 'def'

# Generated at 2022-06-13 16:04:46.693792
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(metaclass=_ABCSingleton):
        def __init__(self):
            self.a = 1
            self.b = 2

    assert TestClass().a == 1 and TestClass().b == 2, "Instance of TestClass returned value not expected"
    assert TestClass.__singleton_instance__ is not None, "__singleton_instance__ should not be None"

    class TestClass(metaclass=_ABCSingleton):
        def __init__(self):
            self.a = 3
            self.b = 4

    assert TestClass().a == 3 and TestClass().b == 4, "Instance of TestClass returned value not expected"
    assert TestClass.__singleton_instance__ is not None, "__singleton_instance__ should not be None"


# Generated at 2022-06-13 16:04:50.584319
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    t_dict = dict(a=1, b=dict(c="C", d=3), e=["e1", "e2", "e3"])
    GlobalCLIArgs.from_options(t_dict)

# Generated at 2022-06-13 16:04:53.143483
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class foo(object):
        __metaclass__ = _ABCSingleton
    f1 = foo()
    f2 = foo()
    assert f1 is f2

# Generated at 2022-06-13 16:05:04.684414
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test the case where we pass in a dict
    args = CLIArgs({'a': 1,
                    'b': [1,2,3],
                    'c': {'a': 1,
                          'b': [1,2,3],
                          'c': 'd'}})
    # test that the input dictionary is immutable
    try:
        args['a'] = 2
    except TypeError:
        pass
    else:
        raise AssertionError("should fail to modify the dictionary")

    # test that we can't modify the inner lists
    try:
        args['b'][0] = 2
    except TypeError:
        pass
    else:
        raise AssertionError("should fail to modify the dictionary")

    # test that we can't modify the inner dictionary

# Generated at 2022-06-13 16:05:24.098571
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from ansible.cli.arguments import SINGLE_NOHOSTS
    assert GlobalCLIArgs.instance() == GlobalCLIArgs.instance()
    GlobalCLIArgs(SINGLE_NOHOSTS)

# Generated at 2022-06-13 16:05:28.634128
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import numbers

    class A(object):
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return repr(self.value)

    def to_set(*args):
        return frozenset(args)

    def to_dict(*args):
        return collections.OrderedDict(args)

    def to_nested_dict(*args):
        nested_dict = {}
        for key, value in args:
            if key == 'nested_dict':
                nested_dict[key] = value
        return nested_dict

    def to_nested_list(*args):
        nested_list = []
        for key, value in args:
            if key == 'nested_list':
                nested_list.append(value)
        return nested_

# Generated at 2022-06-13 16:05:32.324711
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        def __init__(self, x):
            self.x = x

    instance = A(42)
    assert instance is A(42)
    assert instance.x == 42

# Generated at 2022-06-13 16:05:38.293359
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    dict_ = dict(a=1, b=2, c=[1,2,3], d={'a': 'b'})
    result = CLIArgs(dict_)
    assert result == dict_
    assert isinstance(result, ImmutableDict)
    assert isinstance(result['c'], tuple)
    assert isinstance(result['d'], ImmutableDict)
    assert isinstance(result['d']['a'], text_type)

# Generated at 2022-06-13 16:05:45.753327
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options:
        def __init__(self):
            self.test = 1
            self.foo = [1, 2, 3]
            self.bar = True
            self.baz = {'a': 1, 'b': 2}
            self.complex = [{'a': 1, 'b': 2}, [1, 2, 3], (1, 2, 3), 1, 2, "test"]

    options = Options()
    cli_args = CLIArgs.from_options(options)

    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args, Mapping)
    assert isinstance(cli_args, ImmutableDict)

    # Test single value
    assert cli_args['test'] == 1

    # Test list

# Generated at 2022-06-13 16:05:54.701642
# Unit test for constructor of class CLIArgs
def test_CLIArgs():  # pylint: disable=too-few-public-methods
    """
    Test the CLIArgs class constructor
    """
    class Options(object):
        """Options object for the cliargs constructor"""
        def __init__(self):
            self.listvalue = ['a', 1, ['b', 2]]
            self.listvalue_v2 = ['a', 1, ['b', 2], (3, 4, 5)]
            self.setvalue = {'a', 1, ['b', 2]}
            self.dictvalue = {'a': ['b', 2]}
            self.dictvalue_v2 = {'a': {'b': 2, 'c': [3, 4]}, 'd': (1, 2, 3, 4)}

    options = Options()
    obj = CLIArgs.from_options(options)

# Generated at 2022-06-13 16:05:56.542613
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Verify that Python 2 and Python 3 can initialize this class
    assert CLIArgs({})

# Generated at 2022-06-13 16:05:59.344226
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class A:
        pass

    assert isinstance(A, ABCMeta)
    assert issubclass(A, Singleton)

# Generated at 2022-06-13 16:06:04.452515
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': {'aa': 1, 'ab': 2}, 'b': 3, 'c': [1, 2, 3]}
    my_cli_args = CLIArgs(mapping)
    assert isinstance(my_cli_args, ImmutableDict)
    assert isinstance(my_cli_args['a'], ImmutableDict)
    assert isinstance(my_cli_args['c'], tuple)

# Generated at 2022-06-13 16:06:15.650501
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    try:
        # This should be true, verify that it is
        assert GlobalCLIArgs is CLIArgs
    except:
        # If it isn't, then we're doing something wrong, fix it
        raise AssertionError("GlobalCLIArgs should be the same as CLIArgs, they are not")
    # Things added to runtime should be immutable
    test_runtime = GlobalCLIArgs({"verbosity": 3, "diff": True})
    try:
        # This should fail
        test_runtime["verbosity"] = 0
    except:
        # This is good, we want it to fail
        pass
    else:
        # This is bad, and requires a fix
        raise AssertionError("GlobalCLIArgs should be immutable, it is not")
    # Things added to runtime should be immutable,

# Generated at 2022-06-13 16:06:43.732232
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(B):
        pass

    assert isinstance(A(), A)
    assert isinstance(A(), B)
    assert isinstance(A(), C)
    assert isinstance(A(), D)

    assert isinstance(B(), A)
    assert isinstance(B(), B)
    assert isinstance(B(), C)
    assert isinstance(B(), D)

    assert isinstance(C(), A)
    assert isinstance(C(), B)
    assert isinstance(C(), C)
    assert isinstance(C(), D)

    assert isinstance(D(), A)
    assert isinstance(D(), B)
    assert isinstance(D(), C)

# Generated at 2022-06-13 16:06:48.377513
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    newargs = GlobalCLIArgs.from_options(ImmutableDict({'newarg': False, 'newarg2': {'newarg3': True}}))
    assert newargs == ImmutableDict({'newarg': False, 'newarg2': ImmutableDict({'newarg3': True})})

# Generated at 2022-06-13 16:06:50.691886
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    foo = GlobalCLIArgs({"foo": "bar"})
    assert foo["foo"] == "bar"


# Generated at 2022-06-13 16:06:55.839231
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.cli import CLI
    from ansible.errors import AnsibleOptionsError

    display = Display()
    cli = CLI(args=['asdf'], display=display, version=1.1)
    try:
        cli.parse()
    except AnsibleOptionsError:
        pass

    assert isinstance(GlobalCLIArgs.instance(), ImmutableDict)

# Generated at 2022-06-13 16:07:07.207008
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class Options:
        def __init__(self):
            self.foo = 'bar'
            self.baz = {'toast': 'jam'}
            self.qux = ['a', 'b', 'c']
            self.harry = {'potter': {'hagrid': 'rockcakes'}}

    options = Options()
    _make_immutable(options)
    cmd_line_args = GlobalCLIArgs.from_options(options)
    assert cmd_line_args.foo == 'bar'
    assert cmd_line_args.baz == ImmutableDict({'toast': 'jam'})
    assert cmd_line_args.qux == ('a', 'b', 'c')

# Generated at 2022-06-13 16:07:07.791423
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs()

# Generated at 2022-06-13 16:07:09.498688
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'a': {'b': 1}}
    c = CLIArgs(args)
    assert args == c

# Generated at 2022-06-13 16:07:14.150969
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # pylint: disable=too-few-public-methods
    class A(object):
        """
        An object that will use _ABCSingleton as a metaclass
        """
        pass

    class B(object):
        """
        An object that will use _ABCSingleton as a metaclass
        """
        pass

    assert issubclass(A, _ABCSingleton)
    assert issubclass(B, _ABCSingleton)

# Generated at 2022-06-13 16:07:17.789144
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        def __init__(self, a):
            self.a = a

    class B(_ABCSingleton):
        def __init__(self, b):
            self.b = b

    A(1)
    B(2)
    assert A.__dict__ == B.__dict__

# Generated at 2022-06-13 16:07:25.983081
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.constants
    from ansible.cli import CLI
    from ansible.errors import AnsibleOptionsError

    def check(options, expected):
        a = GlobalCLIArgs.from_options(options)
        options.base_parser = CLI.base_parser(constants=ansible.constants)
        if not options.help:
            cli = CLI(options)
            cli.parse()

        assert a == expected

    class test_options(object):
        class Options(object):
            def __init__(self, *args, **kwargs):
                self.opts = kwargs

            def __contains__(self, item):
                return item in self.opts

            def __getattr__(self, item):
                return self.opts[item]


# Generated at 2022-06-13 16:08:13.464972
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    mapping = {'foo': text_type('bar'), 'baz': int(42), 'qux': {'foobar': text_type('baz')}}
    args = GlobalCLIArgs(mapping)
    assert len(args.keys()) == 3
    assert args['foo'] == 'bar'
    assert args['baz'] == 42
    assert len(args['qux'].keys()) == 1
    assert isinstance(args['qux']['foobar'], text_type)
    assert args['qux']['foobar'] == 'baz'

# Generated at 2022-06-13 16:08:17.000457
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    result = CLIArgs({"a": "1", "b": "2"})
    assert result["a"] == "1"
    assert result["b"] == "2"

# Generated at 2022-06-13 16:08:21.458941
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class ABCSingletonTask(object):
        __metaclass__ = _ABCSingleton

    class ABCSingletonIterable(object):
        __metaclass__ = _ABCSingleton

    class ABCSingletonContainer(object):
        __metaclass__ = _ABCSingleton

GlobalCLIArgs().__init__({"a": "b"})

# Generated at 2022-06-13 16:08:25.646249
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    orig = {'a': 1, 'b': "string", 'c': [1, 2, 3]}
    args = GlobalCLIArgs.from_options(orig)
    hash(GlobalCLIArgs())
    assert args['a'] == 1
    assert args['b'] == 'string'
    assert args['c'] == (1, 2, 3)

# Generated at 2022-06-13 16:08:28.804490
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test the _ABCSingleton metaclass can be used
    """
    class Test(_ABCSingleton):
        pass
    assert type(Test) is _ABCSingleton

# Generated at 2022-06-13 16:08:32.867284
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test1(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            pass
    class Test2(Test1):
        def __init__(self):
            super(Test2, self).__init__()
    assert Test1() is Test2()
    assert Test1() is Test2()

# Generated at 2022-06-13 16:08:35.292060
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        """A class with _ABCSingleton as its metaclass"""
        __metaclass__ = _ABCSingleton
    assert len({TestClass(), TestClass()}) == 1

# Generated at 2022-06-13 16:08:41.566281
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    obj1 = CLIArgs({
        u'a': u'foo',
        u'b': {
            u'c': u'bar'
        },
        u'd': None,
        u'e': [
            {u'f': u'baz'},
            u'qux'
        ]
    })

    obj2 = CLIArgs({
        'a': 'foo',
        'b': {
            'c': 'bar'
        },
        'd': None,
        'e': [
            {'f': 'baz'},
            'qux'
        ]
    })


# Generated at 2022-06-13 16:08:44.268333
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    cli_args = GlobalCLIArgs({'some_key': 'some_value'})
    assert cli_args['some_key'] == 'some_value'

# Generated at 2022-06-13 16:08:54.842969
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    This is for testing the construction of _ABCSingleton.  It is not a test for the singleton
    class.  This test is only here to make sure that when _ABCSingleton is constructed that it is
    able to inherit from both the Singleton and ABCMeta classes.

    This test is needed because if you as a developer declare a class with this as the metaclass
    then python will call this function before allowing you to programmatically instantiate the
    class.  So this test tests the behavior of this file when python imports it and will prevent
    python from throwing exceptions on you during that import.
    """
    class MyClass(object):
        __metaclass__ = _ABCSingleton
    _ = MyClass()