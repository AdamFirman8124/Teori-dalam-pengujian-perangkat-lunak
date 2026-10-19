

# Generated at 2022-06-13 15:59:42.947070
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.parsing import vault
    import ansible.constants as C

    # simple test of no-change situation
    mapping = {'foo': 'bar', 'baz': 'bat'}
    args = GlobalCLIArgs(mapping)
    assert args == mapping

    # make sure lists and sets are immutable
    mapping = {'foo': ['bar', 'baz']}
    args = GlobalCLIArgs(mapping)
    assert args == {'foo': ('bar', 'baz')}

    # make sure dicts are immutable
    mapping = {'foo': {'bar': 'baz'}}
    args = GlobalCLIArgs(mapping)
    assert args == {'foo': ImmutableDict({'bar': 'baz'})}

    # make sure we don't get ImmutableDict for non-

# Generated at 2022-06-13 15:59:50.590738
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': {'b': {'c': 1}}}
    new_mapping = CLIArgs(mapping)
    assert isinstance(new_mapping, ImmutableDict)
    assert all(isinstance(value, ImmutableDict) for value in new_mapping.values())
    assert all(isinstance(value, ImmutableDict) for value in new_mapping['a'].values())
    assert isinstance(new_mapping['a']['b']['c'], int)



# Generated at 2022-06-13 16:00:01.635917
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:00:10.510768
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:00:16.173818
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Ensure that the metaclass _ABCSingleton can be composed into other classes
    """

    class _VerySingleton(object):
        __metaclass__ = _ABCSingleton

    class _123Singleton(object):
        __metaclass__ = _ABCSingleton

    # These tests will fail if the metaclass composes improperly
    assert type(_VerySingleton()) is _VerySingleton
    assert type(_123Singleton()) is _123Singleton

# Generated at 2022-06-13 16:00:25.027997
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    import json

    args = [sys.argv[0],
            '-i', 'dummy_inven_file',
            '-u', 'dummy_user',
            '-l', 'dummy_hosts',
            '-m', 'dummy_module',
            '-a', json.dumps({'ANAR_ANSIBLE_TEST_VAR1': 'TEST_VAR1',
                              'ANAR_ANSIBLE_TEST_VAR2': 'TEST_VAR2'}),
            '-t', 'dummy_tags',
            '-v', 'dummy_verbose']

    print('CLIArgs: args:', args)
    cli_args = CLIArgs.from_options(get_optparser().parse_args(args)[0])
    print

# Generated at 2022-06-13 16:00:26.468637
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Just ensuring that it doesn't fail inside __new__
    class SingletonABC(metaclass=_ABCSingleton):
        pass

# Generated at 2022-06-13 16:00:27.961131
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs({})
    assert obj == {}

# Generated at 2022-06-13 16:00:34.974669
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    arg_dict = {'foo': True, 'bar': False, 'baz': {'1': 2, '3': 4}, 'qux': [5, 6]}
    cli_args = CLIArgs(arg_dict)
    assert cli_args == arg_dict
    assert isinstance(cli_args, Mapping)
    assert isinstance(cli_args['baz'], Mapping)
    assert not isinstance(cli_args['bar'], Mapping)

    test_dict = {'foo': 'bar'}
    cli_args['foo'] = test_dict
    assert cli_args['foo'] == test_dict
    assert isinstance(cli_args['foo'], Mapping)

    test_list = [1, 2]
    cli_args['baz']['3'] = test_list


# Generated at 2022-06-13 16:00:42.427834
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common._collections_compat import Mapping
    options = Mapping()
    options['test_key'] = 'test_value'
    options['test_key_2'] = ['test_value_2', 'test_value_3']
    options['test_key_3'] = {'test_key_4': 'test_value_4'}
    _g = GlobalCLIArgs.from_options(options)
    _ga = _g.get('ansible_version')
    assert _ga == {'full': '', 'short': ''}



# Generated at 2022-06-13 16:00:54.896937
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    This test is to validate that a GlobalCLIArgs class is created correctly
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--opt', type=str, default='val')
    parsed = parser.parse_args(['-o', 'arg'])
    args = GlobalCLIArgs.from_options(parsed)

    assert isinstance(args, GlobalCLIArgs)
    assert isinstance(args, ImmutableDict)



# Generated at 2022-06-13 16:00:56.369537
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TrySingleton(GlobalCLIArgs):
        pass
    TrySingleton()

# Generated at 2022-06-13 16:01:01.254537
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    test_map = {'a': 'b', 'c': {1: 2, 2: 5}, 'd': [1, 2, 3], 'e': {1, 2, 3}}
    global_cli = GlobalCLIArgs.from_options(test_map)
    assert global_cli == test_map

# Generated at 2022-06-13 16:01:02.639900
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClass(_ABCSingleton):
        pass

    assert TestClass() is TestClass()

# Generated at 2022-06-13 16:01:14.571434
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    cli = CLIArgs({'test' : 1})
    assert not isinstance(cli['test'], Mapping)
    assert cli['test'] == 1
    cli = CLIArgs({'test' : {'test2' : 1, 'test3': {'test4' : 1, 'test5' : [1, 2, 3], 'test6' : {'test7' : 1}}}})
    assert isinstance(cli['test'], Mapping)
    assert not isinstance(cli['test']['test2'], Mapping)
    assert not isinstance(cli['test']['test3'], Mapping)
    assert cli['test']['test2'] == 1
    assert isinstance(cli['test']['test3']['test4'], int)

# Generated at 2022-06-13 16:01:16.103106
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Test init method
    GlobalCLIArgs({'test': 'value'})



# Generated at 2022-06-13 16:01:20.772312
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(_ABCSingleton):
        pass

    class DerivedTestABCSingleton(TestABCSingleton):
        pass

    class DerivedABCSingleton(Singleton, ABCMeta):
        pass

    class DerivedImplicitlyTestABCSingleton(Singleton, TestABCSingleton):
        pass

    class DerivedFromDerivedExplicitlyTestABCSingleton(DerivedTestABCSingleton):
        pass

    class DerivedFromDerivedImplicitlyTestABCSingleton(DerivedImplicitlyTestABCSingleton):
        pass

    class DerivedFromDerivedFromDerivedImplicitlyTestABCSingleton(DerivedFromDerivedImplicitlyTestABCSingleton):
        pass

    new_instance = TestABCSingleton()
    assert new_instance
    assert new_instance is TestABCSingleton()


# Generated at 2022-06-13 16:01:30.353736
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Just make sure it can be called
    class A(object):
        @add_metaclass(_ABCSingleton)
        class B(object):
            pass
    # Make sure it can be called twice (i.e. no __new__)
    class A(object):
        @add_metaclass(_ABCSingleton)
        class B(object):
            pass
        @add_metaclass(_ABCSingleton)
        class C(object):
            pass
    try:
        class A(object, metaclass=_ABCSingleton):
            pass
    except TypeError:
        pass
    else:
        raise AssertionError(
            'Should not be able to instantiate a class with more than one metaclass')


# Generated at 2022-06-13 16:01:39.291951
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingleton1(object, metaclass=_ABCSingleton):
        @classmethod
        def SetClassMethod(cls, value):
            cls._class_method = value
        def SetMethod(self, value):
            self._method = value

    class _ABCSingleton2(object, metaclass=_ABCSingleton):
        def NotSetMethod(self, value):
            self._method2 = value

    _ABCSingleton1.SetClassMethod(1)
    _ABCSingleton1().SetMethod(2)

    if '_class_method' not in dir(_ABCSingleton1) or '_method' not in dir(_ABCSingleton1()):
        raise Exception('Test for _ABCSingleton1 failed')

    _ABCSingleton2().NotSetMethod(3)

# Generated at 2022-06-13 16:01:41.712434
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SomeClass(object):
        __metaclass__ = _ABCSingleton
    x = SomeClass()
    y = SomeClass()
    assert x is y

# Generated at 2022-06-13 16:01:46.296330
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        def __init__(self):
            super(Test, self).__init__()

    Test()

# Generated at 2022-06-13 16:01:48.208599
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Can't test without an options object
    try:
        g = GlobalCLIArgs.from_options(None)
        assert(False)
    except TypeError:
        assert(True)


# Generated at 2022-06-13 16:01:57.359565
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    a = {}
    a['verbosity'] = 0
    a['output_dir'] = '/var/tmp/test'
    a['private_key_file'] = '/var/tmp/test/private.pem'
    gca = GlobalCLIArgs({'verbosity': 0, 'private_key_file': '/var/tmp/test/private.pem'})
    assert isinstance(gca, collections.Mapping)
    b = gca.copy()
    assert isinstance(b, collections.Mapping)
    assert isinstance(gca, GlobalCLIArgs)
    assert b == a, "b should equal a"

# Generated at 2022-06-13 16:02:02.484372
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible import context
    context.CLIARGS = CLIArgs({})
    for arguments in ({}, {'foo': 'bar'}, {'foo': 'bar', 'baz': 'qux'}, {'foo': {'bar': 'baz'}, 'baz': 'qux'},
                      {'foo': (1, 2, 3), 'baz': 'qux'}, {'foo': {'bar': 'baz'}, 'baz': (1, 2, 3)}):
        assert CLIArgs(arguments) == arguments

# Generated at 2022-06-13 16:02:08.722875
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.common.text.converters import to_bytes
    global_vault = GlobalCLIArgs({u'vault_password_file': to_bytes('/file/path'),
                                  u'vault_password': to_bytes('password')})
    vault = VaultLib(**global_vault)
    vault_password = vault.decrypt('$ANSIBLE_VAULT;1.1;AES256;user\ndata\n')
    assert vault_password == b'password', "VaultLib did not use cli vault_password"

# Generated at 2022-06-13 16:02:14.299081
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class TestClass1(object):
        pass

    @add_metaclass(_ABCSingleton)
    class TestClass2(TestClass1):
        pass

    class TestClass3(TestClass2):
        pass

    assert issubclass(TestClass1, Singleton)
    assert issubclass(TestClass2, Singleton)
    assert issubclass(TestClass3, Singleton)

# Generated at 2022-06-13 16:02:25.146727
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # A dictionary
    mapping = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    result = CLIArgs(mapping)
    assert result == ImmutableDict(mapping)
    assert result is not ImmutableDict(mapping)

    # A dictionary of dictionaries
    mapping = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3',
               'key4': {'key5': 'value5', 'key6': 'value6'}}
    result = CLIArgs(mapping)
    assert result == ImmutableDict(mapping)
    assert result is not ImmutableDict(mapping)
    assert result['key4'] == ImmutableDict(mapping['key4'])

# Generated at 2022-06-13 16:02:31.255836
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test the CLIArgs class constructor"""
    # Test that when given an empty dictionary, we get an empty dictionary back
    empty = {}
    assert CLIArgs(empty) == empty

    # Test that when a dictionary is passed in, we get an ImmutableDict back
    immutable_dict = {'foo': 1, 'bar': 2}
    assert CLIArgs(immutable_dict) == immutable_dict

    # Test that when nested dictionarys are passed in, we get an ImmutableDict back
    nested_immutable_dict = {'foo': {'bar': 1}}
    assert CLIArgs(nested_immutable_dict) == nested_immutable_dict

    # Test that when a list is passed in, we get a tuple back
    immutable_list = [{'foo': 1}, 2]

