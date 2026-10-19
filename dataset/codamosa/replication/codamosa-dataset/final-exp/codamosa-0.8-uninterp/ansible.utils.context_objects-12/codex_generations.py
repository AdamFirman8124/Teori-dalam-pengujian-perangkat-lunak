

# Generated at 2022-06-13 15:59:35.581055
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_dict = {
        "foo": "bar",
        "baz": {
            "blah": "blah"
        }
    }
    assert CLIArgs(cli_dict) == cli_dict
    assert type(CLIArgs(cli_dict)["baz"]) == ImmutableDict

# Generated at 2022-06-13 15:59:41.134456
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 15:59:52.036519
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {
        'one': 'two',
        'three': [
            'four',
            'five',
        ],
        'six': {
            'seven': 'eight',
            'nine': [
                'ten',
                'eleven',
            ]
        },
        'twelve': 'thirteen',
        'fourteen': 'fifteen',
    }
    cli_args = CLIArgs(args)
    # Constructor should have made all of the dicts and lists in this nested dict immutable
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args['three'], tuple)
    assert isinstance(cli_args['six'], ImmutableDict)
    assert isinstance(cli_args['six']['nine'], tuple)



# Generated at 2022-06-13 15:59:57.622245
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({
        'help': True,
        'verbosity': 3,
        'connection': 'changeme',
        'module_path': ['/tmp/yay', '/tmp/ponies'],
    })
    args_dup = GlobalCLIArgs(args)
    assert args is args_dup
    assert args == args_dup

# Generated at 2022-06-13 15:59:58.529331
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    CLIArgs.from_options([])

# Generated at 2022-06-13 16:00:01.478346
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    expected = ImmutableDict(
        {'a': 1, 'b': 2, 'c': 3}
    )
    result = CLIArgs({'a': 1, 'b': 2, 'c': 3})
    assert expected == result



# Generated at 2022-06-13 16:00:05.381509
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Temp(object):
        """Class to use for testing if Singleton and ABCMeta can be combined."""

        __metaclass__ = _ABCSingleton

    assert isinstance(Temp, Singleton)
    assert issubclass(Temp, ABCMeta)

# Generated at 2022-06-13 16:00:14.914916
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli import CLI
    from ansible.utils.path import unfrackpath
    from ansible.utils.display import Display

    display = Display()
    parser = CLI.base_parser(constants=CLI._load_constants(),
                             usage="%prog [options]",
                             epilog="See '%prog --help' for more information.",
                             fromfile_prefix_chars='@')
    parser.add_option("-i", "--inventory-file", dest="inventory",
                      help="specify inventory host file (default=%s)" % unfrackpath('/etc/ansible/hosts'))
    parser.add_option('-l', '--limit', dest='subset',
                      help='further limit selected hosts to an additional pattern')

# Generated at 2022-06-13 16:00:21.767358
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib'))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from ansible.cli.arguments import CLIArgumentParser
    parser = CLIArgumentParser(description='Handles CLI args and configuration')
    parser.parse_args()

if __name__ == '__main__':
    test_GlobalCLIArgs()

# Generated at 2022-06-13 16:00:31.462933
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class MockOptparse(object):
        def __init__(self):
            self.foo = 'bar'
            self.baz = 32
            self.qux = ['mine', 'ours', 'theirs']
            self.quux = {'me': 'you', 'her': 'him'}

    obj = CLIArgs.from_options(MockOptparse())

    assert obj['foo'] == 'bar'
    assert obj['baz'] == 32
    assert obj['qux'] == ('mine', 'ours', 'theirs')
    assert obj['quux'] == {'me': 'you', 'her': 'him'}

    # Test that the object becomes immutable
    try:
        obj['foo'] = 'baz'
    except:
        pass
    else:
        assert False


# Generated at 2022-06-13 16:00:43.241996
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        pass

    class B(object):
        __metaclass__ = _ABCSingleton

    class C(A):
        pass

    class D(A):
        __metaclass__ = _ABCSingleton

    assert not issubclass(A, _ABCSingleton)
    assert issubclass(A, ABCMeta)
    assert issubclass(A, Singleton)
    assert issubclass(A, object)

    assert issubclass(B, _ABCSingleton)
    assert issubclass(B, ABCMeta)
    assert issubclass(B, Singleton)
    assert issubclass(B, object)

    assert issubclass(C, _ABCSingleton)
    assert issubclass(C, ABCMeta)
    assert issubclass(C, Singleton)
    assert issub

