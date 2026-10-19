

# Generated at 2022-06-13 15:59:39.392196
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = {'test1': 1234, 'test2': ['a', 'b', {'test3': [1, 2, 3]}]}
    test_args = CLIArgs(args)

    assert test_args == {'test1': 1234, 'test2': ('a', 'b', {'test3': (1, 2, 3)})}

# Generated at 2022-06-13 15:59:45.452576
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.utils.display import Display
    Display.verbosity = 2
    a1 = GlobalCLIArgs.from_options(Display)
    a2 = GlobalCLIArgs.from_options(Display)
    if a1 != a2:
        raise AssertionError('singleton test failed.')

# Generated at 2022-06-13 15:59:49.102601
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    Number = collections.namedtuple('Number', ['value'])
    number = Number(1)
    assert CLIArgs.from_options({'key': {'value': number}}) == {'key': {'value': number}}

# Generated at 2022-06-13 15:59:52.751896
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    command_line_args = {'foo': ['bar', 'baz'], 'baz': 'foo'}
    gargs = GlobalCLIArgs(command_line_args)
    assert gargs.get('foo') == ('bar', 'baz')
    assert gargs.get('baz') == 'foo'

# Generated at 2022-06-13 16:00:02.282555
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs.from_options(None)
    assert isinstance(a, ImmutableDict)
    assert a == {}

    # Test that GlobalCLIArgs throws an error when it gets this input
    # It should not be possible to create a GlobalCLIArgs with a subclassed dict
    # or with a dict with a subclassed dict inside of it.  This is because GlobalCLIArgs
    # should always be an immutable dict.
    class A(dict):
        """Subclass of a dict"""
        pass

    class B(dict):
        """Subclass of a dict"""
        pass

    try:
        GlobalCLIArgs(A())
    except TypeError:
        pass

    try:
        GlobalCLIArgs({'a': A()})
    except TypeError:
        pass


# Generated at 2022-06-13 16:00:04.812275
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass
    class B(A):
        pass
    assert B() is B()


# Generated at 2022-06-13 16:00:14.295327
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = dict()
    test_dict['verbosity'] = 1
    test_dict['ask_vault_pass'] = 0
    test_dict['ask_pass'] = 1
    test_dict['connection'] = 'ssh'
    test_dict['force_handlers'] = 0
    test_dict['module_path'] = ['/Users/user/code/ansible/hacking/test/units/modules']
    test_dict['become_user'] = 'root'
    test_dict['private_key_file'] = None
    test_dict['private_key_file_passphrase'] = None
    test_dict['become'] = False
    test_dict['become_method'] = 'sudo'
    test_dict['extra_vars'] = dict()

# Generated at 2022-06-13 16:00:16.257272
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    c = GlobalCLIArgs({'foo': 'bar'})
    assert c


# Generated at 2022-06-13 16:00:18.653583
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(object):
        __metaclass__ = _ABCSingleton

    assert Test() is Test()  # Singleton identity



# Generated at 2022-06-13 16:00:21.601856
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class C(object):
        __metaclass__ = _ABCSingleton
        def __init__(self):
            pass
    c = C()

