

# Generated at 2022-06-13 15:59:36.121792
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _TestClass(object, metaclass=_ABCSingleton):
        pass
    assert _TestClass is _TestClass()

# Generated at 2022-06-13 15:59:39.709930
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestClassA(object):
        __metaclass__ = _ABCSingleton

    class TestClassB(object):
        __metaclass__ = _ABCSingleton

    assert TestClassA() is TestClassA()
    assert TestClassB() is TestClassB()

# Generated at 2022-06-13 15:59:42.322391
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    @add_metaclass(_ABCSingleton)
    class SingletonSubclass(object):
        pass

    assert issubclass(SingletonSubclass, Singleton)
    assert issubclass(SingletonSubclass, ABCMeta)

# Generated at 2022-06-13 15:59:49.456428
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonClass(_ABCSingleton):
        pass

    class ABCClass(metaclass=ABCMeta):
        pass

    class SingletonABCClass(_ABCSingleton, ABCClass):
        pass

    assert issubclass(SingletonABCClass, ABCClass)
    assert issubclass(SingletonABCClass, SingletonClass)

    assert SingletonABCClass() is SingletonABCClass()
    assert SingletonABCClass().__class__ == SingletonABCClass


# Generated at 2022-06-13 16:00:00.818047
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:00:01.815622
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:00:10.611115
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    class MyCLIArgs(CLIArgs):
        def __init__(self, options):
            super(MyCLIArgs, self).__init__(vars(options))

    options = object()

    # MyCLIArgs is not a singleton so it will raise an exception if we try to create a new instance
    # when one already exists
    first = MyCLIArgs(options)
    try:
        raise AssertionError('Created more than one instance of non-singleton class')
    except TypeError:
        pass

    # If we try to create a new instance of an instance, this will raise an exception
    try:
        MyCLIArgs(first)
        raise AssertionError('Allowed creation of non-singleton class from instance')
    except TypeError:
        pass

    # If we try to create a new instance of

# Generated at 2022-06-13 16:00:15.312595
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_array = ['ansible', 'foo', '-vvvv']
    cli_args = CLIArgs.from_options(test_array)
    assert len(cli_args) == 2
    assert 'verbosity' in cli_args
    assert 'args' in cli_args

# Generated at 2022-06-13 16:00:21.957242
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils.common.collections import ImmutableDict
    import pytest

    # GlobalCLIArgs should have a from_options method:
    # success test
    test_dict = {'test_key': 'this is a test'}
    gcliargs = GlobalCLIArgs.from_options(test_dict)
    assert isinstance(gcliargs, ImmutableDict)

    # GlobalCLIArgs should still be an instance of ImmutableDict:
    # success test
    assert isinstance(GlobalCLIArgs._inst, ImmutableDict)

    # GlobalCLIArgs should be a singleton:
    # success test
    assert GlobalCLIArgs is GlobalCLIArgs._inst

    # GlobalCLIArgs should be a singleton and hence the same as the _inst attribute:
    # success test
    test

# Generated at 2022-06-13 16:00:29.356161
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections
    import types
    import copy
    import sys

    if sys.version_info[0] >= 3:
        builtin_string_tuple = (str,)
    else:
        builtin_string_tuple = (str, unicode)

    # test for text type tuple
    text_type_tuple = (str, bytes, collections.UserString)
    text_type_tuple_immutable = tuple(text_type_tuple)
    text_type_tuple_copy = copy.copy(text_type_tuple)
    text_type_tuple_mutable_copy = text_type_tuple_copy

    text_type_tuple_object = CLIArgs(dict(a=text_type_tuple_immutable))

# Generated at 2022-06-13 16:00:43.634673
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import types
    # mock_immutable_mapping_type is a mock class that can be used to replace the ImmutableDict class
    mock_immutable_mapping_type = type('ImmutableDict', (object,), {'__new__': lambda cls, *args, **kwargs: object.__new__(types.SimpleNamespace, *args, **kwargs)})
    # Save ImmutableDict class temporarily in _ImmutableDict and then assign a mock class to ImmutableDict
    _ImmutableDict = ImmutableDict
    ImmutableDict = mock_immutable_mapping_type
    # Instantiate the class GlobalCLIArgs by passing an empty mapping
    GlobalCLIArgs.from_options({})
    # Restore the mocked ImmutableDict class to the original ImmutableDict class
    ImmutableDict