# Generated at 2022-06-13 16:00:45.065389
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """ Test that GlobalCLIArgs is a singleton """
    Ga = GlobalCLIArgs()
    Ga1 = GlobalCLIArgs()
    assert id(Ga) == id(Ga1)

# Generated at 2022-06-13 16:00:56.921308
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Create a data structure that exercises all of the different types that can be made immutable
    """
    test_dict = {
        'one': 'two',
        'three': {
            'long': 'four',
            'list': [
                'five',
                'six',
                'seven',
                {
                    'eight': 'nine'
                },
                [
                    'ten',
                    'eleven',
                    {
                        'twelve': 'thirteen'
                    }
                ]
            ]
        },
        'fourteen': ['fifteen', {'sixteen': 'seventeen'}],
        'eighteen': frozenset([19]),
        20: []
    }

    # Constructor should be callable
    GlobalCLIArgs(test_dict)

    # Constructor should produce a mapping, so

# Generated at 2022-06-13 16:01:02.976613
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Create a self-named subclass of _ABCSingleton to test it.
    class TestClass(object, metaclass=_ABCSingleton):
        def __init__(self, x):
            self.x = x

    c1 = TestClass(5)
    c2 = TestClass(9)
    assert c1 is c2
    assert c1.x == 9
    assert c2.x == 9



# Generated at 2022-06-13 16:01:13.238146
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    obj = CLIArgs({'a': {1: 2, 3: 4}, 'b': set([1, 2]), 'c': [1, 2, 3]})

    assert isinstance(obj, ImmutableDict)
    assert isinstance(obj['b'], frozenset)
    assert isinstance(obj['c'], tuple)

    # Check that we don't make immutable data structures immutable
    non_immutable_dict = {'a': 1}
    obj = CLIArgs(non_immutable_dict)
    assert id(obj) != id(non_immutable_dict)
    assert id(obj['a']) == id(non_immutable_dict['a'])

# Generated at 2022-06-13 16:01:20.520931
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Mixin(object):
        pass

    class MutableData(Mapping, Mixin):
        def __init__(self, data):
            self.__data = data

        def __iter__(self):
            return self.__data.__iter__()

        def __len__(self):
            return self.__data.__len__()

        def __getitem__(self, item):
            return self.__data.__getitem__(item)

    class ImmutableData(_ABCSingleton, MutableData):
        pass

    data = dict(a='a', b='b', c='c')
    immutable_data = ImmutableData(data)
    assert len(immutable_data) == 3
    assert list(immutable_data) == ['a', 'b', 'c']


# Generated at 2022-06-13 16:01:27.416852
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # This should work and not raise an error:
    class ABCSingletonTest1(metaclass=_ABCSingleton):
        pass

    # This should work and not raise an error:
    class ABCSingletonTest2(object):
        __metaclass__ = _ABCSingleton

    # This should raise an error because the metaclass is not listed first in the base classes:
    class ABCSingletonTest3(object, metaclass=_ABCSingleton):
        pass

# Generated at 2022-06-13 16:01:30.954894
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    assert isinstance(A(), A)
    assert isinstance(A(), B)
    assert isinstance(B(), A)
    assert isinstance(B(), B)


# Generated at 2022-06-13 16:01:37.033058
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    import io
    import unittest

    class TestGlobalCLIArgs(unittest.TestCase):
        def setUp(self):
            self.saved_stderr = sys.stderr
            self.saved_stdout = sys.stdout
            sys.stderr = io.StringIO()
            sys.stdout = io.StringIO()

        def tearDown(self):
            sys.stderr = self.saved_stderr
            sys.stdout = self.saved_stdout
            sys.argv = []

        def test_args_singleton(self):
            from ansible.utils.singleton import Singleton
            from ansible.utils.display import Display
            from ansible.config.args import GlobalCLIArgs


# Generated at 2022-06-13 16:01:39.856572
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca = GlobalCLIArgs({'x': 'y'})
    _make_immutable(gca)

# Generated at 2022-06-13 16:01:45.591349
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    GlobalCLIArgs constructor
    """
    # pylint: disable=unused-variable
    global_cliargs_obj = GlobalCLIArgs.instance()