# Generated at 2022-06-13 16:00:30.474735
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Unit test for CLIArgs

    We don't want to leak any mutable data in the CLIArgs object, so we test that it was
    converted to immutable data types by creating a bunch of nested objects and then modifying
    them with a second pass.
    """
    test_list = ['one', 'two', 'three']
    test_set = set(test_list)
    test_dict = {'test_list': test_list,
                 'test_set': test_set,
                 'test_dict': {'test_dict': {'test_dict': {'test_dict': {'test_dict': 'one'}}}}}
    cli_args = CLIArgs(test_dict)

    test_list.pop()
    test_list.append('three')
    test_set.add('four')

# Generated at 2022-06-13 16:00:41.557476
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import ansible.cli
    import ansible.utils.collection_loader

    class DummyOptParser(object):
        def __init__(self):
            self.version = '2.7.12'

        def parse_args(self, args=None, namespace=None):
            return (self, ansible.utils.collection_loader.CLICollectionLoader())

    class DummyOptParser2(object):
        def __init__(self):
            self.version = '2.7.12'
            self.connection = 'local'

        def parse_args(self, args=None, namespace=None):
            return (self, ansible.utils.collection_loader.CLICollectionLoader())

    args = ['test']

# Generated at 2022-06-13 16:00:45.843488
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_args = dict(
        test_arg=True,
        test_int_arg=42,
        test_list_arg=['a', 'b', 'c'],
    )
    exp_output = ImmutableDict(dict(
        test_arg=True,
        test_int_arg=42,
        test_list_arg=('a', 'b', 'c'),
    ))
    assert CLIArgs(test_args) == exp_output



# Generated at 2022-06-13 16:00:49.986050
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import doctest
    from ansible.utils import context_objects

    failed, tests = doctest.testmod(context_objects)
    if failed == 0:
        print('PASSED: %s tests' % tests)

# Generated at 2022-06-13 16:00:53.755421
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(GlobalCLIArgs):
        def __new__(cls):
            return object.__new__(cls)

    assert isinstance(TestSingleton(), TestSingleton)


# Unit tests for the CLIArgs class

# Generated at 2022-06-13 16:01:00.482563
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class A:
        def __init__(self, val):
            self.val = val
    m1 = {'key1': 'value1'}
    m2 = {'key2': A('value2')}
    o1 = GlobalCLIArgs.from_options(m1)
    o2 = GlobalCLIArgs.from_options(m2)
    assert o1 == m1
    assert o2 == m2


if __name__ == '__main__':
    test_GlobalCLIArgs()

# Generated at 2022-06-13 16:01:07.966892
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # pylint: disable=protected-access
    # pylint: disable=no-member
    cli_args = CLIArgs({
        'x': 42,
        'y': {'a': 'a', 'b': 'b'},
        'z': ['a', 'b'],
        'z2': {'a', 'b'},
    })
    assert cli_args._dict is cli_args
    assert cli_args._dict['x'] == 42
    assert cli_args._dict['y']._dict == {'a': 'a', 'b': 'b'}
    assert cli_args._dict['z']._dict == ('a', 'b')
    assert cli_args._dict['z2']._dict == frozenset({'a', 'b'})

# Generated at 2022-06-13 16:01:17.310616
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Test the GlobalCLIArgs class.

    CLIArgs is tested through the use of the GlobalCLIArgs class.  The GlobalCLIArgs is a singleton
    wrapper around the CLIArgs class.  Only one of these exist per program as it is for global context.
    """
    m = {'s': 4, 'q': (1, 2), 'f': 3, 't': (2, 3), 'r': {'a': 'b', 'c': 'd'}, 'intro': 'me'}
    global_test_args = GlobalCLIArgs(m)

    import copy
    arg_dict = copy.deepcopy(m)
    for key, value in arg_dict.items():
        if isinstance(value, dict):
            arg_dict[key] = ImmutableDict(value)

# Generated at 2022-06-13 16:01:19.596334
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({'a': 1, 'b': {'c': 'd'}}) == {'a': 1, 'b': {'c': 'd'}}

# Generated at 2022-06-13 16:01:24.822939
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonTest(metaclass=_ABCSingleton):
        pass
    assert isinstance(_ABCSingletonTest, ABCMeta)
    # test that we have exactly one instance of this class
    o1 = _ABCSingletonTest()
    o2 = _ABCSingletonTest()
    assert o1 is o2


# Generated at 2022-06-13 16:01:28.809477
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {"a": 1, "b": 2, "c": 3}
    args = CLIArgs(test_dict)
    assert args == test_dict

# Generated at 2022-06-13 16:01:30.994906
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Make sure we don't get an exception for not properly combining
    # the metaclasses
    class TestABCSingleton(_ABCSingleton):
        pass

    TestABCSingleton()

# Generated at 2022-06-13 16:01:37.625611
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import json
    import re
    import os

    def _run(idx, arg, expected):
        arg_type = arg.split(':')[0]
        val = arg.split(':')[1]
        if arg_type == 'str':
            arg = val
        elif arg_type == 'int':
            arg = int(val)
        elif arg_type == 'float':
            arg = float(val)
        elif arg_type == 'bool':
            arg = True if val == 'True' else False
        elif arg_type == 'ls':
            arg = list(val.split('|'))
        elif arg_type == 'tpl':
            arg = tuple(val.split('|'))
        elif arg_type == 'dict':
            arg = json.loads(val)