# Generated at 2022-06-13 16:00:49.219764
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class MyABCSingleton(_ABCSingleton):
        pass

    first_instance = MyABCSingleton()
    second_instance = MyABCSingleton()

    if not hasattr(MyABCSingleton, '_instance'):
        raise Exception('Expected _instance to be set on MyABCSingleton')

    if first_instance is not second_instance:
        raise Exception('Expected first and second instances to be the same')

# Generated at 2022-06-13 16:00:51.539921
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(metaclass=_ABCSingleton):
        pass

    f1 = Foo()
    f2 = Foo()
    assert f1 is f2

# Generated at 2022-06-13 16:00:53.531463
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    foo = GlobalCLIArgs.from_options(None)
    assert foo is GlobalCLIArgs()

# Generated at 2022-06-13 16:01:04.434425
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    toplevel = {
        'one': 1,
        'two': '2',
        'three': 3.3,
        'four': ['a', 'b', 'c'],
        'five': ['apple', 'orange', 'banana'],
        'six': (1.1, 2.2, 3.3),
        'seven': ['one', 'two', 'three'],
        'eight': ('a', 'b', 'c'),
        'nested': {
            'one': ['a', 'b', 'c'],
            'two': ('a', 'b', 'c'),
        },
    }

# Generated at 2022-06-13 16:01:06.828261
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Temp(_ABCSingleton):
        pass
    Temp()

# Generated at 2022-06-13 16:01:14.742410
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass

    class Bar(_ABCSingleton):
        pass

    class Baz(_ABCSingleton):
        pass

    class Moo(Bar, Baz):
        pass

    class Zoo(Baz):
        pass

    class Zoo(_ABCSingleton):
        pass

    assert issubclass(Foo, _ABCSingleton)
    assert issubclass(Bar, _ABCSingleton)
    assert issubclass(Baz, _ABCSingleton)
    assert issubclass(Moo, _ABCSingleton)
    assert issubclass(Zoo, _ABCSingleton)

# Generated at 2022-06-13 16:01:19.109635
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options(object):
        from collections import namedtuple
        AnsibleOptions = namedtuple('AnsibleOptions', ['args'])
        ansible_options = AnsibleOptions(args=dict(
            debug=True,
            help=True,
            verbose=3
        ))

    global_cli_args = GlobalCLIArgs.from_options(Options())
    assert global_cli_args['debug']
    assert global_cli_args['help']
    assert global_cli_args['verbose'] == 3
    assert global_cli_args['args']

# Generated at 2022-06-13 16:01:22.950200
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Meta(object):
        __metaclass__ = _ABCSingleton
        pass

    class Obj(metaclass=Meta):
        def __init__(self):
            pass

    Obj()

# Generated at 2022-06-13 16:01:32.012986
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs({'a': 1, 'b': 2})
    assert obj['a'] == 1

    obj = GlobalCLIArgs({'a': '1', 'b': '2'})
    assert obj['a'] == '1'

    obj = GlobalCLIArgs({'a': '1', 'b': {'c': 3, 'd': '4'}})
    assert obj['b']['c'] == 3

    obj = GlobalCLIArgs({'a': '1', 'b': ['c', 'd']})
    assert obj['b'][0] == 'c'

    # Test that the above are all immutable
    obj = GlobalCLIArgs({'a': '1', 'b': ['c', 'd']})
    assert obj['b'] == ('c', 'd')

    obj = GlobalCL

# Generated at 2022-06-13 16:01:41.034341
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class A(object):
        __metaclass__ = _ABCSingleton

    assert isinstance(A(), A)
    assert isinstance(A(), Singleton)
    assert isinstance(A(), ABCMeta)

# Generated at 2022-06-13 16:01:49.456943
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    original_dict = dict(
        first_item='first_item',
        second_item=['second_item_1', 'second_item_2'],
        third_item=dict(
            third_item_1='value1',
            third_item_2='value2'
        )
    )

    cli_args = CLIArgs(original_dict)

    assert cli_args == original_dict
    assert isinstance(cli_args, ImmutableDict)
    assert isinstance(cli_args['second_item'], tuple)
    assert isinstance(cli_args['third_item'], ImmutableDict)
    assert isinstance(cli_args['third_item']['third_item_2'], text_type)

