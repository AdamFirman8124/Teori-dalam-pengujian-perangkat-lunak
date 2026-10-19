

# Generated at 2022-06-13 15:59:39.613297
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TempABCMeta(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    t = TempABCMeta()
    assert isinstance(t, TempABCMeta)
    s = TempABCMeta()
    assert t is s
    assert t == s

# Generated at 2022-06-13 15:59:45.962556
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 15:59:54.852291
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import ansible.module_utils.common.utils as utils
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import ImmutableDict

    cli = [
        'ansible',
        '-m', 'example',
        'host',
        '-a', 'arg1=value1',
        '-b',
        '-c', 'arg2=value2',
        '-e', '{"arg3": "value3"}',
    ]
    opts = utils._parse_cli_args(cli)

    cli_args = CLIArgs.from_options(opts)

    assert isinstance(cli_args, Mapping)
    assert isinstance(cli_args, ImmutableDict)

    assert cli_args

# Generated at 2022-06-13 15:59:58.436984
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # pylint: disable=unused-variable
    class test1(object):
        """
        This is an example class which is not an abstract base class.
        """
        __metaclass__ = _ABCSingleton
    # pylint: enable=unused-variable

# Generated at 2022-06-13 16:00:04.913255
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    names = 'name', 'names', 'name_list'

    for name in names:
        for key, value in dict(
            dict=dict(a=1, b=2),
            list=list(range(10)),
            set=set(range(10)),
            tuple=tuple(range(10)),
            text=text_type('Hello, world!'),
            binary=binary_type('Hello, world!'),
        ).items():
            mapping = {name: {key: value}}
            cliargs = CLIArgs(mapping)
            assert cliargs[name][key] == value
            assert cliargs == mapping

# Generated at 2022-06-13 16:00:09.176712
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_args = CLIArgs({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}, 'f': frozenset([1, 2]), 'g': (1, 2, 3)})
    assert isinstance(cli_args, CLIArgs)
    assert cli_args['c']['d'] == 3


# Generated at 2022-06-13 16:00:11.298631
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs.__new__(GlobalCLIArgs)


# Cleanup our namespace
del _ABCSingleton
del _make_immutable

# Generated at 2022-06-13 16:00:15.154002
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # check if constructor throws error for invalid  argument
    try:
        GlobalCLIArgs.from_options(None)
        assert(False)
    except TypeError:
        pass



# Generated at 2022-06-13 16:00:17.547469
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'a': {'b': {'c': 'd'}}})
    assert args['a']['b']['c'] == 'd'