# Generated at 2022-06-13 16:01:55.896972
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import action_loader, connection_loader, module_loader
    from ansible.plugins.connection.persistent import Connection

    parser  = optparse.OptionParser()
    options = parser.parse_args([])[0]

    for loader in module_loader, connection_loader, action_loader:
        for plugin_name, plugin in loader.all(class_only=True).items():
            if plugin_name == 'persistent':
                root_plugin_name = plugin_name
                break
            else:
                root_plugin_name = plugin.split('.')[0]
                break

    options.connection = root_plugin_name
    options.module_path = ''
    options.forks = 5
    options.remote_

# Generated at 2022-06-13 16:01:58.456341
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.argparse import Namespace
    GlobalCLIArgs(Namespace(debug=True, listtasks=False, listtags=False, verbosity=1))

# Generated at 2022-06-13 16:02:05.512152
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({}) == {}
    assert CLIArgs({'a': 1}) == {'a': 1}
    assert CLIArgs({'a': {'b': {'c': 1}}}) == {'a': {'b': {'c': 1}}}
    assert CLIArgs({'a': {'b': [1, 2]}}) == {'a': {'b': (1, 2)}}
    assert CLIArgs({'a': frozenset([1, 2, 3])}) == {'a': frozenset([1, 2, 3])}
    assert CLIArgs({'a': 'b'}) == {'a': 'b'}
    assert CLIArgs({'a': (1, 2, 3)}) == {'a': (1, 2, 3)}

# Generated at 2022-06-13 16:02:06.900185
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({}) == {}

# Generated at 2022-06-13 16:02:09.080084
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Verify that _ABCSingleton works as expected"""
    class ConcreteSample(_ABCSingleton):
        pass

    assert isinstance(ConcreteSample.__class__, ABCMeta)

# Generated at 2022-06-13 16:02:18.121985
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.config.args import CLIArgs
    from ansible.config.args import GlobalCLIArgs
    from ansible.config.args import Singleton
    from ansible.config.args import _make_immutable
    from ansible.module_utils.six import add_metaclass
    assert issubclass(GlobalCLIArgs, CLIArgs)
    assert issubclass(GlobalCLIArgs, Singleton)
    assert GlobalCLIArgs is GlobalCLIArgs()
    assert GlobalCLIArgs() is GlobalCLIArgs()
    assert GlobalCLIArgs.from_options(None) is GlobalCLIArgs()
    assert GlobalCLIArgs.from_options({}) is GlobalCLIArgs()
    assert GlobalCLIArgs.from_options({}) == GlobalCLIArgs()

# Generated at 2022-06-13 16:02:20.639507
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # TODO(spartaco): Write unit tests which verify the behaviour of CLIArgs
    #                 with non-immutable containers.
    pass

# Generated at 2022-06-13 16:02:29.407378
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'key1': 'value1',
               'key2': 'value2',
               'key3': {'key4': 'value4',
                        'key5': 'value5'},
               'key6': ['value6', 'value7', 'value8', 'value9'],
               'key10': [{'key11': 'value11'},
                         {'key12': 'value12'},
                         {'key13': 'value13'}],
               'key14': {'key15': [{'key16': 'value16'},
                                   {'key17': 'value17'}]}}
    cli_args = CLIArgs(mapping)
    cli_args_dict = cli_args.copy()
    assert cli_args_dict == mapping

# Generated at 2022-06-13 16:02:41.169143
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Unit test for constructor of class _ABCSingleton

    Create two classes using the same metaclass (and thus, one inheritance hierarchy) and make sure
    that the Singleton's __init__ is called before the ABCMeta's __init__.  This unit test assumes
    that a check for self.__initialized is done before returning a Singleton object and that self.__initialized is
    set to true after that check.  If the order of __init__ calls is changed, then the ABCMeta's
    __init__ will be called before the Singleton's __init__ and the final check will fail.
    """
    global _init_order
    _init_order = []

    class TestClassMeta(_ABCSingleton):
        def __init__(self, name, bases, namespace):
            _init_order.append('metaclass')

# Generated at 2022-06-13 16:02:55.540696
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Sanity check that ABCMeta and Singleton are combined into one metaclass
    class A(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, arg):
            self.arg = arg

    class B(A):
        pass

    a = A('test')
    assert a.arg == 'test'
    b = B('test2')
    assert b.arg == 'test2'

    # ABCMeta should be able to override methods in A
    class C(A):
        def __init__(self, arg):
            pass

    with raises(TypeError):
        C('test')

    # Singleton should be able to override methods in A