# Generated at 2022-06-13 16:02:00.128695
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import six
    import sys
    if six.PY2:
        if sys.version_info[1] == 5:
            # Skip this test because of Python 2.5
            return
    GA1 = GlobalCLIArgs({'foo': 'bar'})
    assert isinstance(GA1, CLIArgs)
    assert isinstance(GA1, ImmutableDict)
    assert isinstance(GA1, Mapping)
    assert isinstance(GA1, GlobalCLIArgs)
    assert isinstance(GA1, Singleton)
    assert isinstance(GA1, _ABCSingleton)

    # Make sure it is immutable
    def set_foo_baz():
        GA1['foo'] = 'baz'

# Generated at 2022-06-13 16:02:03.167381
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': ['b', 'c', 'd'], 'd': {'f': ['...']}}
    cli_args = CLIArgs(mapping)
    mapping['a'].append('e')
    assert cli_args != mapping


# Generated at 2022-06-13 16:02:04.820675
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        pass

    class Bar(Foo):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    f = Foo()
    b = Bar()

# Generated at 2022-06-13 16:02:07.522471
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs(ImmutableDict({'a': 1})) == GlobalCLIArgs(ImmutableDict({'a': 1}))

# Generated at 2022-06-13 16:02:09.120838
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # GlobalCLIArgs can be instantiated
    global_cli_args = GlobalCLIArgs({'a': 'A'})

# Generated at 2022-06-13 16:02:15.234861
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args_dict = {u'ignore-errors': False, u'force': False, u'user': None, 'private_key': None, u'private-key': None}
    args = CLIArgs(args_dict)
    assert isinstance(args, ImmutableDict)
    assert args[u'ignore-errors'] is False
    assert args[u'force'] is False
    assert args[u'user'] is None
    assert args[u'private_key'] is None
    assert args[u'private-key'] is None

# Generated at 2022-06-13 16:02:17.185591
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    assert issubclass(GlobalCLIArgs, CLIArgs)
    assert isinstance(GlobalCLIArgs._instance, GlobalCLIArgs)