# Generated at 2022-06-13 16:00:21.922094
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Testing class created by combining two metaclasses"""
    class TestClass(object):
        """Test class for _ABCSingleton"""
        __metaclass__ = _ABCSingleton
        pass
    TestClass1 = TestClass()
    TestClass2 = TestClass()
    assert TestClass1 is TestClass2
    # should be a Singleton
    assert TestClass1 is TestClass()

# Generated at 2022-06-13 16:00:29.562141
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs.instances().clear()
    result = GlobalCLIArgs({'a': 1})
    assert isinstance(result, ImmutableDict)
    assert result['a'] == 1
    try:
        result['a'] = 3
    except (KeyError, TypeError):
        pass
    else:
        assert False

    # Should only be one instance now
    assert len(GlobalCLIArgs.instances()) == 1



# Generated at 2022-06-13 16:00:38.380373
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # tuple_to_check = (('inventory', ['/root/inventory/hosts.yml']),('connection', ['local']))
    tuple_to_check = (('inventory', set(['/root/inventory/hosts.yml'])), ('connection', 'local'))
    mapping = {}
    for key, value in tuple_to_check:
        mapping[key] = _make_immutable(value)
    args = GlobalCLIArgs(mapping)
    assert len(args) == 2
    assert args['inventory'] == '/root/inventory/hosts.yml'

# Generated at 2022-06-13 16:00:41.405983
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class __ABCSingletonTester(object):
        __metaclass__ = _ABCSingleton
    assert _ABCSingleton(__ABCSingletonTester.__name__, (), {}) is _ABCSingleton(__ABCSingletonTester.__name__, (), {})


# Generated at 2022-06-13 16:00:45.704708
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    x = CLIArgs({'foo': 'bar'})
    y = CLIArgs({'foo': 'bar', 'baz': None})
    assert x == {'foo': 'bar'}
    assert y == {'foo': 'bar', 'baz': None}
    assert not x == {'foo': 'bar', 'baz': None}
    assert not y == {'foo': 'bar'}

# Generated at 2022-06-13 16:00:55.613370
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=protected-access
    from ansible.module_utils.common.collections import is_immutable
    from ansible.module_utils.basic import AnsibleModule
    from ansible.cli import CLI

    cli = CLI(args='-h --foo=1 --bar=2 -vvvv -m fake_module -a foo=bar'.split(' '))
    options = cli.parse()

    args = GlobalCLIArgs.from_options(options)

    assert args.check_mode is False
    assert args.verbosity == 4

    module = AnsibleModule(argument_spec={})
    assert is_immutable(module)

# Generated at 2022-06-13 16:01:05.692479
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    def check_reference(ref, test):
        #print("mapping: ", ref, test)
        for key, value in ref.items():
            assert key in test
            assert value is test[key]

    import unittest

    class MyTestCase(unittest.TestCase):

        def test_lists(self):
            test_ref = {'key1': ['value1', 'value2'], 'key2': ['value3', 'value4']}
            test = CLIArgs(test_ref)
            check_reference(test_ref, test)

        def test_nested_lists(self):
            test_ref = {'key1': ['value1', ['value2', 'value3'], 'value4'], 'key2': 'value5'}
            test = CLIArgs(test_ref)
            check_

# Generated at 2022-06-13 16:01:10.863446
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    a = CLIArgs({'one': 'two', 'three': 'four'})
    assert a == {'one': 'two', 'three': 'four'}
    assert a.one == 'two'
    assert a.three == 'four'
    assert isinstance(a, ImmutableDict)

# Generated at 2022-06-13 16:01:13.076040
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # When called more than once, do not create a new instance.
    GlobalCLIArgs()
    g1 = GlobalCLIArgs()
    g2 = GlobalCLIArgs()
    assert g1 == g2

# Generated at 2022-06-13 16:01:17.408135
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test for CLIArgs object"""
    args = CLIArgs({"one": [1, 2, 3], "two": {"three": "four"}})

    assert args.get("one") == (1, 2, 3)
    assert args.get("two") == ImmutableDict({"three": "four"})
    assert args.get("one") == (1, 2, 3)



# Generated at 2022-06-13 16:01:18.145756
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    _ABCSingleton()



# Generated at 2022-06-13 16:01:21.039411
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    assert Foo() is Foo.instance()

# Generated at 2022-06-13 16:01:23.715433
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert A() is A()

# Generated at 2022-06-13 16:01:25.563844
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    arguments = {"foo": "bar"}

    args = GlobalCLIArgs(arguments)

    assert args.args == arguments

# Generated at 2022-06-13 16:01:29.951658
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class myclass(object):
        __metaclass__ = _ABCSingleton

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

    instance1 = myclass(1)
    instance2 = myclass(2)
    # ensure that the instances are the same
    assert instance1 is instance2

# Generated at 2022-06-13 16:01:36.395021
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    test_input = {"test_item": "test_value"}
    test_input_immutable = {"test_item": "test_value"}
    res = GlobalCLIArgs(test_input)
    assert res == test_input_immutable
    assert res.__dict__ == test_input
    assert vars(res) == test_input
    res = GlobalCLIArgs.from_options(GlobalCLIArgs(test_input))
    assert res == test_input_immutable
    assert res.__dict__ == test_input
    assert vars(res) == test_input
    if not isinstance(res, GlobalCLIArgs):
        raise RuntimeError("GlobalCLIArgs class is not a singleton.")

