

# Generated at 2022-06-13 15:59:39.343867
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass

    class Bar(_ABCSingleton):
        pass

    f1 = Foo()
    f2 = Foo()
    b1 = Bar()

    assert f1 == f2
    assert b1 != f1
    assert b1 != f2

# Generated at 2022-06-13 15:59:45.810495
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test can create a new object
    cli_args = CLIArgs({})
    # Test dictionary is immutable
    try:
        cli_args['key'] = 'value'
        assert False
    except TypeError:
        pass
    # Test dict can have a dict
    cli_args = CLIArgs({'key': {'inner_key': 'inner_value'}})
    assert cli_args['key']['inner_key'] == 'inner_value'
    # Test inner dict is immutable
    try:
        cli_args['key']['inner_key'] = 'value'
        assert False
    except TypeError:
        pass
    # Test dict can have a list
    cli_args = CLIArgs({'key': ['item1']})

# Generated at 2022-06-13 15:59:51.831186
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    a1 = A()
    a2 = A()
    assert a1 is a2
    assert a1 == a2

    b1 = B()
    b2 = B()
    assert b1 is b2
    assert b1 == b2

    assert a1 is not b1
    assert a1 != b1

# Generated at 2022-06-13 15:59:59.001986
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    from ansible.cli.adhoc import AdHocCLI
    from ansible.cli import CLI
    cli = AdHocCLI(sys.argv)
    opt = cli.parse()
    args = CLIArgs.from_options(opt)
    assert isinstance(args, CLIArgs)
    assert isinstance(args, ImmutableDict)
    assert not isinstance(args, GlobalCLIArgs)
    assert isinstance(args, Mapping)


# Generated at 2022-06-13 16:00:01.969803
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    _ABCSingleton(text_type, (object,), {})

# Generated at 2022-06-13 16:00:10.740260
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # This class is a singleton, and we just want to know that its constructor is working.
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.collections import ImmutableDict, ImmutableList
    from ansible.module_utils.six import string_types, text_type, binary_type

    class Options(object):
        cat = "cat"
        dog = u"dog"
        foo = AnsibleUnsafeText(u"foo")
        bar = boolean(True)
        baz = False
        bat = [u"bat1", u"bat2", AnsibleUnsafeText(u"bat3")]
        barf = [3, 2, 1]