# Generated at 2022-06-13 16:01:47.799135
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.config.manager import ConfigManager
    from ansible.utils.args import load_command_line_config
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    args = ['--version']
    config = ConfigManager(args=args)
    load_command_line_config(config, args)

    option_obj = AnsibleCollectionConfig()
    option_obj.set_collection_playbook_paths(config.get_config_value('collection_playbook_paths'))
    option_obj.set_collection_paths(config.get_config_value('collections_path'))
    option_obj.set_playbook_paths(config.get_config_value('playbook_path'))
    collection_options = vars(option_obj)

    # Second run for class GlobalCLI

# Generated at 2022-06-13 16:01:58.713514
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import unittest
    import collections
    import ansible.utils.argparsing as argparsing
    import ansible.module_utils.common._text as text
    parser = argparsing.ArgumentParser(description="some fake text", epilog="some other fake text")
    parser.add_argument('other_args', nargs='*', metavar="other_args")
    parser.add_argument('--version', action='version', version=text.version('ansible'))
    fake_options = parser.parse_args(['other_args', '-c', 'xxx', '-o', '-k', '-u', 'ec2_user', '-e', 'xxx', 'xxx'])

# Generated at 2022-06-13 16:02:06.743871
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Blah(object):
        __metaclass__ = _ABCSingleton

    class Blah2(object):
        __metaclass__ = _ABCSingleton

    assert Blah() is Blah()
    assert Blah2() is Blah2()
    assert Blah() is not Blah2()

    class Blah(object):
        __metaclass__ = ABCMeta

    class Blah2(object):
        __metaclass__ = Singleton

    class Blah3(Blah, Blah2):
        pass

    try:
        _ = Blah3()
        assert False, "TypeError should have been raised."
    except TypeError:
        pass

    class Blah3(Blah2, Blah):
        pass


# Generated at 2022-06-13 16:02:15.752911
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        __slots__ = ['a']
        def __init__(self, a):
            self.a = a

    class B(metaclass=_ABCSingleton):
        __slots__ = ['a', 'b']
        def __init__(self, a, b):
            self.a = a
            self.b = b

    from ansible.module_utils.six import with_metaclass
    assert issubclass(with_metaclass(B, A), A)
    assert issubclass(with_metaclass(A, B), B)
    assert not issubclass(A, B)
    assert not issubclass(B, A)
    assert issubclass(B, A) and issubclass(A, B)

# Generated at 2022-06-13 16:02:18.529198
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(object):
        __metaclass__ = _ABCSingleton

    assert A() is A()
    assert B() is B()
    assert A() is not B()

# Generated at 2022-06-13 16:02:24.651330
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class A(dict):
        pass

    a = A({'a': 1,
           'b': [{'c': 1,
                  'd': [{'e': 1}]}]})

    cli = CLIArgs(a)

    assert cli['a'] == 1

    cli_b = cli['b']
    assert cli_b[0]['c'] == 1
    assert cli_b[0]['d'][0]['e'] == 1

    cli2 = CLIArgs(cli)
    assert cli2['a'] == 1
    cli_b2 = cli2['b']
    assert cli_b2[0]['c'] == 1
    assert cli_b2[0]['d'][0]['e'] == 1


# Generated at 2022-06-13 16:02:28.877853
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Constructor tests
    try:
        g_cli_args = GlobalCLIArgs(vars(CLIArgs.from_options(None)))
    except TypeError as ex:
        assert 'object not callable' in str(ex)

    # Singleton tests
    g1 = GlobalCLIArgs(vars(CLIArgs.from_options(None)))
    g2 = GlobalCLIArgs(vars(CLIArgs.from_options(None)))
    assert g1 is g2



# Generated at 2022-06-13 16:02:37.548053
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # This test is not very good, should be improved
    class Option(object):
        def __init__(self, **kwargs):
            self.values = kwargs

    opts = Option(connection='mock', check=False, diff=True)
    cli_args = CLIArgs.from_options(opts)
    assert cli_args['check'] is False
    assert cli_args['connection'] == 'mock'
    assert cli_args['diff'] is True



# Generated at 2022-06-13 16:02:42.298779
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    dummy_options = {
        'version': '0.0.0.0',
        'verbosity': 0,
    }

    fake_options = CLIArgs.from_options(dummy_options)
    assert fake_options.version == '0.0.0.0'
    assert fake_options.verbosity == 0


# Generated at 2022-06-13 16:02:51.872105
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Arrange
    test_values = {
        'strkey': 'strval',
        'intkey': 1,
        'listkey': [1,2,3],
        'dictkey': {'x': 5}}
    expected_values = {'strkey': 'strval',
        'intkey': 1,
        'listkey': (1, 2, 3),
        'dictkey': {'x': 5}}

    # Act
    test_obj = CLIArgs(test_values)

    # Assert
    assert test_obj == expected_values