# Generated at 2022-06-13 16:02:23.392707
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Unit test for _ABCSingleton

    This should not give a TypeError about multiple bases having instance lay-out conflict

    >>> class FooBar(object):
    ...     __metaclass__ = _ABCSingleton
    ...     def __init__(self):
    ...         self.test = True
    >>> x = FooBar()
    >>> assert x.test
    >>> y = FooBar()
    >>> assert x is y

    """
    pass

# Generated at 2022-06-13 16:02:29.672953
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class FakeArgs(object):
        foo = 'bar'
        baz = ['bat']

    g = GlobalCLIArgs.from_options(FakeArgs)
    assert g.foo == 'bar'
    assert g.baz == ('bat',)

    #make sure it can't be modified
    try:
        g.foo = 'bat'
    except TypeError:
        assert True
    else:
        assert False, "TypeError not raised on attempt to modify value."



# Generated at 2022-06-13 16:02:41.394215
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:02:46.754055
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'a': 1, 'b': '1', 'c': ['1', 1], 'd': {'1': '1'}, 'e': set('1'), 'f': frozenset('1')})
    assert isinstance(args, ImmutableDict)
    assert args == ImmutableDict({'a': 1, 'b': '1', 'c': (1, '1'), 'd': ImmutableDict({'1': '1'}), 'e': frozenset(('1',)), 'f': frozenset(('1',))})

    # test nested dict

# Generated at 2022-06-13 16:02:56.158894
# Unit test for constructor of class CLIArgs

# Generated at 2022-06-13 16:03:05.537189
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'key_one': 'hello', 'key_two': ['world', 'earth', 'mars']}

    args = CLIArgs(mapping)

    assert args['key_one'] == 'hello'
    assert args['key_two'] == ('world', 'earth', 'mars')

    def try_change_value(args):
        args['key_two'] = ['world', 'moon']

    def try_change_value_nested(args):
        args['key_two'][0] = 'moon'

    def try_delete(args):
        del args['key_two']

    def try_add(args):
        args['key_three'] = 'hello'

    # You cannot add to the dict

# Generated at 2022-06-13 16:03:15.967723
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class Options:
        keys = ['args', 'extra_vars', 'tags', 'skip_tags', 'inventory', 'inventory_vars',
                'inventory_vars_file', 'run_vars', 'extra_vars_file', 'module_vars']

        def __init__(self, mydict):
            for key in mydict:
                setattr(self, key, mydict[key])


# Generated at 2022-06-13 16:03:21.180538
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.basic import AnsibleModule

    temp_args = {
        'ANSIBLE_MODULE_ARGS': {
            'name': 'test_name',
            'state': 'test_state',
            'mode': 'test_mode',
            'properties': ('property1', 'property2')
        },
        'ANSIBLE_MODULE_CONSTANTS': {
            'test_constant': 'test_value'
        },
        'ANSIBLE_MODULE_KWARGS': {
            'test_kwarg': 'test_value'
        }
    }
    temp_args_list = [
        'test_arg'
    ]
    test_module = AnsibleModule(argument_spec=dict(
        test_arg=dict(required=False)
    ))
    test_module

# Generated at 2022-06-13 16:03:28.992295
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    immutables = [
        frozenset(),
        {},
        (),
        set(),
        '',
        b'',
        ImmutableDict()
    ]

    for immutable in immutables:
        cli_args = CLIArgs(immutable)
        assert cli_args == immutable

        mutables = [
            {'foo': []},
            set([['a', 'b']]),
            (1, 3, {'nested': {'mutable': None}}),
            [1, 3, {'nested': {'mutable': None}}],
            {'foo': ['a', 'b'], 'bar': set()},
            {'foo': ['a', 'b'], 'bar': {'nested_mapping': {}}},
        ]

# Generated at 2022-06-13 16:03:35.363914
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonABC(object):
        """
        Test that there is only one instance of this class
        """
        __metaclass__ = _ABCSingleton
        def __init__(self, arg1):
            self.arg1 = arg1

    first = SingletonABC('foo')
    second = SingletonABC('bar')
    assert first is second



# Generated at 2022-06-13 16:03:37.177803
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs({'foo': 'bar'}) is GlobalCLIArgs({'foo': 'bar'})

# Generated at 2022-06-13 16:03:44.549762
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # GlobalCLIArgs is a singleton, so we can't create one to test with
    # But we can create a very similar one that passes the same tests
    class MockGlobalCLIArgs(CLIArgs):
        pass

    global_cli_args = MockGlobalCLIArgs(dict(
        test_key_1="test_value_1",
        test_key_2="test_value_2",
    ))
    assert isinstance(global_cli_args, CLIArgs)
    assert isinstance(global_cli_args, GlobalCLIArgs)
    assert not isinstance(global_cli_args, ImmutableDict)
    assert isinstance(global_cli_args, Mapping)
    assert isinstance(global_cli_args, Container)

    assert 'test_key_1' in global_cli_args

# Generated at 2022-06-13 16:03:52.801602
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Single value
    expected_data = {
        'value': 'test',
    }
    args = CLIArgs(expected_data)
    assert args == expected_data

    # Multiple values
    expected_data = {
        'key1': 'value1',
        'key2': 'value2',
    }
    args = CLIArgs(expected_data)
    assert args == expected_data

    # Values of different types
    expected_data = {
        'key1': 'value1',
        'key2': True,
        'key3': 1,
    }
    args = CLIArgs(expected_data)
    assert args == expected_data

    # Empty dictionary
    expected_data = {}
    args = CLIArgs(expected_data)
    assert args == expected_data

    # Counting empty dictionary
    expected_

# Generated at 2022-06-13 16:03:57.995444
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("-a", action="store_true", dest="a", default=False)
    (options, args) = parser.parse_args(["-a"])
    args = GlobalCLIArgs(vars(options))
    assert args.get("a", "r") == True

# Generated at 2022-06-13 16:04:08.435270
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections
    import sys


# Generated at 2022-06-13 16:04:11.369660
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():

    class abc(metaclass=_ABCSingleton):
        pass

    a1 = abc()
    a2 = abc()
    assert a1 is a2

# Generated at 2022-06-13 16:04:15.125803
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    cmd_args = CLIArgs(test_dict)
    assert cmd_args == test_dict



# Generated at 2022-06-13 16:04:26.311492
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_mapping = {
        'abc': 123,
        'def': [456, 789, 112],
        'ghi': {'jkl': 567, 'mno': 890},
    }
    test_mapping['ghi']['pqr'] = test_mapping

    test_args = CLIArgs(test_mapping)

    assert test_args == test_mapping
    assert test_args['ghi'] == test_mapping['ghi']
    assert test_args['ghi']['jkl'] == test_mapping['ghi']['jkl']
    assert test_args['ghi']['pqr'] == test_mapping
    assert test_args['ghi']['pqr'] is not test_mapping


# Generated at 2022-06-13 16:04:34.337571
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        'a': {
            'b': [
                {
                    'c': [
                        12,
                        13
                    ]
                }
            ]
        },
        'd': {
            'e': 14,
            'f': 15
        }
    }

    ans = CLIArgs(test_dict)
    assert(isinstance(ans, ImmutableDict))
    assert(ans.a.b[0].c[0] == 12)
    assert(ans.a.b[0].c[1] == 13)
    assert(ans.d.e == 14)
    assert(ans.d.f == 15)

# Generated at 2022-06-13 16:04:37.853145
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Instantiate a subclass and ensure it's a singleton
    class _TestClass(_ABCSingleton):  # pylint: disable=no-member
        pass
    _TestClass()
    _TestClass()

# Generated at 2022-06-13 16:04:48.081284
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import io
    import optparse
    import sys
    from ansible.module_utils.six import StringIO

    # Create a list of command-line options to pass to optparse.OptionParser
    opt_list = [
        optparse.make_option('-t', '--some-test-option', dest='some_test_option'),
        optparse.make_option('-d', '--some-test-option-with-default', dest='some_test_option_with_default', default=1),
    ]

    # Create a parser for opt_list and add it to the list of known parsers
    parser = optparse.OptionParser(option_list=opt_list)

    # Set the name of the current parser as the default, as it would be when run by one of the
    # scripts in bin/ which import this module
    sys

# Generated at 2022-06-13 16:04:55.873561
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'a': 1, 'b': {'d': [1, 2, 3, 4]}, 'c': 'foo'}
    assert id(CLIArgs(test_dict)) != id(CLIArgs(test_dict))

# Generated at 2022-06-13 16:04:57.659213
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class fake(metaclass=_ABCSingleton):
        pass
    f1 = fake()
    f2 = fake()
    assert f1 is f2

# Generated at 2022-06-13 16:05:09.681052
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # pylint: disable=unused-argument
    def _mock_command_line(index):
        """Generate a fake command line"""
        return ['ansible-playbook', 'test.yml']

    def _mock_reproducible_options(index):
        """Generate a fake set of options"""

# Generated at 2022-06-13 16:05:19.647017
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Assert that we can mutate the dict without breaking the immutable dict.
    """
    # Create the dict
    args = {
        'b_opt': True,
        'c_opt': 'ccc',
        'd_opt': {
            'inner_d_opt': 'ddd'
            },
        'l_opt': [1, 2, 3],
        's_opt': set(['a', 'b', 'c']),
        }
    # Create the singleton
    global_cli_args = GlobalCLIArgs(args)
    # Assert that the singleton is properly immutable
    try:
        global_cli_args['b_opt'] = True
        assert False
    except TypeError:
        pass
    # Mutate the original dict
    args['b_opt'] = False
    #