# Generated at 2022-06-13 16:03:03.113612
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    class Options:
        def __init__(self, mapping):
            for key, value in mapping.items():
                setattr(self, key, value)


# Generated at 2022-06-13 16:03:06.201364
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'abc': 'ASD', 'def': 'DDD'}
    result = CLIArgs(test_dict)
    assert isinstance(result, ImmutableDict)
    assert result == ImmutableDict(test_dict)


# Generated at 2022-06-13 16:03:08.159159
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(ImmutableDict):
        pass

    class A(X):
        pass

    class B(X):
        pass

    assert A == B

# Generated at 2022-06-13 16:03:17.635895
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import collections
    input_dict = {
        'connection': 'local',
        'verbosity': 3,
    }
    args = CLIArgs(input_dict)
    assert isinstance(args, CLIArgs)

    # Test that it is immutable and unmodifiable
    for key, value in input_dict.items():
        assert args[key] == value
        assert isinstance(args[key], AnsibleUnsafeText)
        assert not isinstance(args[key], collections.MutableMapping)
        assert not isinstance(args[key], collections.MutableSet)
        assert not isinstance(args[key], collections.MutableSequence)
        try:
            args[key] = 'blah'
        except TypeError:
            assert True
       

# Generated at 2022-06-13 16:03:19.222109
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    instance = GlobalCLIArgs.instance([])

# Generated at 2022-06-13 16:03:27.706927
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Check on empty case
    result = CLIArgs({})
    assert isinstance(result, ImmutableDict)
    assert result == {}

    # Check on only top level strings
    mapping = {'string-key': "string-value"}
    result = CLIArgs(mapping)
    assert isinstance(result, ImmutableDict)
    assert result == mapping

    # Check on top level list and dictionary
    mapping = {'list-key': [1, 2, 3], 'dict-key': {'a': 1, 'b': 2}}
    result = CLIArgs(mapping)
    assert isinstance(result, ImmutableDict)
    assert result == mapping

    # Check on dictionary with both list and dictionary

# Generated at 2022-06-13 16:03:28.422891
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs(vars(options))

# Generated at 2022-06-13 16:03:38.751190
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class C(object):
        __metaclass__ = _ABCSingleton
        def __init__(self, x=1):
            self.x = x

    c1 = C()
    c2 = C()

    assert c1.x == 1
    assert c2.x == 1

    c1.x = 2
    assert c1.x == 2
    assert c2.x == 2

    assert c1 == c2
    assert id(c1) == id(c2)

    c3 = C(3)
    assert c3.x == 2

    assert c3 == c1 == c2
    assert id(c1) == id(c2) == id(c3)



# Generated at 2022-06-13 16:03:42.043275
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    argv = ['ansible', '-m', 'foo', '-a', 'bar']
    global_args = GlobalCLIArgs.from_options(argv)
    assert global_args['module_name'] == 'foo'
    assert global_args['module_args'] == 'bar'

# Generated at 2022-06-13 16:03:53.886883
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {'listtags': 'list'}
    options = type('', (), args)
    args = GlobalCLIArgs.from_options(options)
    assert 'listtags' in args
    assert args['listtags'] == 'list'