# Generated at 2022-06-13 16:02:53.540746
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    (options, args) = GlobalCLIArgs.from_options(None)
    assert options==None
    assert args==None

# Generated at 2022-06-13 16:03:03.608329
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test _make_immutable()
    assert _make_immutable("a") == "a"
    assert _make_immutable(("a",)) == ("a",)
    assert _make_immutable("abc") == "abc"
    assert _make_immutable("abc") is not "abc"
    assert _make_immutable({"a": "b"}) == ImmutableDict([("a", "b")])
    assert _make_immutable({"a": "b"}) is not ImmutableDict([("a", "b")])
    assert _make_immutable([{"a": "b"}, {"c": "d"}]) == ([ImmutableDict([("a", "b")]), ImmutableDict([("c", "d")])],)

# Generated at 2022-06-13 16:03:09.808151
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Create an instance of GlobalCLIArgs and attempt to change it's value.  Because it's a Singleton
    this should fail and raise an exception.
    """
    cliargs = GlobalCLIArgs.from_options(
        {'foo': 'bar',
         'spam': 'ham',
         'nested': {'level_one': 'level_two',
                    'list': ['one', 'two', 'three'],
                    'set': set(['one', 'two', 'three'])}}
    )
    other = GlobalCLIArgs.from_options(None)
    try:
        cliargs['foo'] = 'baz'
        raise RuntimeError('Failed to raise exception when changing value in singleton')
    except TypeError as e:
        pass

# Generated at 2022-06-13 16:03:11.761243
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo():
        __metaclass__ = _ABCSingleton
    assert isinstance(Foo(), Foo)

# Generated at 2022-06-13 16:03:13.340335
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    print(type(GlobalCLIArgs.instance()))
    assert type(GlobalCLIArgs.instance()) == GlobalCLIArgs

# Generated at 2022-06-13 16:03:16.653254
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = {'foo': 'bar'}

    obj = GlobalCLIArgs(args)
    assert obj['foo'] == args['foo']
    assert getattr(obj, 'foo') == args['foo']

# Generated at 2022-06-13 16:03:26.315317
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Unit test for class CLIArgs
    """
    class options:
        foo = [1, 2, 3, 'a', {}, [], (1, 2, 3)]
        bar = {'a': 1, 'b': 2, 'c': 3}
        baz = {'a': [], 'b': {'a': 1}, 'c': (1, 2, 3)}
    cli_args = CLIArgs.from_options(options)
    assert type(cli_args) == CLIArgs
    assert type(cli_args['foo']) == tuple
    assert type(cli_args['bar']) == ImmutableDict
    assert type(cli_args['baz']) == ImmutableDict
    assert type(cli_args['baz']['a']) == tuple

# Generated at 2022-06-13 16:03:40.169040
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # This does not actually test that GlobalCLIArgs is a global object, but it does assert that
    # GlobalCLIArgs has the intended metaclass and that it uses the correct __new__ method.
    from ansible.module_utils.common.dict_transformations import dictmerge
    from ansible.module_utils.common.parameters import ParseableDict
    from ansible.utils.path import unfrackpath

    class Options(dict):
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)

    options = Options()
    options.ansible_config_file = unfrackpath("/path/to/ansible/config")
    options.output_file = unfrackpath("/path/to/output")
    options.module_path = unfrack

# Generated at 2022-06-13 16:03:46.679163
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs(dict(ANSIBLE_MODULE_ARGS=dict(a=1, b=2, c=3), ANSIBLE_MODULE_ARGS_INCLUDE_ROOT=True))

    assert isinstance(args, ImmutableDict)
    assert args == dict(ANSIBLE_MODULE_ARGS=dict(a=1, b=2, c=3), ANSIBLE_MODULE_ARGS_INCLUDE_ROOT=True)
    assert isinstance(args['ANSIBLE_MODULE_ARGS'], ImmutableDict)
    assert args['ANSIBLE_MODULE_ARGS'] == dict(a=1, b=2, c=3)

# Generated at 2022-06-13 16:03:48.432954
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'