# Generated at 2022-06-13 16:02:36.869039
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
    assert C() is not A()

# Generated at 2022-06-13 16:02:41.751458
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mutable_data = {'foo': 'bar', 'arr': ['a', 'b', 'c'], 'mapping': {'key': 'value'}}
    immutable_data = _make_immutable(mutable_data)
    args = CLIArgs(immutable_data)

    assert immutable_data == mutable_data
    assert immutable_data != args

# Generated at 2022-06-13 16:02:56.229260
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:02:57.864482
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(object):
        __metaclass__ = _ABCSingleton
        pass



# Generated at 2022-06-13 16:03:06.714588
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        """Expect this to be a singleton"""
        pass

    class C(A):
        # This is allowed because it is not a duplicate
        pass

    a = A()

    assert isinstance(a, A)
    assert isinstance(a, B)
    assert isinstance(a, C)

    # Test for immutability
    assert a.__init__ is A.__init__
    assert a.__new__ is A.__new__

    b = B()
    c = C()

    assert a is b is c


# Generated at 2022-06-13 16:03:14.388421
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs._GlobalCLIArgs__instance = None
    aa = GlobalCLIArgs({'a':{'b':2}})
    assert isinstance(aa, ImmutableDict)
    assert isinstance(aa, CLIArgs)
    assert isinstance(aa, GlobalCLIArgs)
    assert isinstance(aa, dict)
    assert isinstance(aa['a'], ImmutableDict)
    assert isinstance(aa['a'], dict)
    assert not isinstance(aa['a'], CLIArgs)
    assert not isinstance(aa['a'], GlobalCLIArgs)