# Generated at 2022-06-13 16:00:20.207314
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test that CLIArgs properly makes all it's values immutable
    """
    # pylint: disable=unused-argument
    def modify_sequence(seq):
        """
        Modify a sequence.

        This is used in the unit test to check that all nested data structures are immutable.
        """
        seq[0] = True

    def modify_set(the_set):
        """
        Modify a set

        This is used in the unit test to check that all nested data structures are immutable.
        """
        the_set.add(True)

    def modify_mapping(mapping):
        """
        Modify a mapping

        This is used in the unit test to check that all nested data structures are immutable.
        """
        mapping[True] = False


# Generated at 2022-06-13 16:00:30.370948
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(A):
        # class B inherits from A, and is also a singleton
        pass
    class C(B):
        # class C inherits from B, and is also a singleton
        pass
    class D(B):
        # class D inherits from B, and is also a singleton
        pass

    # verify that we can get separate instances of each class
    # by calling each directly
    a = A()
    b = B()
    c = C()
    d = D()

    # Now verify that we get the expected instances when we call
    # get_instance for each class.
    x = A.get_instance()
    assert x == a

    y = B.get_instance()
    assert y == b

    z

# Generated at 2022-06-13 16:00:35.244125
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs({'verbosity': 1})
    assert global_cli_args
    assert isinstance(global_cli_args, ImmutableDict)
    item = global_cli_args.get('verbosity')
    assert item == 1

# Generated at 2022-06-13 16:00:44.274694
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonMetaclassType(object):
        __metaclass__ = _ABCSingleton
        pass

    class NonSingletonMetaclassType(object):
        pass

    # should be a subclass of ABCMeta
    assert issubclass(_ABCSingleton, ABCMeta)

    # should be a subclass of Singleton
    assert issubclass(_ABCSingleton, Singleton)

    # issue #30697: ensure that a class with a metaclass derived from _ABCSingleton is also a Singleton
    # (as well as ABC)
    assert issubclass(SingletonMetaclassType, Singleton)
    assert issubclass(SingletonMetaclassType, ABCMeta)

    # ensure that a class without a metaclass derived from _ABCSingleton is not a Singleton
    # (or ABC)

# Generated at 2022-06-13 16:00:58.225440
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest
    from ansible.module_utils.common.network import NetworkError
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.utils.display import Display
    from ansible.utils.path import module_loader


# Generated at 2022-06-13 16:01:00.136958
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs({'var1': 1, 'var2': 2})

# Generated at 2022-06-13 16:01:04.076608
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    myargs = CLIArgs({'a': 1, 'b': {'c': 2, 'd': 3}, 'f': [1, 2, 3, 4]})
    assert myargs == {'a': 1, 'b': {'c': 2, 'd': 3}, 'f': [1, 2, 3, 4]}

# Generated at 2022-06-13 16:01:10.352761
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs(dict(a=1))
    GlobalCLIArgs(dict(a=dict(b=2)))
    GlobalCLIArgs(dict(a=dict(b=dict(c=[1,2,3]))))
    GlobalCLIArgs(dict(a=dict(b=dict(c=set([1,2,3])))))

# Generated at 2022-06-13 16:01:14.369632
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class MyOptions(object):
        def __init__(self, foo, bar, baz):
            self.foo = foo
            self.bar = bar
            self.baz = baz

    args = MyOptions(
        "foo",
        ["bar1", "bar2"],
        {"baz1": 1, "baz2": 2}
    )
    GlobalCLIArgs.from_options(args)

# Generated at 2022-06-13 16:01:16.065092
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Create a single GlobalCLIArgs instance to test that the constructor works properly
    """
    GlobalCLIArgs()