# Generated at 2022-06-13 16:05:29.313340
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import doctest
    from ansible.module_utils.common import CLIArgs as CLIArgsBase

    class _MockCLIArgs(CLIArgsBase):
        def __init__(self, *args, **kwargs):
            super(_MockCLIArgs, self).__init__(*args, **kwargs)
            self.command = "test"
            self.this = "that"
            self.params = ["one", "two"]
            self.check = False
            self.diff = True

    # Need to pass empty module_args to doctest as they are normally
    # initialized by the module, which is what we are testing
    doctest.run_docstring_examples(_MockCLIArgs, globals(), name="CLIArgs", module_relative=False,
                                   module_args={})

# Generated at 2022-06-13 16:05:31.844712
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(object):
        __metaclass__ = _ABCSingleton

    f = Foo()
    assert(Foo() is f)

# Generated at 2022-06-13 16:05:39.418979
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    dictionary = {
        'foo': 'bar',
        'baz': {
            'one': 'two',
            'three': {
                'apple': 'banana',
                'cherry': 'date',
            }
        }
    }
    temp_args = GlobalCLIArgs(dictionary)
    assert temp_args['foo'] == 'bar'
    assert temp_args['baz']['three']['cherry'] == 'date'



# Generated at 2022-06-13 16:05:40.407585
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert(GlobalCLIArgs() is GlobalCLIArgs())


# Generated at 2022-06-13 16:05:49.434658
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:05:51.769144
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(_ABCSingleton):
        pass
    ts1 = TestABCSingleton.__new__(TestABCSingleton)
    ts2 = TestABCSingleton.__new__(TestABCSingleton)
    assert ts1 is ts2, '_ABCSingleton is not a Singleton'