# Generated at 2022-06-13 16:03:23.659620
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.release import __version__
    from ansible.config.manager import ConfigManager
    from ansible.cli import CLI
    from ansible.errors import AnsibleError

    config_manager = ConfigManager(['/dev/null'], '/dev/null')
    options = CLI.base_parser(config_manager, '/dev/null', runas_opts=True).parse_args([])
    cli_args = CLIArgs.from_options(options)
    assert cli_args[u'ansible_version'] == __version__
    cli_args[u'ansible_verbosity'] = 4
    assert cli_args[u'ansible_verbosity'] == 4


# Generated at 2022-06-13 16:03:26.206601
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingleton(object):
        __metaclass__ = _ABCSingleton
    assert type(ABCSingleton()) is ABCSingleton
    assert type(ABCSingleton()) is ABCSingleton
    assert type(ABCSingleton()) is ABCSingleton

# Generated at 2022-06-13 16:03:35.162491
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = {
        'one': 1,
        'two': 2,
        'three': {
            'four': 4,
            'five': 5,
            'six': [6]
        },
        'seven': {
            'eight': {
                'nine': 9,
                'ten': [10]
            }
        }
    }
    data = CLIArgs(data)
    assert(data['one'] == 1)
    assert(data['three']['five'] == 5)
    assert(data['seven']['eight']['ten'][0] == 10)