# Generated at 2022-06-13 16:01:18.286110
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MySingleton(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(MySingleton, Singleton)
    assert issubclass(MySingleton, ABCMeta)

# Generated at 2022-06-13 16:01:21.173749
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _SingletonClass(metaclass=_ABCSingleton):
        pass

    assert issubclass(_SingletonClass, Singleton)
    assert issubclass(_SingletonClass, ABCMeta)

# Generated at 2022-06-13 16:01:31.349582
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display

# Generated at 2022-06-13 16:01:34.901443
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs({'_ansible_socket_path': '/path/to/socket'})
    GlobalCLIArgs.reset()



# Generated at 2022-06-13 16:01:43.883801
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo:
        __metaclass__ = _ABCSingleton
        pass

    class Bar(Foo, Sequence):
        pass

    assert issubclass(Foo, ABCMeta)
    assert issubclass(Foo, Singleton)
    assert not issubclass(Foo, Sequence)

    assert issubclass(Bar, ABCMeta)
    assert issubclass(Bar, Singleton)
    assert issubclass(Bar, Sequence)

# Generated at 2022-06-13 16:01:49.124771
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class OldClass(object):
        __metaclass__ = ABCMeta

        def __init__(self):
            pass

    class NewClass(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    assert issubclass(OldClass, ABCMeta)
    assert issubclass(NewClass, ABCMeta)

    assert issubclass(OldClass, Singleton)
    assert issubclass(NewClass, Singleton)

# Generated at 2022-06-13 16:01:59.804662
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import tempfile

    # Create command line arguments
    from ansible.cli import CLI as AnsibleCLI
    cli = AnsibleCLI([])
    cli.options = cli.parse()[0]

    # Test the accepted command line arguments
    global_args = GlobalCLIArgs.from_options(cli.options)
    assert global_args['become'] is False
    assert global_args['become_method'] == 'sudo'
    assert global_args['become_user'] == 'root'
    assert global_args['check'] is False
    assert global_args['connection'] == 'smart'
    assert global_args['diff'] is False
    assert global_args['forks'] == 5
    assert global_args['inventory'] == '/etc/ansible/hosts'

    # See https://

# Generated at 2022-06-13 16:02:07.862582
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from collections import MutableMapping

    class MutableMappingSubclass(MutableMapping):
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

    # Test mutable mapping subclass is mutable
    cli_args_normal = CLIArgs(MutableMappingSubclass({'a': 1, 'b': 2}))

# Generated at 2022-06-13 16:02:09.197665
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=unused-variable
    GlobalCLIArgs()

# Generated at 2022-06-13 16:02:10.619067
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs({"a": 3})
    try:
        a["a"] = 4
        assert False, "GlobalCLIArgs should not be mutable"
    except TypeError:
        pass

# Generated at 2022-06-13 16:02:11.177376
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:02:19.307871
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """This is the test for adding new arguments to the command line.
    """
    import os
    import tempfile

    from ansible.cli import CLI

    class OptionsMock(object):
        def __init__(self):
            self.connection = ''
            self.forks = 1
            self.become = False
            self.become_method = ''
            self.become_user = ''
            self.check = False
            self.diff = False
            self.verbosity = 0
            self.module_path = None
            self.listhosts = None
            self.syntax = None
            self.extra_vars = None
            self.inventory = []
            self.passwords = None
            self.ask_vault_pass = None
            self.raw_ssh_args = None
            self.private_

# Generated at 2022-06-13 16:02:23.100015
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    expected_opts = {'debug': True, 'foo': 'bar'}
    opts = CLIArgs(expected_opts)
    assert opts == expected_opts
    assert opts['debug'] is True
    assert opts['foo'] == 'bar'

# Generated at 2022-06-13 16:02:25.888239
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    arguments = {'argument1': 'value1', 'argument2': 'value2'}

    try:
        GlobalCLIArgs(arguments)
    except TypeError:
        pass
    else:
        assert False, 'Expected exception when trying to create object'

# Generated at 2022-06-13 16:02:41.391809
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import GlobalCLIArgs

# Generated at 2022-06-13 16:02:46.042989
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    example_dict = dict()
    example_dict['some_var'] = 1
    example_dict['some_list'] = ["a", "b", "c"]

    obj = CLIArgs(example_dict)
    assert isinstance(obj, ImmutableDict)
    assert obj['some_var'] == 1
    assert obj['some_list'] == ("a", "b", "c")
    assert example_dict['some_list'] == ["a", "b", "c"]

    obj2 = CLIArgs({'some_var': 12, 'some_list': ["x", "y", "z"]})
    assert isinstance(obj2, ImmutableDict)
    assert obj2['some_var'] == 12
    assert obj2['some_list'] == ("x", "y", "z")


# Generated at 2022-06-13 16:02:47.751578
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class AAA(metaclass=_ABCSingleton):
        pass

    class BBB(AAA):
        pass

    class CCC(AAA):
        pass

# Generated at 2022-06-13 16:02:56.412805
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from collections import OrderedDict
    from operator import itemgetter
    from types import MappingProxyType
    import copy

    ans_dict = OrderedDict()
    ans_dict['a1'] = 'a'
    ans_dict['b'] = ImmutableDict({
        'c': 'c',
        'd': 'd',
    })
    ans_dict['e'] = [
        'e',
        MappingProxyType({
            'f': 'f',
            'g': [
                'g',
                'h',
                'i',
            ],
        }),
    ]
    ans_dict['j'] = ('j', 'k', 'l')
    ans_dict['m'] = frozenset(['m', 'n', 'o'])

# Generated at 2022-06-13 16:03:05.110193
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # In the unit test, we use the public API to construct a GlobalCLIArgs object.  This is not
    # how the object will get created in real life.  In real life, GlobalCLIArgs will be
    # automatically created on-the-fly the first time it is accessed.
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--test', action='store_true')
    parser.add_option('--test2', action='store_true')
    (options, args) = parser.parse_args(args=['--test', '--test2'])
    args = CLIArgs.from_options(options)
    GlobalCLIArgs.set(args)
    assert GlobalCLIArgs() == args

# Generated at 2022-06-13 16:03:15.647786
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import ansible.utils.unsafe_proxy

    args = GlobalCLIArgs({'ANSIBLE_REMOTE_TEMP': '/tmp', 'ANSIBLE_CONFIG': 'ansible.cfg'})

    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args, ImmutableDict)
    assert isinstance(args, Mapping)
    assert args['ANSIBLE_REMOTE_TEMP'] == '/tmp'
    assert args['ANSIBLE_CONFIG'] == 'ansible.cfg'

    with pytest.raises(ansible.utils.unsafe_proxy.AnsibleUnsafeText):
        args['ANSIBLE_REMOTE_TEMP'] = '/tmp2'
        assert False, "Should have thrown an exception"


# Generated at 2022-06-13 16:03:24.118376
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options:
        hello = 'world'
        peace = 'love'
        change = [1, 2, 3, 4]
        beatles = {'john': 'guitar',
                   'paul': 'bass',
                   'george': 'lead guitar',
                   'ringo': 'drums',
                   }
        jimi = ('hendrix', 'srv', 'johnny', 'winter')
        foo = {'bar': {'baz': 'quux'}}

    options = Options()

    cli = GlobalCLIArgs.from_options(options)

    assert options.hello == 'world'
    assert options.peace == 'love'
    assert options.change == [1, 2, 3, 4]

# Generated at 2022-06-13 16:03:28.402480
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import unittest
    try:
        # the instantiation must work
        args = GlobalCLIArgs({'foo': 'bar'})
        # assert id of the class instance is the same
        assert id(args) == id(GlobalCLIArgs({'foo': 'bar'}))
        assert id(args) == id(GlobalCLIArgs.instance())
    except:
        raise
    finally:
        os._exit(unittest.main())

# Generated at 2022-06-13 16:03:33.214629
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B, C):
        pass
    a = A()
    b = B()
    d = D()