# Generated at 2022-06-13 16:04:01.908831
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Test that the metaclass _ABCSingleton can create a class that looks like a Singleton"""
    class AbstractSingletonTest(GlobalCLIArgs):
        """Test class for verifying that Abstract Singleton can be constructed"""
        def __init__(self):
            super(AbstractSingletonTest, self).__init__({'foo': 'bar'})
    try:
        AbstractSingletonTest()
    except TypeError:
        assert False, "Can't construct an abstract Singleton"
    assert True, "Abstract Singleton was constructable"

# Generated at 2022-06-13 16:04:02.943109
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Dummy(object):
        # noop
        pass
    a = Dummy()
    b = Dummy()
    assert a is b

# Generated at 2022-06-13 16:04:11.299550
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'boo': 10,
               'far': {'baz': [2, 3, 4],
                       'zoink': 'zoink'
                       },
               'woo': {'foo': 'foo',
                       'bar': 'bar'
                       }
               }

    args = CLIArgs(mapping)
    for key, value in mapping.items():
        assert args[key] == value
    assert len(args) == len(mapping)
    assert args == mapping
    assert args == CLIArgs(mapping)
    assert mapping == args
    assert set(args) == set(mapping)
    assert set(mapping) == set(args)
    assert args.keys() == tuple(mapping.keys())
    assert args.keys() == set(mapping.keys())

# Generated at 2022-06-13 16:04:23.135070
# Unit test for constructor of class CLIArgs
def test_CLIArgs():

    # Non-recursive structure
    assert CLIArgs.from_options(
        ImmutableDict(
            ansible={
                'foo': 'bar',
                'baz': 'qux',
            }
        )
    ) == ImmutableDict(
        ansible={
            'foo': 'bar',
            'baz': 'qux',
        }
    )

    # Recursive arrays (tuples)

# Generated at 2022-06-13 16:04:29.599187
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Ensure that immutability is set correctly by subclassing GlobalCLIArgs to remove the
    singleton behaviour and calling the constructor
    """
    args = {'a': 1, 'b': {1: 2, 2: 3}, 'c': [1, 2, 3], 'd': 'hello'}
    test_args = GlobalCLIArgs(args)
    assert isinstance(test_args, ImmutableDict)
    assert test_args['a'] == 1

# Generated at 2022-06-13 16:04:38.411974
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': [0, 1, 2],
               'm': {'b': {'c': 0},
                     'd': [1, 2, 3],
                     'e': {'f': {'g': {'h': 0}}}
                     },
               'n': 'g'
               }
    cli_args = CLIArgs(mapping)
    # check cli_args is immutable
    mapping['a'][0] = 100
    assert cli_args['a'] == (0, 1, 2)
    assert cli_args['a'][0] == 0
    mapping['m']['b']['c'] = 100
    assert cli_args['m']['b']['c'] == 0
    assert cli_args['m']['d'] == (1, 2, 3)

# Generated at 2022-06-13 16:04:43.320341
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(metaclass=_ABCSingleton):
        pass
    a = Foo()
    b = Foo()
    assert a is b
    class Foo2(Foo):
        pass
    # ABCMeta, being a named metaclass, is higher on the metaclass resolution tree than _ABCSingleton,
    # so they are considered equivalent and you can subclass them together.
    c = Foo2()
    assert c is a

# Generated at 2022-06-13 16:04:47.543089
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestClass(_ABCSingleton):
        def __init__(self):
            pass

    t1 = _TestClass()
    t2 = _TestClass()

    assert t1 is t2, '_TestClass should be a Singleton'

# Generated at 2022-06-13 16:04:57.621000
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections as _collections
    import os as _os
    import ansible.module_utils.basic as _basic


# Generated at 2022-06-13 16:05:21.825104
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    import tempfile

    # Test basic construction, aka turning a dict into an ImmutableDict
    assert isinstance(CLIArgs(dict(a=1, b=2)), collections.Mapping)

    with tempfile.NamedTemporaryFile() as fp:
        # Test a simple case of reading a file
        fp.write(b"a: a\nb: b\n")
        fp.flush()
        # Test reading from a file
        assert CLIArgs.from_options(dict(vault_password_file=fp.name)) == ImmutableDict(dict(vault_password_file=fp.name))

        # Test a simple example of reading a file contents
        fp.write(b"foo")
        fp.flush()