# Generated at 2022-06-13 16:01:46.814712
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class AnsibleOptions(object):
        def __init__(self, list_options):
            for option in list_options:
                setattr(self, option[0], option[1])

    options = AnsibleOptions([('foo', 'bar'), ('baz', 'qux')])
    cli_args = CLIArgs.from_options(options)

    assert(cli_args['foo'] == 'bar')
    assert(cli_args['baz'] == 'qux')

    try:
        cli_args['foo'] = 'changed'
        assert(False)
    except Exception:
        pass

    try:
        cli_args['foobar'] = 'changed'
        assert(False)
    except Exception:
        pass



# Generated at 2022-06-13 16:01:51.126009
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Make sure that our class can be instantiated"""
    class Temp(object):
        __metaclass__ = _ABCSingleton

    try:
        tmp = Temp()
    except TypeError:
        assert False, "Unable to instantiate instance of _ABCSingleton"
    else:
        assert True

# Generated at 2022-06-13 16:02:00.951691
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_loader_dl import AnsibleCollectionLoaderDl
    from ansible.utils.collection_loader_dir import AnsibleCollectionLoaderDir
    assert GlobalCLIArgs.instance() is GlobalCLIArgs()
    GlobalCLIArgs.instance().__init__(dict(foo='bar'))
    assert GlobalCLIArgs.read('foo') == 'bar'
    assert GlobalCLIArgs()['foo'] == 'bar'
    GlobalCLIArgs.reset()
    assert GlobalCLIArgs.read('foo') is None
    assert GlobalCLIArgs()['foo'] is None
    GlobalCLIArgs.instance().__init__(dict(erase_collections='never'))

# Generated at 2022-06-13 16:02:04.406100
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass
    assert isinstance(A(), A)

    class B(A):
        pass
    assert isinstance(B(), B)

    class C(metaclass=_ABCSingleton):
        pass
    assert isinstance(C(), C)


# Generated at 2022-06-13 16:02:07.682318
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = dict(one=1, two=2, three=3, four=4)
    test_CLIArgs_obj = CLIArgs(test_dict)
    assert test_CLIArgs_obj == test_dict
    assert isinstance(test_CLIArgs_obj, ImmutableDict)

# Generated at 2022-06-13 16:02:12.353349
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class testA(object):
        __metaclass__ = _ABCSingleton
    class testB(object):
        __metaclass__ = _ABCSingleton
    assert testA() == testB()

# Generated at 2022-06-13 16:02:15.752917
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Bar(object):
        __metaclass__ = _ABCSingleton

    class Foo(Bar):
        pass

    class Foobar(Foo):
        pass

    assert issubclass(Foo, Bar)
    assert issubclass(Foobar, Foo)
    assert issubclass(Foobar, Bar)

# Generated at 2022-06-13 16:02:22.775121
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections

    argdict = {'a': [1, 2, 3], 'b': 'foo', 'c': ['bar', 'baz']}
    options = collections.namedtuple('options', argdict.keys())(*argdict.values())
    test_obj = GlobalCLIArgs.from_options(options)

    # confirm all types are immutable
    assert isinstance(test_obj, ImmutableDict)
    assert not isinstance(test_obj, Mapping)
    assert isinstance(test_obj['a'], tuple)
    assert not isinstance(test_obj['a'], Sequence)
    assert isinstance(test_obj['c'], tuple)
    assert not isinstance(test_obj['c'], Sequence)

    # confirm data matches what we asked for

# Generated at 2022-06-13 16:02:25.243050
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(A):
        pass
    assert hash(A()) == hash(A())
    assert hash(B()) == hash(B())

# Generated at 2022-06-13 16:02:28.525351
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object): pass
    options = Options()
    options.one = 1
    options.two = 2
    options.three = 3
    option_args = vars(options)
    obj = GlobalCLIArgs(option_args)
    assert obj.get('one') == 1
    assert obj.get('two') == 2
    assert obj.get('three') == 3

# Generated at 2022-06-13 16:02:29.836130
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(object):
        __metaclass__ = _ABCSingleton

    assert X() is X()
    assert issubclass(X, ABCMeta)

# Generated at 2022-06-13 16:02:32.685910
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(metaclass=_ABCSingleton):
        pass

    x = Foo()
    y = Foo()
    assert x is y

# Generated at 2022-06-13 16:02:43.389531
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest

    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.plugin_docs import get_docstring
    from ansible.utils.display import Display
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.json_utils import AnsibleJSONEncoder
    from ansible.module_utils.common.json_utils import AnsibleJSONDecoder

    valid_args = [
        'cat',
        'cowsay',
        'user',
    ]

    # Arguments that need to be passed to the module in order to be tested
    module_args = {
        'foo': 'bar',
        'this': 'that',
    }
    module_args = ImmutableDict(module_args)


# Generated at 2022-06-13 16:02:52.147539
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test with an empty object
    test_dict = {}
    cliargs = CLIArgs(test_dict)
    assert cliargs == {}
    # Test with an object with data
    test_dict = {'test': 1, 'string': 'test'}
    cliargs = CLIArgs(test_dict)
    assert 'test' in cliargs
    assert cliargs['test'] == 1
    assert 'string' in cliargs
    assert cliargs['string'] == "test"


# Generated at 2022-06-13 16:02:59.948398
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():  # pylint: disable=missing-docstring
    import collections
    test_dict = {
        'dict': {
            'subdict': {'subsubdict': 'subsubdict-value'},
            'sublist': ['sublist-value'],
            'subpair': ('subpair-value',),
        },
        'list': ['list-value'],
        'pair': ('pair-value',),
        'value': 'value',
    }

# Generated at 2022-06-13 16:03:08.444685
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    options = dict(one=1, two=2, three=3)
    ca = CLIArgs(options)
    assert ca == ImmutableDict(options)

    options['one'] = 'one'
    options['two'] = ['two', 'deux', 'dos']
    options['three'] = {'three': 'trois', 'four': 4}
    ca = CLIArgs(options)
    assert ca == ImmutableDict(one='one', two=tuple(['two', 'deux', 'dos']), three=ImmutableDict(three='trois', four=4))

    options['one'] = ImmutableDict(ok='ok', one=1)
    options['two'] = (tuple(['two', 'deux', 'dos']), {'three': 'trois', 'four': 4})

# Generated at 2022-06-13 16:03:17.861450
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import json
    import types
    import test.support

    # list of dicts to be used to test instantiation of CLIArgs
    cli_args_list = [
        [{'foo': 1, 'bar': 2}],
        [{'foo': [1, 2, 3], 'bar': (1, 2, 3)}],
        [{'foo': {"key": "value"}, 'bar': {"key": "value"}}],
        [{'foo': 1, 'bar': 2}, {'foo': [1, 2, 3], 'bar': (1, 2, 3)}],
        [{'foo': {"key": "value"}, 'bar': {"key": "value"}}, {'foo': 1, 'bar': 2}]
        ]

    for cli_args in cli_args_list:
        cli_args

# Generated at 2022-06-13 16:03:27.202741
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test the constructor of class CLIArgs
    """
    # Test one dict level
    a = CLIArgs({'key': 'value'})
    assert a['key'] == 'value'
    assert a.key == 'value'
    # Test two dict levels
    b = CLIArgs({'key': {'dict1': 'value1', 'dict2': 'value2'}})
    assert b['key']['dict1'] == 'value1'
    assert b.key.dict1 == 'value1'
    assert b['key']['dict2'] == 'value2'
    assert b.key.dict2 == 'value2'
    # Test list level
    c = CLIArgs({'lists': ['item1', 'item2', 3, 4]})
    assert c['lists'][0] == 'item1'