# Generated at 2022-06-13 16:03:54.905709
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test that CLIArgs can instantiate as expected
    """
    import random

    # Create some random args, and test that they are set correctly
    test_args = {}
    for i in range(random.randint(1, 15)):
        test_args[str(i)] = random.randint(1, 50)

    cli_args = CLIArgs(test_args)

    for key in test_args.keys():
        assert key in cli_args, "Key %s should be in CLIArgs instance" % key
        assert test_args[key] == cli_args[key], "Value for key %s should be %s but was %s" % (key, test_args[key], cli_args[key])

    # Create some random args, and test that they are immutable
    test_args = {}
   

# Generated at 2022-06-13 16:03:57.010228
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(object):
        __metaclass__ = _ABCSingleton
    assert isinstance(TestClass(), object)

# Generated at 2022-06-13 16:04:07.713456
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class MockOpts(object):
        def __init__(self, mydict):
            for key, value in mydict.items():
                setattr(self, key, value)

    testdict = {
        'a_text': text_type('a_text'),
        'a_binary': binary_type('a_binary'),
        'a_list': [1, 2, 3],
        'a_tuple': (4, 5, 6),
        'a_dict': {'a': 0, 'b': 1},
        'a_set': set(('c', 'd', 'e')),
        'a_int': 7,
        'a_float': 8.1,
        'a_complex': 5+4j
    }
    my_opts = MockOpts(testdict)

# Generated at 2022-06-13 16:04:19.149476
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    inputs = {
        'text': 'text as text',
        'bytes': b'bytes as bytes',
        'list': [1, 2, 3],
        'set': set([1, 2, 3]),
        'dict': {'a': 'b'},
        'nested_mapping': {'a': [1, 2, 3], 'b': {'c': 'd'}},
        'nested_sequence': [1, [2, [3, [4]]]],
        'list_of_list_of_list': [[[1, 2, 3], [4, 5, 6]]]
    }

# Generated at 2022-06-13 16:04:30.114130
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=protected-access
    assert GlobalCLIArgs._inst is None
    assert len(GlobalCLIArgs._instances) == 0
    try:
        GlobalCLIArgs({"foo": 1})
    except TypeError:
        pass
    else:
        assert False, "GlobalCLIArgs should not allow itself to be instantiated"
    assert GlobalCLIArgs._inst is None
    assert len(GlobalCLIArgs._instances) == 0
    GlobalCLIArgs.create({"foo": 1})
    assert GlobalCLIArgs._inst is not None
    assert len(GlobalCLIArgs._instances) == 1
    try:
        GlobalCLIArgs.create({"bar": 2})
    except ValueError:
        pass

# Generated at 2022-06-13 16:04:32.557633
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton(_ABCSingleton):
        pass

    assert isinstance(TestSingleton(), TestSingleton)


# Generated at 2022-06-13 16:04:37.354220
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs == GlobalCLIArgs.__new__(GlobalCLIArgs)
    g = GlobalCLIArgs.__new__(GlobalCLIArgs)
    assert g is GlobalCLIArgs.__new__(GlobalCLIArgs)
    assert not hasattr(g, '__init__')
    assert g is GlobalCLIArgs.__new__(GlobalCLIArgs)
    assert g.__class__ is GlobalCLIArgs

# Generated at 2022-06-13 16:04:53.007058
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    def assert_immutable(value):
        try:
            value[0] = None
        except TypeError:
            pass
        else:
            raise AssertionError("Expected a TypeError to be raised")


# Generated at 2022-06-13 16:05:04.510223
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test CLIArgs with simple types"""
    mapping = {u'foo': u'bar', u'baz': 1, u'qux': False}
    obj = CLIArgs(mapping)

    # We expect all strings to be unicode
    assert isinstance(obj.get(u'foo'), text_type)
    assert isinstance(obj.get(u'baz'), int)
    assert isinstance(obj.get(u'qux'), bool)

    # We expect the strings "foo" and "baz" to be equal to
    # the unicode strings u"foo" and u"baz" respectively
    assert obj.get(u'foo') == u'bar'
    assert obj.get(u'baz') == 1
    assert obj.get(u'qux') is False



# Generated at 2022-06-13 16:05:08.045942
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class test_class1(object):
        __metaclass__ = _ABCSingleton

    class test_class2(object):
        __metaclass__ = _ABCSingleton

    assert test_class1() is test_class2()