# Generated at 2022-06-13 16:06:04.948056
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'a': 3})
    assert args['a'] == 3


# Generated at 2022-06-13 16:06:06.703343
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _ABCSingletonSubclass(GlobalCLIArgs):
        pass

# Generated at 2022-06-13 16:06:17.025600
# Unit test for constructor of class GlobalCLIArgs

# Generated at 2022-06-13 16:06:26.878963
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Ensure GlobalCLIArgs can be instantiated and its contents are immutable
    """
    import pytest
    from ansible.module_utils.basic import AnsibleModule

    # Make an AnsibleModule which is the source of the underlying immutable copy of cli arguments
    module_args = dict(
        an_argument=dict(a="A", b="B", c=dict(one=1, two=2, three=3)),
        another_argument=["1", "2", "3"],
        final_argument=True,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    args = module.params

    # Make a copy of cli arguments to pass to GlobalCLIArgs
    args_copy = dict()

# Generated at 2022-06-13 16:06:30.251057
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({"key1": "value1", "key2": "value2"})
    # We are testing that the above line doesn't raise an exception
    assert True

# Generated at 2022-06-13 16:06:40.480183
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys
    cwd = os.getcwd()
    # Test 1 - creating new instance for os.getcwd() changes
    assert(GlobalCLIArgs(vars(sys.argv)) == GlobalCLIArgs(sys.argv))
    os.chdir('..')
    # Test 2 - test1 failed as it seems there is no way to set sys.argv, but
    # we can use os.getcwd() to test
    assert(GlobalCLIArgs(os.getcwd()) == GlobalCLIArgs(os.getcwd()))
    os.chdir(cwd)
    # Test 3 - test2 failed as GlobalCLIArgs.__init__() calls super and ImmutableDict() caches
    # the value, so test3 failed

# Generated at 2022-06-13 16:06:46.819427
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class FakeOptions():
        foo = 0
        bar = None
        baz = []

    gargs = GlobalCLIArgs.from_options(FakeOptions())
    assert isinstance(gargs, GlobalCLIArgs)

    assert gargs['bar'] is None
    assert gargs['foo'] == 0
    assert isinstance(gargs['baz'], tuple) and gargs['baz'] == ()

# Generated at 2022-06-13 16:06:56.848269
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    dict1 = dict(a=1, b=2, c=3)
    dict2 = dict(x=4, y=dict(p=5, q=6), z=7)
    dict3 = dict(g=dict(x=8, h=9))

    # Test the basic case
    obj = _make_immutable(dict1)
    assert obj == ImmutableDict({'a': 1, 'b': 2, 'c': 3})

    # Test one level deep
    dict_temp = dict(a=1, b=2, c=3, d=dict(a=4, b=5, c=6))
    obj = _make_immutable(dict_temp)

# Generated at 2022-06-13 16:06:58.845259
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert isinstance(CLIArgs({1: 2}), ImmutableDict)

# Generated at 2022-06-13 16:07:03.866580
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Add a test that verifies that we can make a CLIArgs object with CLIArgs(dict())
    cli_args = CLIArgs(dict(foo=0, bar=dict(zed=1), baz=2))
    assert isinstance(cli_args, CLIArgs)


# Generated at 2022-06-13 16:07:26.124811
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Merely test that _ABCSingleton can be instantiated to avoid unexpected errors in future
    """
    test_abc_singleton = _ABCSingleton()
    assert isinstance(test_abc_singleton, _ABCSingleton)