# Generated at 2022-06-13 16:03:30.201018
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    class Test2(Test, object):
        pass

    Test()
    Test2()

# Generated at 2022-06-13 16:03:34.141031
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test CLIArgs construction
    """
    data = {"foo": "bar"}
    cli_args = CLIArgs(data)
    assert cli_args["foo"] == "bar"



# Generated at 2022-06-13 16:03:35.709866
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    instance = GlobalCLIArgs()
    assert instance is not None


# Generated at 2022-06-13 16:03:44.074120
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Test(object):
        def __init__(self, x):
            self.x = x

    args = CLIArgs(dict(
        blah='blah',
        test=Test(5),
        test2=[Test(10), Test(20)],
        stuff=[1, 2, 3],
        test3={'key1': 'blah1', 'key2': 'blah2', 'key3': [1, 2, 3]}
    ))

    assert args['blah'] == 'blah'
    assert args['test'].x == 5
    assert args['stuff'] == (1, 2, 3)
    assert list(args['test2'])[0].x == 10
    assert list(args['test2'])[1].x == 20

# Generated at 2022-06-13 16:03:52.439688
# Unit test for constructor of class _ABCSingleton

# Generated at 2022-06-13 16:03:59.292022
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """ Test the _ABCSingleton metaclass """

    class Foo(object):
        """
        A class to test __ABCSingleton__
        """
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    foo = Foo()
    assert foo == Foo()
    assert id(foo) == id(Foo())
    assert isinstance(foo, ABCMeta)
    assert isinstance(foo, Singleton)



# Generated at 2022-06-13 16:03:59.939628
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:04:04.025459
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    
    class SingletonTest(metaclass=_ABCSingleton):
        pass

    assert SingletonTest() is SingletonTest()

# Generated at 2022-06-13 16:04:09.014133
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs.from_options(ImmutableDict({"foo": "bar"}))
    assert args == {"foo": "bar"}
    with pytest.raises(TypeError) as error:
        args["foo"] = "baz"
    assert "is immutable" in str(error)
    assert "is immutable" not in str(args)
    assert "is immutable" in "{0}".format(args)


# Generated at 2022-06-13 16:04:21.232432
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Create a sample class for testing
    class SampleArgs(object):
        def __init__(self, value):
            self.value = value

    # Create a sample of the types we expect
    args = {
        'one': 'val',
        'two': [
            'sorted',
            'set',
            'list',
        ]
    }

    # Create a sample class
    args['sample'] = SampleArgs('testing')

    # Create a second sample class
    args['sample2'] = SampleArgs('testing2')

    # Create a sample class which is in a list
    args['sample_list'] = [
        SampleArgs('testing_list')
    ]

    # Create a sample class which is in a dictionary
    args['sample_dict'] = {
        'test': SampleArgs('testing_dict')
    }



# Generated at 2022-06-13 16:04:25.174749
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass
    class B(A):
        pass
    class C(A):
        pass

    class D(A):
        pass

    class E(metaclass=_ABCSingleton):
        pass

# Generated at 2022-06-13 16:04:34.493746
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert A() is A()
    assert isinstance(A(), A)
    assert isinstance(A(), object)
    assert isinstance(A(), _ABCSingleton)
    assert not isinstance(A(), type)
    assert isinstance(A, type)
    assert not isinstance(A, _ABCSingleton)

# These unit tests make sure that every thing which _make_immutable() is given returns an immutable
# equivalent.  This is a whitebox test, meaning it is based on the internals of _make_immutable().
# The test should be changed if that function is altered.

# Generated at 2022-06-13 16:04:43.228996
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli.doc import DocCLI
    from ansible.cli.galaxy import GalaxyCLI
    from ansible.cli.playbook import PlaybookCLI
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    doc_cli = DocCLI(['--module-path', '.'])
    doc_parser = doc_cli.get_base_parser(['--help'])
    doc_options = doc_cli.parse(doc_parser)

    galaxy_cli = GalaxyCLI(['--module-path', '.'])
    galaxy_parser = galaxy_cli.get_base_parser(['--help'])
    galaxy_options = galaxy_cli.parse(galaxy_parser)

    playbook_cli = PlaybookCLI

# Generated at 2022-06-13 16:04:47.887423
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(metaclass=_ABCSingleton):
        pass

    assert isinstance(A(), A)
    assert isinstance(B(), B)
    assert not isinstance(A(), B)

# Generated at 2022-06-13 16:04:53.310672
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    kwargs = {'foo': None, 'bar': dict(zip(range(10), range(10))), 'baz': set([text_type(i) for i in range(20)])}
    args = GlobalCLIArgs(kwargs)

    for k, v in kwargs.items():
        assert args[k] == v

# Generated at 2022-06-13 16:05:04.770534
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        "test_key": "value",
        "test_key2": {"test_key3": "test_value3", "test_key4": "test_value4"},
        "test_key5": ["test_value5", "test_value6", "test_value7"]
    }

    # Make sure you get a CLIArgs object back
    result = CLIArgs(test_dict)
    assert isinstance(result, CLIArgs)

    # Make sure keys are the same, ignoring case
    assert set(result) == set(test_dict)

    # Make sure values are the same
    for key in result:
        assert result[key] == test_dict[key]

    # Make sure the class is immutable

# Generated at 2022-06-13 16:05:08.007716
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass1(object):
        __metaclass__ = _ABCSingleton
    class TestClass2(object):
        __metaclass__ = _ABCSingleton

    test1 = TestClass1()
    test2 = TestClass2()

# Generated at 2022-06-13 16:05:17.184814
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(ImmutableDict):
        __metaclass__ = _ABCSingleton

    assert isinstance(_ABCSingletonTest(), _ABCSingletonTest)
    assert isinstance(_ABCSingletonTest(), Singleton)
    assert isinstance(_ABCSingletonTest(), ImmutableDict)

# Generated at 2022-06-13 16:05:19.075794
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    with pytest.raises(AssertionError):
        GlobalCLIArgs(None)

# Generated at 2022-06-13 16:05:21.442145
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca = GlobalCLIArgs({1: 'a', 2: 'b'})

# Generated at 2022-06-13 16:05:26.293465
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    '''
    Test the GlobalCLIArgs class by creating two instances and comparing
    the memory locations to see if they are identical
    '''
    global_cli_args = GlobalCLIArgs({'foo': 'bar'})
    global_cli_args1 = GlobalCLIArgs({'foo': 'bar'})
    assert global_cli_args is global_cli_args1

# Generated at 2022-06-13 16:05:37.686387
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Ensure that the CLIArgs constructor works the way we expect it to

    We want to make sure that the CLIArgs constructor converts it's incoming data into the format
    that we expect.  We have specific needs for this type of data to be able to use it throughout
    the code with ease.
    """
    # Make some test data to use
    test_data = {
        'one': 1,
        'two': 2,
        'three': [1, 2, 3],
        'four': {
            'a': 'b',
            'c': 'd',
        },
    }
    # Make a CLIArgs type object and store the original test data in it
    cli_args = CLIArgs(test_data)
    # Check that all the original keys still exist
    for key in test_data:
        assert key in cli_