# Generated at 2022-06-13 16:05:24.707039
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Verify initialization of GlobalCLIArgs works
    """
    # No function in the class so just instantiate it here and make the tests
    GlobalCLIArgs()

# Generated at 2022-06-13 16:05:25.904462
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs.from_options('options')

# Generated at 2022-06-13 16:05:30.219472
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass
    class Bar(_ABCSingleton):
        pass

    foo = Foo()
    bar = Bar()

    assert foo is not bar
    assert foo == bar
    assert hash(foo) == hash(bar)


# Generated at 2022-06-13 16:05:33.754657
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    class Bar(object):
        __metaclass__ = _ABCSingleton

    assert Foo() is Foo()
    assert Foo() is not Bar()

# Generated at 2022-06-13 16:05:39.736979
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    input_dict = {'a': 1, 'b': 2}
    input_dict2 = {'c': 3}
    test_object = CLIArgs(input_dict)
    assert test_object['a'] == 1 and test_object['b'] == 2
    test_object2 = CLIArgs(input_dict2)
    assert test_object2['c'] == 3

# Generated at 2022-06-13 16:05:47.351072
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    try:
        a = GlobalCLIArgs({})
    except AssertionError:
        a = None
    assert a is None

    try:
        a = GlobalCLIArgs._make_empty()
    except AssertionError:
        a = None
    assert a is None

    try:
        a = GlobalCLIArgs({'one': 1})
    except AssertionError:
        a = None
    assert a is None

    try:
        a = GlobalCLIArgs({'one': 'one'})
    except AssertionError:
        a = None
    assert a is None

    try:
        a = GlobalCLIArgs({'one': [1, 2, 3]})
    except AssertionError:
        a = None
    assert a is None


# Generated at 2022-06-13 16:05:51.066472
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # First test that the "from_options" method works
    from argparse import Namespace
    args = Namespace(foo='bar', baz='qux')
    test_cli_args = CLIArgs.from_options(args)

# Generated at 2022-06-13 16:05:58.524210
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Simple test to ensure that the CLIArgs constructor stores immutable data
    obj = CLIArgs({'key1': 'value1'})
    assert obj == ImmutableDict({'key1': 'value1'})
    # Now test to make sure that a nested object is made immutable
    obj = CLIArgs({'key1': {'key2': 'value2'}})
    assert obj == ImmutableDict({'key1': ImmutableDict({'key2': 'value2'})})
    # And test with a nested list
    obj = CLIArgs({'key1': [{'key2': 'value2'}]})
    assert obj == ImmutableDict({'key1': (ImmutableDict({'key2': 'value2'}), )})

# Generated at 2022-06-13 16:06:02.691721
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'monkey': ['dude', 'chimp'], 'chicken': 'wings'}
    options = type('Options', (object,), mapping)
    args = CLIArgs(mapping)
    assert args == mapping
    args = CLIArgs.from_options(options)
    assert args == mapping

# Generated at 2022-06-13 16:06:34.205101
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class A(object):
        pass

    a = A()
    assert a is A()

# Generated at 2022-06-13 16:06:43.523977
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-log', action='store_false', dest='writelog', default=True)
    options, _ = parser.parse_known_args()

    # See https://github.com/ansible/ansible/issues/39816
    # Use the dict below to verify correct behavior
    # args = dict(writelog=True)
    args = GlobalCLIArgs.from_options(options)
    assert args.writelog

    # See https://github.com/ansible/ansible/issues/39816
    # Use the dict below to verify correct behavior
    # args.writelog = False
    # assert args.writelog == False

    # See https://docs.python.org/2/library/functions.html#v

# Generated at 2022-06-13 16:06:48.335055
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object):
        pass
    options = Options()
    options.foo = "bar"
    gc1 = GlobalCLIArgs.from_options(options)
    gc2 = GlobalCLIArgs.from_options(options)
    assert gc1 is gc2
    assert gc1 == gc2

# Generated at 2022-06-13 16:06:54.369670
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        def __init__(self, foo, bar, baz):
            self.foo = foo
            self.bar = bar
            self.baz = baz

    # Test the constructor
    options = Options("foo", "bar", "baz")
    args = CLIArgs.from_options(options)
    assert args.foo == "foo"
    assert args.bar == "bar"
    assert args.baz == "baz"

# Generated at 2022-06-13 16:06:58.319391
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'one': 1, 'two': 2}
    args = CLIArgs(mapping)
    for key in mapping.keys():
        assert mapping[key] == args[key]
    assert 'one' in args
    assert 'not_in_mapping' not in args
    assert args == mapping


# Generated at 2022-06-13 16:07:03.084411
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyClassABC(object):
        __metaclass__ = _ABCSingleton
        def __init__(self, arg):
            self.arg = arg

    class MyClassSingleton(object):
        __metaclass__ = _ABCSingleton
        def __init__(self, arg):
            self.arg = arg

    MyClassABC('foo')
    MyClassABC('bar')

    MyClassSingleton('foo')
    MyClassSingleton('bar')

# Generated at 2022-06-13 16:07:13.176085
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = {
        'x': {
            'y': [1, 2, 3],
            'z': {
                'a': {
                    'b': 'val'
                }
            }
        }
    }

    args = CLIArgs(data)

    # Top level
    assert isinstance(args, ImmutableDict)
    assert isinstance(args.get('x'), ImmutableDict)
    assert isinstance(args.get('x').get('z'), ImmutableDict)
    assert isinstance(args.get('x').get('y'), tuple)

    # Two layers in
    assert isinstance(args.get('x').get('z').get('a'), ImmutableDict)
    assert isinstance(args.get('x').get('z').get('a').get('b'), text_type)

    #

# Generated at 2022-06-13 16:07:21.793362
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    obj1 = {
        "a": "b",
        "c": set(["d"]),
        "e": ["f", set(["g"])]
    }
    obj2 = CLIArgs(obj1)
    assert obj1 == obj2
    try:
        obj2["a"] = "b"
    except TypeError:
        pass
    else:
        assert False
    try:
        obj2["c"] = "d"
    except TypeError:
        pass
    else:
        assert False
    try:
        obj2["e"] = "f"
    except TypeError:
        pass
    else:
        assert False

# Generated at 2022-06-13 16:07:29.316465
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    import types
    import copy

    mapping = {
        'key1': 'value1',
        'key2': [1, 2, 3],
        'key3': {
            'key31': 'value31',
            'key32': 'value32'
        }
    }

    # Make a copy of the dictionary so we can compare after we convert it to an ImmutableDict
    mapping_copy = copy.copy(mapping)

    # Make sure we can init with a dict
    cli_args = CLIArgs(mapping)

    # Make sure the mapping is as expected
    assert cli_args == mapping_copy

    # Make sure it is an ImmutableDict
    assert isinstance(cli_args, ImmutableDict)

    # Make sure the mapping is immutable and all the nested key, value pairs are immutable

# Generated at 2022-06-13 16:07:31.791443
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Ferret(object):
        __metaclass__ = _ABCSingleton

    f1 = Ferret()
    f2 = Ferret()
    assert f1 is f2

# Generated at 2022-06-13 16:08:44.796441
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_text
    import json

    class Options():
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


# Generated at 2022-06-13 16:08:56.642906
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():

    # We have to have a command line for the next line to work
    import sys
    from optparse import OptionParser

    # Create a mock command line
    parser = OptionParser()
    parser.add_option('-a', action="store_const", const='const', dest="const", help="const help")
    parser.add_option('-b', action="store", type="int", dest="int", help="int help")
    parser.add_option('-c', action="store", type="string", dest="string", help="string help")
    parser.add_option('-d', action="store_true", dest="boolean_true", default=False, help="boolean_true help")

# Generated at 2022-06-13 16:09:02.170010
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert isinstance(CLIArgs([]), ImmutableDict)
    assert isinstance(CLIArgs({}), ImmutableDict)
    assert isinstance(CLIArgs({"foo": "bar"}), ImmutableDict)
    assert isinstance(CLIArgs({"foo": {"bar": "baz"}}), ImmutableDict)
    assert isinstance(CLIArgs({"foo": ["bar", "baz"]}), ImmutableDict)



# Generated at 2022-06-13 16:09:09.969130
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest

    class Options(object):
        def __init__(self, **kwds):
            self.__dict__.update(kwds)

    options = Options(
        module_path='/tmp',
        tree='/tree',
        forks=10,
    )

    GlobalCLIArgs.from_options(options)
    with pytest.raises(RuntimeError) as excinfo:
        GlobalCLIArgs.from_options(options)
    assert 'GlobalCLIArgs already instanced' in str(excinfo.value)

# Generated at 2022-06-13 16:09:18.469514
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    d = {'b': 2}
    f = {'a': d, 'b': 3}
    e = CLIArgs(f)

    # Make sure it was converted to an immutable dictionary
    assert isinstance(e, ImmutableDict)

    # Make sure it is still possible to access the data
    assert e['a']['b'] == 2
    assert e['b'] == 3

    # Make sure that the original data is still mutable
    d['b'] = 3
    assert e['a']['b'] == 2

    # Test a second of data
    d = {'c', 2}
    f = {'a': d, 'b': 3}
    e = CLIArgs(f)

    # Make sure it was converted to an immutable dictionary
    assert isinstance(e, ImmutableDict)

    # Make sure

# Generated at 2022-06-13 16:09:28.780766
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import datetime
    import random
    import uuid
    import collections

    # Create a data structure with various immutable and mutable types, then
    # construct a CLIArgs object from it and verify that it becomes immutable
    date_time = datetime.datetime.now()
    date = datetime.date.today()
    uuid_obj = uuid.uuid4()
    random_obj = random.random()