# Generated at 2022-06-13 16:03:34.053748
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    Test()

# Generated at 2022-06-13 16:03:49.074845
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SubclassOfABCSingleton(_ABCSingleton):
        pass

    class SubclassOfSingleton(Singleton):
        pass

    class SubclassOfABCSingletonAndSingleton(_ABCSingleton, Singleton):
        pass

    assert SubclassOfABCSingleton.__mro__[1] == Singleton
    assert SubclassOfSingleton.__mro__[1] == ABCMeta
    assert SubclassOfABCSingletonAndSingleton.__mro__[1] == Singleton
    assert SubclassOfABCSingletonAndSingleton.__mro__[2] == ABCMeta

# Generated at 2022-06-13 16:03:55.618148
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class RealSingleton(_ABCSingleton):
        pass

    class RealABC(RealSingleton):
        def __init__(self):
            pass

    # When class RealABC is initialized it should also initialize class RealSingleton.
    # This would cause an assertion error if the metaclass
    # generated by _ABCSingleton is not correct.
    RealABC()



# Generated at 2022-06-13 16:03:58.581075
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        a = 'a'

    class B(_ABCSingleton):
        b = 'b'

    assert A.a == B.b



# Generated at 2022-06-13 16:04:06.921190
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'a': 1, 'b':2}
    temp = CLIArgs(args)
    assert isinstance(temp, CLIArgs)

    try:
        temp['c'] = 3
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    assert not temp.keys() == set()
    assert temp.keys() == set(['a', 'b'])

    try:
        temp['a'] = 2
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    assert temp['a'] == 1


# Generated at 2022-06-13 16:04:08.168200
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestingABCSingleton(object):
        __metaclass__ = _ABCSingleton