# Generated at 2022-06-13 16:07:37.079560
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    assert CLIArgs({'a': 1}) == {'a': 1}
    assert CLIArgs({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert CLIArgs({'a': 1, 'b': [2]}) == {'a': 1, 'b': [2]}
    assert CLIArgs({'a': {1: 1}}) == {'a': {1: 1}}
    assert CLIArgs({'a': {1: {2: 3}}}) == {'a': {1: {2: 3}}}
    assert CLIArgs({'a': ({1: 1}, )}) == {'a': ({1: 1}, )}
    assert CLIArgs({'a': ({1: 1, 2: 2}, )}) == {'a': ({1: 1, 2: 2}, )}

# Generated at 2022-06-13 16:07:44.250979
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import pytest
    from collections import deque
    from ansible.module_utils.common.collections import MutableMapping

    args = CLIArgs(
        {
            'foo': 1,
            'dict': {'bar': 2, 'baz': 3},
            'list': [1, 2, 3],
            'set': set([1, 2, 3]),
            'frozenset': frozenset([1, 2, 3]),
            'deque': deque([1, 2, 3]),
            'tuple': (1, 2, 3),
            'bytes': b'abc',
            'str': 'abc',
        }
    )
    assert isinstance(args, Mapping)
    assert isinstance(args.keys(), Set)
    assert isinstance(args.values(), Sequence)

# Generated at 2022-06-13 16:07:47.907754
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLIArgs({'a': 1, 'b': [2, 3], 'c': {'d': 4, 'e': {'f': 5}}})

# Generated at 2022-06-13 16:07:54.441036
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    s=set()
    s.add('1')
    s.add('2')
    s.add('3')
    x = CLIArgs({'a':'10', 'b':'20', 'c':s})
    print(x)
    for xx in x.items():
        print(xx)
    print(x['a'])
    print(x['b'])
    print(x['c'])
    for v in x['c']:
        print(v)


# Generated at 2022-06-13 16:07:58.263212
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    d = GlobalCLIArgs({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d == d2

# Generated at 2022-06-13 16:08:04.523328
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    opts = {'opt1': 'value1', 'opt2': 'value2', 'opt3': 'value3'}
    result = CLIArgs(opts).copy()
    assert 'opt1' in result
    assert result['opt1'] == 'value1'
    assert 'opt2' in result
    assert result['opt2'] == 'value2'
    assert 'opt3' in result
    assert result['opt3'] == 'value3'


# Generated at 2022-06-13 16:08:06.081465
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    global_cli_args = GlobalCLIArgs({})
    assert isinstance(global_cli_args, GlobalCLIArgs)

# Generated at 2022-06-13 16:08:16.056566
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # test a correct case
    correct_args = {'name': 'test'}
    assert CLIArgs(correct_args) == ImmutableDict(correct_args)

    # test a nested case
    nested_args = {'name': 'test', 'nested': {'name': 'test'}}
    assert CLIArgs(nested_args) == ImmutableDict(nested_args)

    # test an item in list
    list_args = {'name': 'test', 'nested': [{'name': 'test'}]}
    assert CLIArgs(list_args) == ImmutableDict(list_args)

    # test an item in tuple
    tuple_args = {'name': 'test', 'nested': ({'name': 'test'},)}
    assert CLIArgs(tuple_args) == ImmutableDict

# Generated at 2022-06-13 16:08:25.733453
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.display import Display
    import inspect
    import sys
    from ansible.utils.hashing import checksum_s

    class_to_use = CLIArgs
    test_dict = {
        'display': Display(),
        'sys': sys,
        'inspect': inspect,
        'curious': 'value',
        'mutable': {'something': 'else'},
        'mutable_list': [1, 2, 3],
        'mutable_set': {'one', 'two', 'three'},
        'mutable_tuple': (1, '2', 3),
    }

    # Create a object of the class under test
    cli_args = class_to_use(test_dict)

    assert cli_args['curious'] == 'value'

    # Verify the objects in

# Generated at 2022-06-13 16:09:16.885142
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    """
    Verify that only one instance of GlobalCLIArgs exists in the system.
    If two instances are created then it will raise a RuntimeError.

    NOTE: If a RuntimeError is raised when running unittests then it means that a
    new instance of GlobalCLIArgs was created directly (cmdline.py) or indirectly
    while running unittests.
    """
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.errors import AnsibleError

    options = MockOptions

# Generated at 2022-06-13 16:09:18.281472
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    assert isinstance(A(), A)

# Generated at 2022-06-13 16:09:20.205741
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs({'foo': 'bar'})
    pass

# Generated at 2022-06-13 16:09:29.884882
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    from ansible.module_utils._text import to_bytes
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    name = 'ansible.module_utils.basic.GlobalCLIArgs'
    gargs = AnsibleCollectionLoader.load_collection_file(name)
    assert isinstance(gargs, CLIArgs)
    assert isinstance(gargs, GlobalCLIArgs)
    assert isinstance(gargs.get('connection'), to_bytes)
    assert isinstance(gargs.get('become_user'), to_bytes)
    assert gargs.get('check')
    assert gargs.get('diff')
    assert isinstance(gargs.get('extra_vars'), dict)
    assert isinstance(gargs.get('inventory'), dict)
    assert gargs.get('module_path')