# Generated at 2022-06-13 16:05:45.609780
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({
        'key1': 'value1',
        'key2': 'value2',
        'key3': [
            {
                'key4': ('value4_1', 'value4_2', 'value4_3'),
                'key5': {
                    'key6': 'value6'
                },
                'key7': 'value7'
            },
            {
                'key8': 'value8',
                'key5': {
                    'key9': 'value9'
                }
            }
        ]
    })
    assert isinstance(args, Mapping)
    assert isinstance(args['key3'], Sequence)
    assert isinstance(args['key3'][0], Mapping)
    assert isinstance(args['key3'][1], Mapping)
    assert isinstance

# Generated at 2022-06-13 16:05:51.262666
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.shlex import shlex_split
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    # Make sure that custom vars work
    current_vars = combine_vars(loader=DataLoader(), variables=dict(a=1, b=2, c=3))
    current_vars.extra_vars = dict(d=4, c=5, e=6)
    cli_args = CLIArgs.from_options(current_vars)
    assert cli_args['a'] == 1
    assert cli_args['b'] == 2
    assert cli_args['c'] == 5
    assert cli_args['d'] == 4
    assert cli_args['e'] == 6

    # Make sure

# Generated at 2022-06-13 16:05:55.981276
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test1(metaclass=_ABCSingleton):
        pass

    class Test2(metaclass=_ABCSingleton):
        pass

    assert Test1() is Test1()
    assert Test1() is not Test2()