# Generated at 2022-06-13 16:04:16.094391
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs(
        {
            'connection': 'network_cli',
            'module_path': '/path/to/module.py',
            'module_args': '{"host": "localhost", "username": "foo", "password": "bar", "use_ssl": True}',
            'become': False,
            'become_method': 'enable',
            'become_user': 'root',
            'verbosity': 1,
            'check': True,
            'diff': True,
            'debug': True,
        }
    )

# Generated at 2022-06-13 16:04:22.462921
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test success case
    mapping = {'toplevel1': 1, 'toplevel2': [1, 2, 3], 'toplevel3': {'sub1': ['sub1sub1', 'sub1sub2'], 'sub2': {'sub2sub1': 'sub2sub1sub1'}}}
    cli_args = CLIArgs(mapping)
    assert cli_args['toplevel1'] == 1
    assert cli_args['toplevel2'] == (1, 2, 3)
    assert cli_args['toplevel3'] == ImmutableDict({'sub1': ('sub1sub1', 'sub1sub2'), 'sub2': ImmutableDict({'sub2sub1': 'sub2sub1sub1'})})

# test singleton constructor

# Generated at 2022-06-13 16:04:32.454688
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cliargs = CLIArgs({'a': {'b': [1, 2, 3, {'c': ['a', 'b', 'c']}, 'd', 'e']}})
    assert isinstance(cliargs, ImmutableDict)
    assert isinstance(cliargs['a'], ImmutableDict)
    assert isinstance(cliargs['a']['b'], tuple)
    assert isinstance(cliargs['a']['b'][0], int)
    assert isinstance(cliargs['a']['b'][3], ImmutableDict)
    assert isinstance(cliargs['a']['b'][3]['c'], tuple)
    for index, value in enumerate(cliargs['a']['b'][3]['c']):
        assert isinstance(value, text_type)


# Generated at 2022-06-13 16:04:41.620359
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class options:
        check = False
        diff = False
        force_handlers = False
        flush_cache = False
        help = False
        host_key_checking = True
        inventory = '/home/ansible/ansible/dev/hosts'
        listhosts = False
        syntax = False
        module_path = None
        subset = None
        vault_password_file = None
        verbosity = 0
        version = False
        start_at_task = None
        step = False
        tags = None
        skip_tags = None
        one_line = False
        tree = None
        ask_sudo_pass = False
        ask_su_pass = False
        ask_vault_pass = False
        vault_password_files = None
        connection = 'smart'
        remote_user = None
        private_key

# Generated at 2022-06-13 16:04:53.249259
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Generate an immutable copy of a sample
    sample_mapping = {
        'one': 'some value',
        'two': {
            'some': 'other value',
            'complex': {
                'structure': 'with a long value'
            }
        }
    }
    sample_args = CLIArgs(sample_mapping)
    assert isinstance(sample_args, CLIArgs)
    assert isinstance(sample_args, ImmutableDict)
    # Check that it's deep copy is also immutable
    assert isinstance(sample_args['two'], ImmutableDict)
    assert isinstance(sample_args['two']['complex'], ImmutableDict)
    # Check that we have the expected values
    assert sample_args['one'] == sample_mapping['one']
    assert sample_args['two']

# Generated at 2022-06-13 16:05:13.623529
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        'foo': 'Foo',
        'bar': 'Bar',
        'baz': [1, 2, {'three': 'Three', 'four': 'Four'}],
        'quux': {'a': 'A', 'b': 'B'},
        'bazinga': ('one', ('two', ('three', 'four')), 'five')
    }
    mutable_dict = ImmutableDict(test_dict)
    immutable_dict = CLIArgs(test_dict)
    assert mutable_dict == immutable_dict
    assert isinstance(immutable_dict, Mapping)
    assert isinstance(immutable_dict, CLIArgs)
    assert isinstance(immutable_dict, GlobalCLIArgs)
    assert immutable_dict.foo == 'Foo'

# Generated at 2022-06-13 16:05:18.357127
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        def __init__(self, value):
            self.value = value

    class B(A):
        pass

    class C(A):
        pass

    assert A('a') is A('a')
    assert B('a') is A('a')
    assert C('a') is A('a')

    assert issubclass(B, A)
    assert issubclass(C, A)