# Generated at 2022-06-13 16:05:16.985089
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    toplevel = {}
    toplevel['foo'] = "bar"
    toplevel['baz'] = "boo"
    toplevel['func'] = lambda x: x + 1
    toplevel['list'] = ['one', 'two', 'three']
    toplevel['dict'] = {'one': 1, 'two': 2, 'three': 3}
    toplevel['tuple'] = (1, 2, 3)
    toplevel['set'] = set([1, 2, 3])
    toplevel['set_of_sets'] = set([{1, 2}, {3, 4}, {5, 6}])
    toplevel['list_of_dicts'] = [{'one': 1, 'two': 2}, {'three': 3, 'four': 4}]

# Generated at 2022-06-13 16:05:27.626882
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest
    from collections import MutableMapping
    from ansible.utils.path import unfrackpath


# Generated at 2022-06-13 16:05:36.921705
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from collections import namedtuple
    from ansible.module_utils._text import to_bytes

    test_args = namedtuple('TestArgs', 'debug check no_log verbosity')
    args = test_args(
        debug=True,
        check=False,
        no_log=False,
        verbosity=3,
    )

    cli = CLIArgs.from_options(args)
    assert cli['debug'] is True
    assert cli['check'] is False
    assert cli['no_log'] is False
    assert cli['verbosity'] == 3

    # TODO: add tests for args with non-string keys,
    #       and maybe some non-container values

# Generated at 2022-06-13 16:05:42.394960
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common._collections_compat import Sequence

    args = CLIArgs({'foo': 'bar', 'horse': 'whinney', 'numbers': [1, 2, 3],
                    'letters': ('a', 'b', 'c'), 'mixed': (1, 2, 'three', 'four', 'five', False)})
    assert isinstance(args['numbers'], Sequence)
    assert isinstance(args['letters'], Sequence)
    assert isinstance(args['mixed'], Sequence)

# Generated at 2022-06-13 16:05:45.988097
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    gca = GlobalCLIArgs.from_options(dict(a=1, b=2))
    assert isinstance(gca, GlobalCLIArgs)
    assert gca['a'] == 1
    assert gca['b'] == 2


# Generated at 2022-06-13 16:05:49.434016
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    original = {
        "debug": False,
        "inventory": [],
        "module_path": [],
        "forks": 10,
        "playbook_path": [],
        "version": False,
    }

    args = GlobalCLIArgs(original)

    assert isinstance(args, ImmutableDict)



# Generated at 2022-06-13 16:05:54.907556
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from io import StringIO

    try:
        from ansible.utils.display import Display
        display = Display()
        display.verbosity = 4
    except ImportError:
        display = None

    # Create an ArgumentParser mock

# Generated at 2022-06-13 16:06:15.445374
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options():
        pass

    opts = Options()
    opts.foo = "bar"
    opts.bar = ["hello", "world"]

    args = GlobalCLIArgs.from_options(opts)

    assert args["foo"] == "bar"
    assert args["bar"] == ("hello", "world")

    # Test for the immutability part of the constructor
    # We wrap in a try/except and use a raise AssertionError, because we don't have
    # any way to override __setitem__ to allow an exception to be raised
    try:
        args['bar'] = "changed"
        raise AssertionError("Item was not made to be immutable")
    except TypeError:
        pass

# Generated at 2022-06-13 16:06:20.224415
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    a = CLIArgs({'a': 1, 'b': {'c': {'d': [1, 2, 3]}}})
    assert a == ImmutableDict({'a': 1, 'b': ImmutableDict({'c': ImmutableDict({'d': (1, 2, 3)})})})

# Generated at 2022-06-13 16:06:23.478691
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass1(object):
        __metaclass__ = _ABCSingleton

    assert isinstance(TestClass1(), TestClass1)
    assert TestClass1() is TestClass1()

# Generated at 2022-06-13 16:06:26.549754
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    a = A()
    b = A()
    assert a is b
    assert issubclass(A, ABCMeta)

# Generated at 2022-06-13 16:06:29.486497
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs({'a': 1})
    b = GlobalCLIArgs(a)
    assert a == b
    assert a is b

# Generated at 2022-06-13 16:06:34.548494
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(object):
        __metaclass__ = _ABCSingleton

    assert A() == A()

    # No error means test passed
    try:
        A() == B()
    except Exception:
        assert False, "Got exception when ABC and Singleton metaclasses should not have conflicted"