# Generated at 2022-06-13 16:03:39.284421
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Need to have a class that is not an error
    class MinimalClass(object):
        pass

    class MinimalClass1(MinimalClass, _ABCSingleton):
        pass

    class MinimalClass2(MinimalClass, _ABCSingleton):
        pass

    assert MinimalClass1() is MinimalClass1()
    assert MinimalClass2() is MinimalClass2()


# Generated at 2022-06-13 16:03:40.956320
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({'foo': {'bar': 123, 'baz': ['quux']}})

# Generated at 2022-06-13 16:03:50.861084
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test whether the constructor of class CLIArgs works as expected
    """

# Generated at 2022-06-13 16:04:03.636228
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs("fake_mapping")
    assert isinstance(global_cli_args, CLIArgs)

# Generated at 2022-06-13 16:04:05.557985
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Child(_ABCSingleton):
        pass
    class Child2(_ABCSingleton):
        pass
    assert Child() is Child()
    assert Child2() is Child2()
    assert Child() is not Child2()



# Generated at 2022-06-13 16:04:17.492189
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # singleton object
    cli_args_obj = GlobalCLIArgs.instance()
    cli_args_obj['foo'] = 'bar'
    cli_args_obj['baz'] = 'blah'
    cli_args_obj['baz']['boo'] = 'blah'
    cli_args_obj['baz']['boo']['bzz'] = 'blah'

    # immutable
    try:
        cli_args_obj['baz']['boo']['bzz'] = 'boom'
        assert False, "should have raised exception as cli args are immutable"
    except:
        pass

    # second singleton
    cli_args_obj2 = GlobalCLIArgs.instance()

# Generated at 2022-06-13 16:04:22.232378
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        assert issubclass(GlobalCLIArgs, CLIArgs)
        assert GlobalCLIArgs.__class__.__name__ == '_ABCSingleton'
    except AssertionError:
        raise AssertionError('_ABCSingleton did not properly combine ABCMeta with Singleton.')

# Generated at 2022-06-13 16:04:27.594346
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _Tester(_ABCSingleton):
        pass

    tester = _Tester()
    # Singleton construction should raise a TypeError since _Tester() is callable
    try:
        new_tester = _Tester()
    except TypeError:
        pass
    else:
        raise AssertionError("Expected a TypeError but got {0}".format(new_tester))


# Generated at 2022-06-13 16:04:31.163261
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_args = GlobalCLIArgs({})
    assert isinstance(global_args, GlobalCLIArgs)
    assert isinstance(global_args, CLIArgs)
    assert isinstance(global_args, ImmutableDict)

# Generated at 2022-06-13 16:04:32.762436
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCTest(_ABCSingleton):
        pass
    t = ABCTest()
    assert t is ABCTest()

# Generated at 2022-06-13 16:04:39.975892
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test CLIArgs with a dict of mixed data types
    """
    _input = {
        'a': 'a',
        'b': [1, 2, 3],
        'c': {
            'a': 'a',
            'b': [1, 2, 3],
            'c': {
                'a': 'a',
                'b': [1, 2, 3],
            },
        },
    }