# Generated at 2022-06-13 16:05:19.312727
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass

# Generated at 2022-06-13 16:05:29.246050
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyMetaclass(object):
        """Plain old type to use as a metaclass"""
        pass

    # Make sure this class doesn't cause infinite recursion in __mro__ determination
    class MySingleton(_ABCSingleton, metaclass=MyMetaclass):
        """A class that uses _ABCSingleton as a metaclass when MyMetaclass is used as a metaclass"""
        pass

    class MyClass(MySingleton):
        """
        A class that uses _ABCSingleton as a metaclass when MyMetaclass is used as a metaclass
        and is not an abstract class
        """
        pass


# Generated at 2022-06-13 16:05:31.807385
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert isinstance(_ABCSingleton("test", (), {}), Singleton)
    assert issubclass(_ABCSingleton("test", (), {}), ABCMeta)

# Generated at 2022-06-13 16:05:39.372720
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'alpha': {'beta': 'gamma'}, 'delta': ['echo', 'foxtrot']})
    alpha = args['alpha']
    assert(isinstance(alpha, ImmutableDict))
    beta = alpha['beta']
    assert(isinstance(beta, text_type))
    delta = args['delta']
    assert(delta[0] == 'echo')
    assert(isinstance(delta, tuple))

    with pytest.raises(TypeError):
        args['bravo'] = 'charlie'



# Generated at 2022-06-13 16:05:46.692783
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.constants import DEFAULT_KEEP_REMOTE_FILES
    from ansible.module_utils.common.argparse_utils import parser

    options, args = parser.parse_known_args(['--keep-remote-files', '--module-name', 'Foo'])

    # Make sure that it is a singleton
    args1 = GlobalCLIArgs.from_options(options)
    args2 = GlobalCLIArgs.from_options(options)
    assert args1 is args2

    # Make sure that it raises TypeError if we try to instantiate it directly
    with pytest.raises(TypeError):
        args3 = GlobalCLIArgs()

    # Make sure that it works as expected

# Generated at 2022-06-13 16:05:52.164322
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(Singleton):
        pass

    class B:
        pass

    a = A()

    try:
        B.__metaclass__ = _ABCSingleton
        b = B()
        assert a is b
    except TypeError:
        # Correct behaviour is that the combination of ABCMeta and Singleton would prevent
        # multiple instantiation because B is not an instance of ABCMeta
        pass

    class C(metaclass=_ABCSingleton):
        pass

    c = C()

    try:
        d = C()
        assert c is d
    except TypeError:
        # Correct behaviour is that when the metaclass is inherited and not assigned to the
        # existing class, the instantiation would fail because of the Singleton
        pass

    class D(metaclass=_ABCSingleton):
        pass


# Generated at 2022-06-13 16:06:03.219332
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test CLIArgs class to ensure constructor takes data and makes it immutable
    """
    temp = {
        'str_key': 'str_value',
        'int_key': 1,
        'dict_key': {'nested_str_key': 'nested_str_value', 'list_key': [1, 2, 3]},
        'list_key': [1, 2, 3, {'nested_str_key': 'nested_str_value', 'list_key': [1, 2, 3]}],
        'tuple_key': (1, 2, 3, 'tuple_value', {'nested_str_key': 'nested_str_value', 'list_key': [1, 2, 3]}),
    }
    obj = CLIArgs(temp)

# Generated at 2022-06-13 16:06:06.091806
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    c = CLIArgs({'a': 1, 'b': 2})
    assert c['a'] == 1 and c['b'] == 2

# Generated at 2022-06-13 16:06:25.544343
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test constructor of class CLIArgs
    """
    options = _make_immutable(dict(name='test_CLIArgs'))
    test_CliArgs = CLIArgs.from_options(options)
    assert isinstance(test_CliArgs, CLIArgs)