# Generated at 2022-06-13 16:06:43.833564
# Unit test for constructor of class CLIArgs
def test_CLIArgs():

    non_immutable_dict = {
        'foo': 'bar',
        'baz': ['abc', 'def'],
        'qux': {
            'cat': 'dog',
            'horse': 'sheep',
        }
    }

    class FakeOptions(object):
        def __init__(self):
            for key in non_immutable_dict:
                setattr(self, key, non_immutable_dict[key])

    options = FakeOptions()
    cli_args = CLIArgs.from_options(options)

    assert cli_args == non_immutable_dict
    assert isinstance(cli_args, CLIArgs)
    assert isinstance(cli_args, ImmutableDict)
    assert not isinstance(cli_args, dict)


# Generated at 2022-06-13 16:06:49.679737
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Test that CLIArgs sets each item and all their nested items as immutable"""
    from ansible.module_utils.common.collections import MutableMapping
    from ansible.module_utils.common.collections import MutableSet
    from ansible.module_utils.common.collections import MutableSequence

    test_mutable_mapping = MutableMapping()
    test_mutable_mapping['mutable_key'] = 'mutable_value'
    test_mutable_mapping['immutable_key'] = 'immutable_value'
    test_mutable_mapping['mutable_set'] = MutableSet()
    test_mutable_mapping['mutable_set'].add('mutable_set_value')
    test_mutable_mapping['immutable_set'] = frozenset()
   

# Generated at 2022-06-13 16:06:59.255569
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {}
    test_dict['somedict'] = {'key1': 'value1', 'key2': 'value2'}
    test_dict['somefrozenset'] = frozenset(['value3', 'value4'])
    test_dict['sometuple'] = ('value5', 'value6')
    test_dict['somethingelse'] = 'value7'
    test_object = CLIArgs(test_dict)

    assert isinstance(test_object, ImmutableDict)
    assert isinstance(test_object['somedict'], ImmutableDict)
    assert isinstance(test_object['somefrozenset'], frozenset)
    assert isinstance(test_object['sometuple'], tuple)
    assert test_object['somethingelse'] == 'value7'

    assert len

# Generated at 2022-06-13 16:07:07.294027
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.cli import CLI
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import cli_plugins

    _, options, _ = CLI.base_parser(cli_plugins=cli_plugins, usage='%prog some_module [options]',
                                     desc='Ansible module interface').parse_args(args=['something'])
    context = PlayContext()
    context.CLI = options
    context.CLIARGS = dict()
    context.module_name = 'something'
    GlobalCLIArgs(context.CLI)

# Generated at 2022-06-13 16:07:32.586911
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs(ImmutableDict(names=['Bob', 'Alice'], ages=[32, 24]))
    assert args.names == ('Bob', 'Alice')
    assert args.ages == (32, 24)
    ImmutableDict.__setitem__(args, "names", ['Spongebob', 'Patrick'])
    assert args.names == ('Spongebob', 'Patrick')

    # Construct a new instance of this type of object
    another_instance = _ABCSingleton.__call__(GlobalCLIArgs)
    assert another_instance is args

# Generated at 2022-06-13 16:07:35.089562
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # pylint: disable=unused-variable,unused-argument
    try:
        class MockSingleton(object):
            pass
        GlobalCLIArgs(MockSingleton())
        assert False, "GlobalCLIArgs did not raise exception when passed wrong type"
    except TypeError:
        pass

# Generated at 2022-06-13 16:07:38.215735
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    class Bar(Foo):
        pass

    assert isinstance(Foo(), Foo)
    assert isinstance(Bar(), Foo)
    assert not isinstance(Foo(), type)

# Generated at 2022-06-13 16:07:41.647802
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {"a": "b", "c": 123, "d": ["a", "b", "c"],
                 "e": {"f": ["a", "b", "c"]},
                 "g": {"h": {"i": ["a", "b", "c"]}}}
    cli_args = CLIArgs(test_dict)
    assert cli_args == test_dict

# Generated at 2022-06-13 16:07:53.501946
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Create a new object
    obj = CLIArgs({'one': 1,
                   'two': 2,
                   'three': 3})
    assert obj['one'] == 1
    assert obj['two'] == 2
    assert obj['three'] == 3
    try:
        obj['four']
        assert False
    except KeyError:
        pass

    # Test immutability
    try:
        obj['one'] += 1
        assert False
    except TypeError:
        pass
    try:
        obj['two'] -= 1
        assert False
    except TypeError:
        pass
    try:
        obj['three'] = 4
        assert False
    except TypeError:
        pass
    try:
        del obj['three']
        assert False
    except TypeError:
        pass

# Generated at 2022-06-13 16:07:59.355557
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """Test we can create an object with _ABCSingleton as its metaclass"""
    class TestABCSingleton(object):
        """A dummy class needed to test the metaclass _ABCSingleton"""
        __metaclass__ = _ABCSingleton

    something = TestABCSingleton()

    assert something is TestABCSingleton()

# Generated at 2022-06-13 16:08:03.097467
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(metaclass=_ABCSingleton):
        pass

    class C(A, B):
        pass

    class D(B, A):
        pass

    assert C is D

# Generated at 2022-06-13 16:08:05.393391
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestSingleton0(object):
        __metaclass__ = _ABCSingleton

    obj1 = TestSingleton0()
    obj2 = TestSingleton0()
    assert obj1 is obj2

# Generated at 2022-06-13 16:08:09.168589
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options = ImmutableDict({'a': 'valueA', 'b': 'valueB', 'c': {'d': 'valueD', 'e': 'valueE'}})
    global_cli_args = CLIArgs.from_options(options)
    assert global_cli_args['a'] == 'valueA'

# Generated at 2022-06-13 16:08:19.507704
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Create an instance of GlobalCLIArgs and make sure it works
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    import os

    os.environ['ANSIBLE_PASSPHRASE'] = 'V3ryS3cur3'

    dataloader = DataLoader()
    ansible_vars = dataloader.load_from_file('test/unit/cli/test_ansible_vars.yml')
    context = PlayContext(CLIArgs.from_options(ansible_vars))

    ansible_vars = GlobalCLIArgs.from_options(ansible_vars)
    assert ansible_vars['ask_pass'] is False

# Generated at 2022-06-13 16:09:05.097814
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys
    import subprocess

    # assert that the object is really a singleton
    g1 = GlobalCLIArgs.from_options(None)
    g2 = GlobalCLIArgs.from_options(None)
    assert g1 is g2

    # this is a sad test case.  We have to create a new process because otherwise we already have the
    # cli args in the global variables from the process that is running this test.  If we don't do this
    # we won't correctly catch the error of trying to mutate the immutable dict.
    args = ['python', '-c', "from ansible.cli import CLIArgs; g = CLIArgs.from_options(None); g['changed'] = True"]
    result = subprocess.run(args, stdout=subprocess.PIPE)

# Generated at 2022-06-13 16:09:15.523047
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.network import ModuleStdin
    from ansible.module_utils.common.parameters import BASE_PARAMETERS

    class Options:
        pass
    options = Options()
    options.accelerate_port = 5099
    options.accelerate_timeout = 30
    options.action_plugins = None
    options.aliases = None
    options.ask_pass = False
    options.ask_private_key_pass = False
    options.ask_sudo_pass = False
    options.ask_vault_pass = False
    options.become = False
    options.become_ask_pass = False
    options.become_method = 'sudo'
    options.bec

# Generated at 2022-06-13 16:09:18.642628
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    c1 = GlobalCLIArgs(dict(a=1, b=2))
    assert c1.a == 1
    assert c1.b == 2

    c2 = GlobalCLIArgs(dict(a=1, b=2))
    assert c1 is c2

# Generated at 2022-06-13 16:09:20.304563
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test for dict -> CLIArgs
    assert isinstance(CLIArgs({'flag':True}), CLIArgs)


# Generated at 2022-06-13 16:09:29.953910
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    innerdict_1 = {"key1": "value1"}
    innerdict_2 = {"key2": "value2"}
    innerlist_1 = ["item1"]
    innerlist_2 = ["item2"]
    innerlist_dict_1 = {"item1": "item2"}
    innerlist_dict_1 = {"item1": "item2"}
    innerlist_dict_2 = {"item1": "item1"}
    innerset_1 = {"item1"}
    innerset_2 = {"item1"}

    dict_1 = {"key1": "value1"}
    dict_2 = {"key1": "value1"}
    list_1 = ["item1"]
    list_2 = ["item1"]
    list_dict_1 = {"item1": "item2"}

# Generated at 2022-06-13 16:09:32.511348
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest
    data = {'a': [1, 1], 'b': {'c': 'd'}}
    args = CLIArgs(data)
    assert args.a == data['a']
    assert args.b == data['b']
    assert args.b.c == data['b']['c']
    with pytest.raises(AttributeError):
        args.c