# Generated at 2022-06-13 16:04:50.429467
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    a = GlobalCLIArgs({'key1':'val1', 'key2': 'val2'})

    assert a['key1'] == 'val1'
    assert a['key2'] == 'val2'

    try:
        a['key1'] = 'val2'
    except TypeError:
        assert True
    else:
        assert False, 'Should raise exception'

    try:
        a.update({'key1':'val2'})
    except TypeError:
        assert True
    else:
        assert False, 'Should raise exception'

    try:
        a.update({'key3':'val3'})
    except TypeError:
        assert False, 'Should not raise exception'
    else:
        assert True

# Generated at 2022-06-13 16:04:55.135509
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test class _ABCSingleton by using it as the metaclass for a class and by instantiating the class.
    Demonstrate that the class is a metaclass, a Singleton, and is ABCMeta based.

    The class should be hashable, iterable like a dict, and should support both dict-like and
    attribute-like access.
    """
    class _TestABCSingleton(_ABCSingleton):
        def __str__(self):
            return "__str__"
        def __repr__(self):
            return "__repr__"

    obj1 = _TestABCSingleton()
    obj2 = _TestABCSingleton()
    # Show that obj1 and obj2 are both instances of _TestABCSingleton and _ABCSingleton

# Generated at 2022-06-13 16:05:17.019914
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:05:24.099885
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Options(object):
        pass

    options = Options()
    options.foo=1
    options.bar=[1,2,3]
    options.baz={'a':1, 'b':2}
    my_args = CLIArgs.from_options(options)
    assert my_args == {'foo': 1, 'bar': (1, 2, 3), 'baz': ImmutableDict({'a': 1, 'b': 2})}

# Generated at 2022-06-13 16:05:25.326432
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(GlobalCLIArgs, CLIArgs)



# Generated at 2022-06-13 16:05:35.973528
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    d1 = {"a": "A", "b": "B", "c": "C"}
    d2 = {"a": "A", "b": "B", "d": {"e": ["f", "g"]}}
    d3 = {"a": "A", "b": "B", "d": {"e": {"f": "g", "h": ("1", "2")}}}
    d4 = {"a": "A", "b": "B", "d": {"e": {"f": {"g": "h", "i": ["1", "2"]}}}}

    cli_args1 = CLIArgs(d1)
    assert cli_args1 == {"a": "A", "b": "B", "c": "C"}

    cli_args2 = CLIArgs(d2)

# Generated at 2022-06-13 16:05:38.211085
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class Foo(object):
        __metaclass__ = _ABCSingleton

    assert issubclass(Foo, ABCMeta)

# Generated at 2022-06-13 16:05:45.726256
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class ABCSingletonSubclass(object):
        __metaclass__ = _ABCSingleton

    class ABCSingletonSubclass2(object):
        __metaclass__ = _ABCSingleton

    assert isinstance(ABCSingletonSubclass(), ABCSingletonSubclass)
    assert isinstance(ABCSingletonSubclass(), ABCSingletonSubclass2)
    assert isinstance(ABCSingletonSubclass2(), ABCSingletonSubclass)
    assert isinstance(ABCSingletonSubclass2(), ABCSingletonSubclass2)
    assert ABCSingletonSubclass() is ABCSingletonSubclass()
    assert ABCSingletonSubclass2() is ABCSingletonSubclass2()
    assert ABCSingletonSubclass() is ABCSingletonSubclass2()
    assert ABCSingletonSubclass() is not ABCSingletonSubclass2()



# Generated at 2022-06-13 16:05:54.671391
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLI_ARGS = CLIArgs({'foo': 'bar'})
    assert CLI_ARGS == {'foo': 'bar'}
    assert id(CLI_ARGS) != id({'foo': 'bar'})
    CLI_ARGS = CLIArgs(__file__='fake_filename')
    assert CLI_ARGS == {'__file__': 'fake_filename'}
    assert isinstance(CLI_ARGS, ImmutableDict)
    CLI_ARGS = CLIArgs({'foo': [{'bar': 'baz'}, {'bar': 'baz'}]})
    assert CLI_ARGS == {'foo': ({'bar': 'baz'}, {'bar': 'baz'})}
    assert isinstance(CLI_ARGS, ImmutableDict)
    CLI_ARGS = CLIArgs

# Generated at 2022-06-13 16:05:57.848674
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options:
        def __init__(self):
            self.dev = [
                "eth0",
                "eth1"
                ]

    GlobalCLIArgs.from_options(Options())

# Generated at 2022-06-13 16:06:00.086222
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyClass(metaclass=_ABCSingleton):
        pass

    # It should be possible to instantiate this class
    my_obj = MyClass()

# Generated at 2022-06-13 16:06:04.154668
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'foo': 'bar'})
    assert isinstance(args, CLIArgs)
    # it is not mutable
    try:
        args['foo'] = 'baz'
        raise AssertionError('should not be able to modify CLIArgs')
    except TypeError:
        pass
    assert args['foo'] == 'bar'

# Generated at 2022-06-13 16:06:49.673101
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'
    try:
        args['foo'] = 'blah'
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 16:06:53.106730
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestSingleton(_ABCSingleton):
        fixed_value = 'singleton'

    test_class = _TestSingleton()
    assert test_class.fixed_value == 'singleton', 'Failed to initialize test_class'

# Generated at 2022-06-13 16:06:56.729334
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    class C(B):
        pass

    a = A()
    b = B()
    c = C()

    assert a is b
    assert a is c

# Generated at 2022-06-13 16:06:59.001214
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class X(object, metaclass=_ABCSingleton):
        pass
    x1 = X()
    x2 = X()
    assert x1 is x2

# Generated at 2022-06-13 16:07:04.494584
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Ensure we can construct a Singleton
    # This feels like a lot of boilerplate for a singleton though.  Maybe we should have a helper for
    # that?
    class Test(GlobalCLIArgs):
        pass

    # pylint: disable=no-member
    # would have preferred `__new__` but not supported by Singleton
    instance1 = Test.__call__()  # pylint: disable=no-value-for-parameter
    instance2 = Test.__call__()  # pylint: disable=no-value-for-parameter
    assert instance1 is instance2



# Generated at 2022-06-13 16:07:09.661629
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Unit test will fail if we can't assign to self.args
    :return:
    """

    class TestArgs(GlobalCLIArgs):
        def __init__(self, args):
            self.args = args

    try:
        TestArgs({'foo': 'bar'})
    except Exception:
        assert False
    else:
        assert True