# Generated at 2022-06-13 16:06:34.400781
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    toplevel = {'level1':
                    {'level2':
                         [{'level3': 'value1'}, {'level4': 'value2'}],
                     'level2b': 'value3'}}
    args = CLIArgs(toplevel)
    assert isinstance(args, dict)
    assert isinstance(args, Mapping)
    assert isinstance(args.get('level1'), ImmutableDict)
    assert isinstance(args.get('level1').get('level2'), tuple)
    assert isinstance(args.get('level1').get('level2b'), str)
    assert isinstance(args.get('level1').get('level2')[0], ImmutableDict)
    assert isinstance(args.get('level1').get('level2')[0].get('level3'), str)


# Generated at 2022-06-13 16:06:43.733632
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    mutation_test_dict = {"first_key": "string_test",
                          "second_key": {"key_a": "string_test", "key_b": "string_test"},
                          "third_key": ["string_test", {"key_a": "string_test", "key_b": "string_test"}]}
    # We expect that passing mutation_test_dict to GlobalCLIArgs will not mutate mutation_test_dict.
    GlobalCLIArgs(mutation_test_dict)

# Generated at 2022-06-13 16:06:54.838429
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        class SingletonSubclass(_ABCSingleton):
            pass
    except TypeError:
        assert False, '_ABCSingleton unit test 1 failed'

    try:
        class Subclass(_ABCSingleton):
            pass
    except TypeError:
        assert False, '_ABCSingleton unit test 2 failed'

    try:
        class SingletonSubclass(_ABCSingleton, Mapping):
            pass
    except TypeError:
        assert False, '_ABCSingleton unit test 3 failed'

    try:
        class Subclass(_ABCSingleton, Mapping):
            pass
    except TypeError:
        assert False, '_ABCSingleton unit test 4 failed'

    try:
        class Subclass(_ABCSingleton):
            pass
    except TypeError:
        assert False, '_ABCSingleton unit test 5 failed'

# Generated at 2022-06-13 16:06:58.402122
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test that _ABCSingleton is combination of Singleton and ABCMeta
    """
    class MyClass(_ABCSingleton):  # pylint: disable=no-init
        pass
    obj1 = MyClass()
    obj2 = MyClass()
    assert obj1 is obj2

# Generated at 2022-06-13 16:07:05.432553
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest.mock
    import argparse

    args = argparse.Namespace(connection='network_cli', module_path='./library')

    with unittest.mock.patch('argparse.ArgumentParser.parse_args', return_value=args):
        options = GlobalCLIArgs.from_options(args)

    assert options.connection == 'network_cli'
    assert options.module_path == './library'

# Generated at 2022-06-13 16:07:12.177460
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Test _ABCSingleton by making two metaclasses and making sure it raises a TypeError"""
    class _TestMeta(_ABCSingleton): pass
    class _TestBase(object): __metaclass__=_TestMeta

    class _TestMeta2(_ABCSingleton): pass
    class _TestBase2(_TestBase, metaclass=_TestMeta2): pass

    assert issubclass(_TestMeta2, _TestMeta)
    assert issubclass(_TestMeta2, _ABCSingleton)
    assert issubclass(_TestMeta, _ABCSingleton)

# Generated at 2022-06-13 16:07:22.034851
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli.arguments import Options
    options = Options()
    options.version = 2

    # Singleton should have been created by now
    global_cli_args = GlobalCLIArgs._get_instance()
    assert global_cli_args['version'] == 2
    # Test that the GlobalCLIArgs class is a singleton
    assert global_cli_args == GlobalCLIArgs._get_instance()

    # Test that CLIArgs is working correctly
    options.version = 3
    options.connection = 'foo'
    cli_args = CLIArgs.from_options(options)
    assert cli_args['version'] == 3
    assert cli_args['connection'] == 'foo'

# Generated at 2022-06-13 16:07:26.998165
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestMetaClass(_ABCSingleton):
        pass

    # The set of instance attributes defined by a class definition is determined by inspecting the
    # list of class attributes and their types. The same is true for the list of instance methods.
    # Instance attributes are defined by assigning to the class rather than to self in any class
    # method with the exception of __init__.
    class _TestSingletonClass(metaclass=_TestMetaClass):
        pass

    # it should be a singleton
    assert _TestSingletonClass() is _TestSingletonClass()