# Generated at 2022-06-13 16:05:59.947696
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton
        pass

    foo = Foo()
    assert isinstance(foo, Foo)
    foo2 = Foo()
    assert foo is foo2
    assert issubclass(Foo, object)

# Generated at 2022-06-13 16:06:03.516771
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(metaclass=_ABCSingleton):
        pass

    assert A() is A()
    assert B() is B()
    assert A() is not B()
    assert B() is not A()

# Generated at 2022-06-13 16:06:20.411356
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # force singleton to reset
    GlobalCLIArgs._instances = {}
    _options = ImmutableDict({'a': 1, 'b': {'c': 2}, 'd': [{1: 2, 'f': 'g'}]})
    assert GlobalCLIArgs.from_options(_options) is GlobalCLIArgs.from_options(_options)

# Generated at 2022-06-13 16:06:25.859265
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    class C(A):
        pass

    assert A() is A()
    assert B() is B()
    assert C() is C()
    assert A() is not B()
    assert B() is not C()

# Generated at 2022-06-13 16:06:28.894064
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli_args = CLIArgs.from_options(MockOptions())
    assert cli_args['check'] == True

# Generated at 2022-06-13 16:06:39.114300
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test that we correctly transform an arbitrary group of nested python objects into
    immutable data types based on the same structure.
    """
    from copy import deepcopy

    global_ref_dict = {'a': {'b': 1,
                             'c': 2,
                             'd': 3},
                       'e': {'f': {'g': 4,
                                   'h': 5}},
                       'i': (1, 2, 3, 'abc'),
                       'j': (1, 2, {'k': 'abc'}, 3),
                       'l': set([1, 2, 3]),
                       'm': set([1, (1, 2), 'abc'])}

    # Make a copy of the reference dict so we can modify it
    local_dict = deepcopy(global_ref_dict)


# Generated at 2022-06-13 16:06:42.580273
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class Z(object):
        pass

    class A(Z, object, metaclass=_ABCSingleton):
        pass

    class B(A, object, metaclass=ABCMeta):
        pass

    class C(B, object):
        pass

# Generated at 2022-06-13 16:06:48.635936
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    class C(B, metaclass=_ABCSingleton):
        pass

    # This will fail if metaclass is Error because Python cannot choose between ABCMeta and Singleton
    class D(C):
        pass

    # No exceptions raised means test passed.
    pass

# Generated at 2022-06-13 16:06:58.325069
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    opts = {
        "foo": "bar",
        "bar": ([1,2,3],(4,5,6)),
        "baz": {
            "foo": "bar",
            "bar": [1,2,3],
            "baz": {
                "foo": "bar",
                "bar": [1,2,3],
                "baz": "foo",
            },
            "boo": [
                "foo",
                "bar",
                "baz"
            ]
        }
    }
    cliargs = CLIArgs(opts)
    assert cliargs.foo == "bar"
    assert cliargs.bar[0] == [1,2,3]
    assert cliargs.bar[1] == (4,5,6)

# Generated at 2022-06-13 16:07:00.132370
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs.from_options(GlobalCLIArgs()) is GlobalCLIArgs()

# Generated at 2022-06-13 16:07:11.348398
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Create a dummy command line option object
    from ansible_collections.ansible.community.plugins.module_utils.ansible_release import __version__ as ansible_version
    from argparse import Namespace

# Generated at 2022-06-13 16:07:17.082469
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

    # __metaclass__ resolution only works on new style classes
    class A(object):
        pass
    class B(object):
        pass
    class C(A):
        pass
    class D(B):
        pass

    # __metaclass__ resolution happens before __init__ is called
    class A(metaclass=_ABCSingleton):
        def __init__(self):
            super(A, self).__init__()
            self.a = 0

# Generated at 2022-06-13 16:07:45.467052
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.utils.boolean import boolean

    # since Display is a class that mutates it's own state, it could be seen as a singleton.
    # The reason we're testing it here is because there is no other
    # singleton that is guaranteed to be instantiated for all runs before the GlobalCLIArgs is.
    # If another singleton is added, this test could be moved to it's code.
    # Not the best place for the test but it'll do for now.
    d = Display()

# Generated at 2022-06-13 16:07:50.876411
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(object):
        __metaclass__ = _ABCSingleton
        def __init__(self, x=0):
            self.x = x

    assert X() is X()
    assert X(1) is X(1)
    assert type(X()) is type(X())
    assert type(X(1)) is type(X(1))

# Generated at 2022-06-13 16:07:58.137239
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'foo': 'bar', 'this': 'that', 'a': {'b': 'c'}, 'd': {'e': ['f', 'g'], 'h': 'i'}, 'j': ['k', 'l', {'m': 'n', 'o': ['p', 'q']}]}
    test = CLIArgs(test_dict)
    assert isinstance(test, ImmutableDict)
    assert test == test_dict
    assert test['foo'] == test_dict['foo']
    assert test['a']['b'] == test_dict['a']['b']
    assert test['d']['e'][0] == test_dict['d']['e'][0]

# Generated at 2022-06-13 16:08:06.077674
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        def __init__(self):
            self.foo = "bar"
            self.bar = ["baz", "quux"]
            self.baz = {"bam": set(["ham", "spam"])}
            self.quux = None

    options = Options()
    cliargs = CLIArgs.from_options(options)
    assert cliargs.foo == "bar"
    assert cliargs.bar == ["baz", "quux"]
    assert cliargs.baz == {"bam": set([u"ham", u"spam"])}
    assert cliargs.quux is None


# Generated at 2022-06-13 16:08:08.848275
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class test_class(object):
        __metaclass__ = _ABCSingleton
    assert issubclass(test_class, Singleton)
    assert issubclass(test_class, ABCMeta)

# Generated at 2022-06-13 16:08:12.410922
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    instance = CLIArgs({'foo': [1, 2, 3], 'bar': {'a': 'b'}})
    assert instance['foo'] == (1, 2, 3)
    assert instance['bar'] == ImmutableDict({'a': 'b'})



# Generated at 2022-06-13 16:08:18.090073
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args1 = GlobalCLIArgs.get_instance()
    args2 = GlobalCLIArgs.get_instance()
    assert args1 is args2
    assert args1 == args2
    assert args1.__class__ is GlobalCLIArgs
    args1['test'] = 'test'
    assert args2['test'] == 'test'
    assert args1 is args2
    # Ensuring that the class is hashable
    hash(GlobalCLIArgs)

# Generated at 2022-06-13 16:08:26.508537
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:08:31.673654
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=unused-variable,unused-argument
    class GlobalCLIArgsImpl(GlobalCLIArgs):
        """Used in unit testing only"""
        pass

    arg1 = GlobalCLIArgsImpl.from_options(None)
    arg2 = GlobalCLIArgsImpl.from_options(None)

    # Verify that the names of the two arguments are the same
    assert arg1 is arg2


# Generated at 2022-06-13 16:08:37.806576
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    from ansible.config.manager import ConfigManager
    from ansible.config.cli.args import parse_vault_opts_into_dict
    from ansible.cli.context import CLI
    from ansible.plugins.loader import find_plugin_filters
    from ansible.plugins.callback.default import CallbackModule
    from ansible.plugins.action.normal import ActionModule
    from ansible.cli import CLI

    # Put an instance of GlobalCLIArgs into the global context
    args = CLI().parser.parse_args(["--connection=local", "--forks=1", "--version"])
    GlobalCLIArgs.from_options(args)

    # This variable should always be empty.  If not, we are accidentally leaking information from
    # one test run to another.
   

# Generated at 2022-06-13 16:09:31.817004
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from collections import MutableMapping
    from ansible.module_utils.common.collections import is_mutable_mapping
    from ansible.module_utils.common.collections import is_immutable_mapping
    import pytest
    GlobalCLIArgs({1: "hello", 2: "world"})
    GlobalCLIArgs({1: "hello", 2: MutableMapping()})
    # This test fails because the constructor of ImmutableDict doesn't work with MutableMapping as
    # arguments.
    with pytest.raises(TypeError):
        GlobalCLIArgs({1: "hello", 2: MutableMapping([(1, "hello"), (2, "world")])})
    immutable_dict = ImmutableDict({1: "hello", 2: "world"})