# Generated at 2022-06-13 16:07:13.447375
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class Stub_options:
        def __init__(self, mapping):
            self.__dict__ = mapping

    args = {'one': 'once', 'two': 'twice'}
    options = Stub_options(args)
    cli_args = CLIArgs.from_options(options)
    assert cli_args == args

# Generated at 2022-06-13 16:07:22.194668
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    d1 = GlobalCLIArgs({'a': 1, 'b': 2})
    d2 = GlobalCLIArgs({'a': 2, 'b': 3})
    assert d1 is not d2
    assert d1 == d2
    assert d1.a == d2.a == 2
    assert d1.b == d2.b == 3
    GlobalCLIArgs.clear_instance()
    d3 = GlobalCLIArgs({'a': 1, 'b': 2})
    assert d1 is not d3
    assert d1 == d3
    assert d1.a == d3.a == 1
    assert d1.b == d3.b == 2

# Generated at 2022-06-13 16:07:26.276826
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.facts.system.distribution import Distribution
    dist = Distribution()
    args = dist._parse_cli_facts()
    args.datetime = "2018-04-19T14:00:00Z"
    options = dist._get_options(args)
    parsed = CLIArgs.from_options(options)
    assert parsed.datetime == "2018-04-19T14:00:00Z"

# Generated at 2022-06-13 16:07:34.409097
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_data = {
        'a': 'b',
        'c': [
            'q',
            'w',
        ],
        'd': {
            '1': '2',
            '3': '4',
        },
    }
    # Note: a tuple object is returned in the place of a list object
    assertion = {
        'a': 'b',
        'c': ('q', 'w'),
        'd': {
            '1': '2',
            '3': '4',
        },
    }
    assert CLIArgs(test_data) == assertion