# Generated at 2022-06-13 16:07:29.621042
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = CLIArgs({'a': 1, 'b': {'c': 2}})
    assert args['a'] == 1
    assert args['b']['c'] == 2

# Generated at 2022-06-13 16:08:02.412147
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(_ABCSingleton, Singleton)
    assert issubclass(_ABCSingleton, ABCMeta)

# Generated at 2022-06-13 16:08:08.938908
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    c = CLIArgs(dict(a=1, b=dict(c=2), d=[1,2,3], e={'x':2, 'y':3}))
    assert isinstance(c, Mapping)
    assert isinstance(c, ImmutableDict)
    assert not isinstance(c, CLIArgs)
    assert isinstance(c, Container)
    assert isinstance(c['b'], ImmutableDict)
    assert isinstance(c['d'], Sequence)
    assert isinstance(c['e'], ImmutableDict)
    assert isinstance(c['e'], Container)

# Generated at 2022-06-13 16:08:14.029830
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    cli_args = parser.parse_args([])
    global_cli_args = GlobalCLIArgs.from_options(cli_args)
    print(global_cli_args)


# Generated at 2022-06-13 16:08:15.289478
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert hasattr(GlobalCLIArgs, '__metaclass__')

# Generated at 2022-06-13 16:08:21.103094
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        pass
    class B(_ABCSingleton):
        pass
    class C(A, B):
        pass
    assert A.__mro__[1] is ABCMeta
    assert B.__mro__[1] is ABCMeta
    assert C.__mro__[1] is ABCMeta
    assert C.__mro__[2] is A
    assert C.__mro__[3] is B


# Generated at 2022-06-13 16:08:23.245203
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass1(object, metaclass=_ABCSingleton):
        pass
    test1 = TestClass1()
    test2 = TestClass1()
    assert test1 == test2

# Generated at 2022-06-13 16:08:28.476325
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    base_args = dict()
    base_args["user"] = "root"
    base_args["password"] = "123456"
    base_args["host"] = "192.168.99.100"
    base_args["port"] = "22"
    args = CLIArgs(base_args)
    assert args["user"] == "root"
    assert args["password"] == "123456"
    assert args["host"] == "192.168.99.100"
    assert args["port"] == "22"
    base_args["user"] = "ansible"
    assert args["user"] != "ansible"

# Generated at 2022-06-13 16:08:36.822272
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import ansible

# Generated at 2022-06-13 16:08:46.585064
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.utils.sentinel import Sentinel

    display = Display()
    options = Sentinel()
    options.verbosity = 0
    options.debug = False
    options.action_plugins = []
    options.cache_plugins = []
    options.callback_plugins = []
    options.connection_plugins = []
    options.lookup_plugins = []
    options.filter_plugins = []
    options.test_plugins = []
    options.strategy_plugins = []
    options.vars_plugins = []
    options.terminal_plugins = []
    options.display = display
    options.ask_vault_pass = None
    options.vault_password_files = []
    options.new_vault_password_file = None
    options.output_file = None
   

# Generated at 2022-06-13 16:08:57.533088
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Unit test for class GlobalCLIArgs

    Unit test for both class GlobalCLIArgs and its superclass, CLIArgs.

    Make sure that the contents of the GlobalCLIArgs object are immutable, even if its contents are
    modified by the user.
    """
    # Create a GlobalCLIArgs object
    cli_args = GlobalCLIArgs({'flag': True})

    # Check its internal state
    assert cli_args == ImmutableDict({'flag': True})

    # Make sure we can't accidentally mutate the object when we are just trying to get at its
    # contents
    try:
        cli_args['flag'] = False
    except TypeError:
        pass
    else:
        assert False, 'GlobalCLIArgs object can be mutated'