# Generated at 2022-06-13 16:09:14.673577
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Type conversions to test
    class TestObject(object):
        pass

    class TestObject2(object):
        pass

    class TestObject3(object):
        pass

    class TestObject4(object):
        pass

    # Container types to test
    test_dict = {'one': 1, 'two': 2, 'three': TestObject()}
    test_dict_with_obj = {'one': 1, 'two': TestObject(), 'three': TestObject2()}
    test_tuple = (1, 2, 3, TestObject())
    test_list = [1, 2, 3, TestObject()]
    test_set = {1, 2, 3, TestObject()}
    test_list_of_list = [[1, 2], [3, TestObject()]]

# Generated at 2022-06-13 16:09:16.451072
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class C(metaclass=_ABCSingleton):
        pass

# Generated at 2022-06-13 16:09:23.359415
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    import ansible.cli.arguments as cli_args


# Generated at 2022-06-13 16:09:31.719128
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # pylint: disable=protected-access
    data = {'foo': {'bar': 'baz'}, 'bee': 'boo'}
    x = CLIArgs(data)
    assert x._data == {'foo': {'bar': 'baz'}, 'bee': 'boo'}
    assert isinstance(x, ImmutableDict)
    assert isinstance(x, Mapping)
    assert not isinstance(x, Container)
    assert not isinstance(x, Sequence)
    assert not isinstance(x, Set)
    assert id(x) != id(data)
    assert isinstance(x['foo'], ImmutableDict)
    assert isinstance(x['foo'], Mapping)
    assert not isinstance(x['foo'], Container)