

# Generated at 2022-06-13 15:59:37.928693
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()
    assert a is b
    assert a is c
    assert b is c

# Generated at 2022-06-13 15:59:49.504962
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': {'b': {'c': [1, 2, 3]}}}
    assert isinstance(mapping['a'], Mapping)
    assert isinstance(mapping['a']['b'], Mapping)
    assert isinstance(mapping['a']['b']['c'], Sequence)
    result = CLIArgs(mapping)
    assert isinstance(result, ImmutableDict)
    assert isinstance(result['a'], ImmutableDict)
    assert isinstance(result['a']['b'], ImmutableDict)
    assert isinstance(result['a']['b']['c'], tuple)

# Generated at 2022-06-13 16:00:00.859630
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonA(ImmutableDict):
        __metaclass__ = _ABCSingleton
        def __init__(self, foo):
            super(SingletonA, self).__init__()
            self.foo = foo

    class SingletonB(ImmutableDict):
        __metaclass__ = _ABCSingleton
        def __init__(self, bar):
            super(SingletonB, self).__init__()
            self.bar = bar

    for _ in range(0, 5):
        a = SingletonA("bar")
        assert hasattr(a, 'foo')

    for _ in range(0, 5):
        b = SingletonB("bar")
        assert hasattr(b, 'bar')

    a = SingletonA("foo")
    assert hasattr(a, 'foo')

    b

# Generated at 2022-06-13 16:00:02.317692
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(_ABCSingleton):
        pass

    assert A() is A()
    assert isinstance(A(), A)

# Generated at 2022-06-13 16:00:10.932442
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """Unit test for instantiation of class CLIArgs"""
    from ansible.module_utils._text import to_text
    from enum import Enum
    from io import BytesIO
    from pprint import pprint

    class MyEnum(Enum):
        """An example Enum for testing"""
        ENUM_1 = 1
        ENUM_2 = 2

    def my_callback_1(value):
        return to_text(value) + u' callback 1'

    def my_callback_2(value):
        return to_text(value) + u' callback 2'

    class MyClass(object):
        """An example class for testing"""
        def __init__(self, param=None):
            if param is None:
                param = {}
            self.param = param


# Generated at 2022-06-13 16:00:20.342944
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import collections

    test_dict = collections.OrderedDict()
    test_dict['test_key1'] = 'test'
    test_dict['test_key2'] = 100
    test_dict['test_key3'] = {'test_key': 'test'}

    global_cli_args = GlobalCLIArgs(test_dict)
    # test Immutable class
    assert global_cli_args == test_dict
    assert isinstance(global_cli_args, ImmutableDict)
    assert not isinstance(global_cli_args, dict)
    assert not isinstance(global_cli_args, Mapping)
    assert not isinstance(global_cli_args, Sequence)
    assert not isinstance(global_cli_args, Set)
    assert isinstance(global_cli_args, Container)

    # test Sing

# Generated at 2022-06-13 16:00:28.095122
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Given
    mapping = {
        'string': 'foobar',
        'list': ['1', '2', '3'],
        'dict': {
            'a': 'b',
            'c': 'd'
        }
    }

    # When
    args = CLIArgs(mapping)

    # Then
    assert isinstance(args, ImmutableDict)
    assert isinstance(args['string'], text_type)
    assert isinstance(args['list'], tuple)
    assert isinstance(args['dict'], ImmutableDict)

# Generated at 2022-06-13 16:00:32.039314
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    obj_dict = {'foo': {'baz': 'value'}, 'bar': ['value1', 'value2']}
    obj = CLIArgs(obj_dict)
    assert obj == obj_dict
    assert obj is not obj_dict
    assert obj['foo'] is not obj_dict['foo']
    assert obj['bar'] is not obj_dict['bar']

# Generated at 2022-06-13 16:00:42.466675
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        "param": "value",
        "only_one": "value",
        "list": ["value1", "value2", "value3"],
        "dict": {
            "subparam": "subvalue",
            "sublist": ["subvalue1", "subvalue2", "subvalue3"]
        }
    }
    test_obj = CLIArgs(test_dict)
    assert test_obj["param"] == "value"
    assert test_obj["only_one"] == "value"
    assert test_obj["list"] == ("value1", "value2", "value3")
    assert test_obj["dict"]["subparam"] == "subvalue"
    assert test_obj["dict"]["sublist"] == ("subvalue1", "subvalue2", "subvalue3")

# Generated at 2022-06-13 16:00:46.900602
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # test with a normal object
    try:
        instance = type.__call__(GlobalCLIArgs, {'a': 2})
    except TypeError:
        assert False
    else:
        assert True
    # test with another instance of GlobalCLIArgs
    try:
        instance = type.__call__(GlobalCLIArgs, GlobalCLIArgs())
    except TypeError:
        assert False
    else:
        assert True

# Generated at 2022-06-13 16:00:59.307518
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import time
    import random
    import json

    # Make random args
    args = {}
    for i in range(10):
        key = "key" + str(i)
        value = str(random.randint(0, 1000))
        args[key] = value

    # Make cli args object
    cli_args = CLIArgs(args)

    # Check to make sure its members are immutable
    for key, value in cli_args.items():
        with pytest.raises(TypeError):
            value += " test"

    # Check to make sure the cli args object itself is immutable
    with pytest.raises(TypeError):
        cli_args["test"] = "test"

# Generated at 2022-06-13 16:01:05.525394
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Verify that _ABCSingleton properly combines the methods of
    its parent classes.
    """
    class Foo(_ABCSingleton):
        def __init__(self, value):
            self.value = value
        def bar(self):
            return self.value
    # Make sure the class is called exactly once
    single1 = Foo('foo')
    single2 = Foo('bar')
    assert single1 is single2
    # Make sure the class has all of the methods from its parents
    assert single1.bar() == 'foo'

# Generated at 2022-06-13 16:01:11.586219
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    options = GlobalCLIArgs.from_options(ImmutableDict(a=1, b=2, c=3))
    # TODO: Test that options is immutable and the contents of options is immutable
    assert isinstance(options, ImmutableDict)
    assert options.a == 1
    assert options.b == 2
    assert options.c == 3



# Generated at 2022-06-13 16:01:13.631722
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'
    assert args.get('foo') == 'bar'
    assert args.get('bar') is None

# Generated at 2022-06-13 16:01:17.051208
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # pylint: disable=protected-access
    abc1 = _ABCSingleton('ABC1', (object,), {})
    abc2 = _ABCSingleton('ABC2', (object,), {})
    assert abc1 == abc2
    assert abc1 is abc2

# Generated at 2022-06-13 16:01:27.245083
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs.from_options(ImmutableDict(dict(a='b', c=dict(d='e'), f=list(['g', 'h', list(['i', 'j']), 'k']))))
    assert args['a'] == 'b'
    assert args['c']['d'] == 'e'
    assert args['f'] == ('g', 'h', ('i', 'j'), 'k')

    from collections import OrderedDict
    args = CLIArgs.from_options(OrderedDict(dict(a='b', c=dict(d='e'), f=list(['g', 'h', list(['i', 'j']), 'k']))))
    assert args['a'] == 'b'
    assert args['c']['d'] == 'e'

# Generated at 2022-06-13 16:01:31.042142
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Test class _ABCSingleton

    This is a unit test for class _ABCSingleton.
    """
    class A(metaclass=_ABCSingleton):
        pass
    class B(metaclass=_ABCSingleton):
        pass

    assert A() is A()
    assert B() is B()
    assert A() is not B()

# Generated at 2022-06-13 16:01:32.563527
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    pass

# Generated at 2022-06-13 16:01:38.712579
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs(dict(a=1, b=[1, 2, 3, dict(c=1)]))
    assert isinstance(args, Mapping)
    assert isinstance(args, ImmutableDict)
    assert isinstance(args, dict)
    assert not isinstance(args, GlobalCLIArgs)
    assert args["a"] == 1
    assert args["b"][3]["c"] == 1
    assert args["b"][3]["c"] == 1
    assert isinstance(args["b"], ImmutableDict)
    assert isinstance(args["b"], tuple)



# Generated at 2022-06-13 16:01:48.147670
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    try:
        from ansible.module_utils.common.collections import ImmutableDict as idict
    except ImportError:
        # This means that there is a problem with the import paths
        # Probably ansible is not checked out in the standard place
        # (with ansible source in the same directory as this file)
        # so we can not test.  It is better to ensure that all the
        # tests work, but at least we can make sure that this file
        # gets imported properly.
        return
    data = {
        'a': 'alpha',
        'b': {'ba': 'b alpha', 'bb': [1, 2, 3]},
        'c': [('d', {'da': 'd alpha', 'db': 'd beta'}), ('e', 5)],
        'e': 5,
    }


# Generated at 2022-06-13 16:01:57.114921
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {
        'a': 'A',
        'b': {
            'b1': 'B1',
            'b2': ['B2'],
            'b3': {
                'b31': ['B31']
            }
        },
        'c': ['C']
    }
    args = CLIArgs(test_dict)

    import json
    print(json.dumps(args, sort_keys=True, indent=4))

# Generated at 2022-06-13 16:02:02.156653
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import sys
    class Dummy(object):
        pass
    cmd_line_args = Dummy()
    cmd_line_args.foo = 'bar'
    old_args = sys.argv
    sys.argv = ['ansible-inventory', '--foo', 'bar']
    opt = GlobalCLIArgs.from_options(cmd_line_args)
    sys.argv = old_args
    assert opt['foo'] == 'bar'

# Generated at 2022-06-13 16:02:09.620772
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    class _FakeOptionValues(object):
        def __init__(self):
            self.example_string = "test"
            self.example_int = 10
            self.example_list = [1, 2, 3, 4, 5]

    options = _FakeOptionValues()
    args = GlobalCLIArgs.from_options(options)

    assert args["example_string"] == options.example_string
    assert args["example_int"] == options.example_int
    assert args["example_list"] == options.example_list

    assert isinstance(args["example_string"], text_type)
    assert isinstance(args["example_int"], int)
    assert isinstance(args["example_list"], tuple)


# Generated at 2022-06-13 16:02:15.123279
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    mapping = {
        'a': 1,
        'b': {
            'c': [1, 2, 3],
            'd': [
                {'f': 'g'},
                {'h': 'i'},
            ],
        },
    }

    args = GlobalCLIArgs(mapping)
    assert isinstance(args['b']['d'], tuple)
    assert isinstance(args['b']['d'][0], ImmutableDict)

# Generated at 2022-06-13 16:02:20.242608
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Foo(_ABCSingleton):
        pass

    class Foo1(Foo):
        pass

    class Foo2(Foo):
        pass

    f1 = Foo1()
    f2 = Foo1()
    assert f1 is f2

    with pytest.raises(TypeError):
        class Bar(Foo1, Foo2):
            pass

# Generated at 2022-06-13 16:02:21.900299
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    from ansible.module_utils.common.dummy.module_utils.module_common import ModuleCommon

    assert issubclass(ModuleCommon, _ABCSingleton)

# Generated at 2022-06-13 16:02:28.023314
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    import StringIO

    class Options(object):
        def __init__(self, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13, n=14, o=15, p=16, q=17, r=18, s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f
            self.g = g
            self.h = h
            self.i = i
            self.j = j


# Generated at 2022-06-13 16:02:30.867807
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    try:
        class Extender(_ABCSingleton):
            pass
    except TypeError:
        pass
    else:
        assert False, "Can't create a class with metaclass _ABCSingleton without it raising a TypeError"

# Generated at 2022-06-13 16:02:37.790695
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    mapping = {'a': 1, 'b': {'c': 2, 'd': {'e': 4}}, 'f': ['g', 'h']}
    args = CLIArgs(mapping)
    assert isinstance(args, ImmutableDict)
    assert isinstance(args['b'], ImmutableDict)
    assert isinstance(args['b']['d'], ImmutableDict)
    assert isinstance(args['f'], tuple)


# Generated at 2022-06-13 16:02:47.090824
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    test_dict = {'a': 1, 'b': 2, 'c': 'test', 'd': {'d1': 1, 'd2': 'test'},
                 'e': ['test', 'test2', 'test3'], 'f': [{'f1': 'test', 'f2': 1}]}
    cli = CLIArgs(test_dict)

    assert isinstance(cli, ImmutableDict)
    assert cli.a == 1
    assert cli.c == 'test'
    assert cli.d.d1 == 1
    assert cli.d.d2 == 'test'
    assert cli.e[0] == 'test'
    assert cli.e[1] == 'test2'
    assert cli.e[2] == 'test3'

# Generated at 2022-06-13 16:02:59.429613
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    data = {
        'a': [1, 2, {'b': 'c'}]
    }

    args = CLIArgs(data)

    assert isinstance(args, Container)
    assert isinstance(args, Mapping)
    assert not isinstance(args, Set)
    assert not isinstance(args, Sequence)

    assert isinstance(args['a'], Container)
    assert not isinstance(args['a'], Mapping)
    assert not isinstance(args['a'], Set)
    assert isinstance(args['a'], Sequence)

    assert isinstance(args['a'][0], int)
    assert args['a'][0] == 1

    assert isinstance(args['a'][1], int)
    assert args['a'][1] == 2


# Generated at 2022-06-13 16:03:00.748298
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # setup
    GlobalCLIArgs()
    # test
    GlobalCLIArgs()

# Generated at 2022-06-13 16:03:08.364788
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import tempfile
    _, test_yaml = tempfile.mkstemp(text=True)
    with open(test_yaml, 'w') as test_yaml_obj:
        test_yaml_obj.write('test: 42\n')

# Generated at 2022-06-13 16:03:14.644148
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils.common.args import AnsibleOptions
    options = AnsibleOptions()
    options.connection = 'local'
    options.private_key_file = 'myprivatekey'
    options.user = 'me'

    my_args = CLIArgs.from_options(options)
    assert my_args['connection'] == 'local'
    assert my_args['private_key_file'] == 'myprivatekey'
    assert my_args['user'] == 'me'


# Generated at 2022-06-13 16:03:23.828307
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    >>> import argparse
    >>> cli_args = argparse.Namespace(foo=argparse.Namespace(bar='buz'))
    >>> cli_args.foo.bar
    'buz'
    >>> args = CLIArgs.from_options(cli_args)
    >>> args
    {u'foo': {u'bar': u'buz'}}
    >>> args['foo']['bar']
    u'buz'
    >>> args['foo']['bar'] = 'new'
    Traceback (most recent call last):
        ...
    TypeError: ...
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:03:26.909069
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class TestABCSingleton(object):
        __metaclass__ = _ABCSingleton

    class TestABCSingleton2(object):
        __metaclass__ = _ABCSingleton

    assert TestABCSingleton() is TestABCSingleton()
    assert TestABCSingleton2() is TestABCSingleton2()



# Generated at 2022-06-13 16:03:34.655231
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class B(metaclass=_ABCSingleton):
        def __init__(self):
            self.b = 'hello'
    B1 = B()
    assert B1.b == 'hello'
    B2 = B()
    assert B1 is B2
    assert B1.b == B2.b
    B2.b = 'goodbye'
    assert B1.b == B2.b
    assert B1.b == 'goodbye'

# Generated at 2022-06-13 16:03:36.494278
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    assert GlobalCLIArgs({'foo': 'bar'}) == {'foo': 'bar'}


# Generated at 2022-06-13 16:03:44.532688
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test1(object):
        __metaclass__ = _ABCSingleton

    class Test2(Test1):
        pass

    class Test3(_ABCSingleton):
        pass

    class Test4(Test3):
        pass

    class Test5(Test1):
        pass

    class Test6(object):
        __metaclass__ = _ABCSingleton

    class Test7(Test6):
        pass

    # Hashable based Singletons
    instance1 = Test1()
    instance2 = Test2()
    instance3 = Test3()
    instance4 = Test4()
    instance5 = Test5()
    instance6 = Test6()
    instance7 = Test7()

    # Should return True
    assert instance1 is instance2
    assert instance1 is instance4
    assert instance1 is instance5
    assert instance

# Generated at 2022-06-13 16:03:45.415315
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLIArgs({'a': 1})



# Generated at 2022-06-13 16:04:02.279521
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.unsafe_proxy import UnsafeProxy

    test_mapping = {
        'foo': 1,
        'bar': 2,
        'baz': 3,
        'qux': {'a': 'abc', 'b': 'def'},
        'tzu': [1, 2, 3],
        'zoo': {'a': 1, 'b': 2, 'c': [1, 2, 3]},
    }

    args = CLIArgs(test_mapping)

    # Ensure that the class of the returned object is the same
    assert args.__class__ is CLIArgs

    # Ensure that the returned object is immutable
    try:
        args['foo'] = 4
    except (TypeError, AttributeError):
        pass
    else:
        assert False

    # Ensure that the object is still

# Generated at 2022-06-13 16:04:06.628972
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    """
    Test that CLIArgs correctly converts str, string, and dict to immutable.

    The original intention of this test was to test that CLIArgs correctly converts all non
    immutable types to immutable types but we were not able to test that.  We only added the test
    that the CLIArgs class is able to correctly convert dicts, lists, and strings.  We need to
    further investigate a way to test this.
    """
    import collections
    import types
    cli_args = CLIArgs({'a': 'string', 'b': {'d': 'string'},
                        'c': ['string', 'string']})
    assert isinstance(cli_args, collections.Container)
    assert not isinstance(cli_args, types.MutableMapping)

# Generated at 2022-06-13 16:04:18.036156
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.module_utils._text import to_text
    import sys
    sys.modules.pop('ansible.module_utils.common.cli.cliargs', None)  # avoids warning in cli.py
    from ansible.module_utils.common.cli import CLIArgs, GlobalCLIArgs
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext
    from ansible.utils import common
    import os
    import yaml
    test_string = "value_to_get_back"

# Generated at 2022-06-13 16:04:24.573832
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """ Unit test for constructor of class _ABCSingleton """

    class A(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    get_instance = A()

    class B(object):
        __metaclass__ = _ABCSingleton

        def __init__(self):
            pass

    get_instance2 = B()

    assert get_instance is get_instance2

# Generated at 2022-06-13 16:04:27.331045
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    GlobalCLIArgs(dict())
    GlobalCLIArgs.instance

# Generated at 2022-06-13 16:04:29.203366
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass



# Generated at 2022-06-13 16:04:35.382260
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Create a input data
    data = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': {
                'f': 4,
                'g': 5,
            },
        },
    }
    # Create a CLIArgs object using data
    args = CLIArgs(data)
    # Check the result
    assert args == data
    assert not isinstance(args, dict)
    assert not isinstance(args['c'], dict)

# Generated at 2022-06-13 16:04:41.289863
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(object):
        __metaclass__ = _ABCSingleton
    class B(A):
        pass
    class C(A):
        pass

    a1 = A()
    a2 = A()
    assert a1 is a2

    b1 = B()
    b2 = B()
    assert b1 is b2
    assert b1 is a1

    c1 = C()
    c2 = C()
    assert c1 is c2
    assert c1 is b1
    assert c1 is a1

# Generated at 2022-06-13 16:04:45.770641
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    string_value = 'string'
    mutable_value = [1, 2, 3]
    immutable_value = (1, 2, 3)
    original_values = {'string': string_value, 'mutable': mutable_value, 'immutable': immutable_value}
    args = CLIArgs(original_values)

    arg_values = vars(args)
    assert arg_values['mutable'] == immutable_value
    assert arg_values['immutable'] == immutable_value
    assert arg_values['string'] == string_value

# Generated at 2022-06-13 16:04:55.045772
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A(metaclass=_ABCSingleton):
        pass

    class B(A):
        pass

    class C:
        pass

    # We do not use isinstance here because importlib.abc.ABCMeta does not
    # correctly implement all of __subclasshook__ for some reason
    assert issubclass(B, A)

    # We should not be able to subclass an ABCMeta class
    assert not issubclass(A, C)

    # In fact, issubclass should fail with TypeError
    try:
        issubclass(A, C)
    except TypeError:
        pass
    else:
        assert False, "issubclass did not fail with TypeError"

# Generated at 2022-06-13 16:05:06.077480
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test(_ABCSingleton):
        pass
    assert isinstance(Test(), Test)

# Generated at 2022-06-13 16:05:09.819559
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # Create a new object of the class GlobalCLIArgs
    a = GlobalCLIArgs({'A': 'a', 'B': 'b'})

    assert isinstance(a, dict) is True
    assert a == {'A': 'a', 'B': 'b'}

# Generated at 2022-06-13 16:05:18.251514
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.vars import combine_vars

    temp_args = {'skip_tags': set(), 'extra_vars': [], 'tags': set()}

    temp_dict = {'skip_tags': ['foo', 'bar'], 'tags': ['baz']}

    temp_args['tags'].update(combine_vars(temp_dict)['tags'])
    temp_args['skip_tags'].update(combine_vars(temp_dict)['skip_tags'])

    # Sanity check that we really did mix the two data types
    assert isinstance(temp_args['skip_tags'], set), "The type of skip_tags was not a set"
    assert isinstance(temp_args['extra_vars'], list), "The type of extra_vars was not a list"


# Generated at 2022-06-13 16:05:21.615613
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    expected = {'foo': {'bar': 1, 'baz': 2}, 'qwer': (1, 2, 3)}
    actual = CLIArgs(expected)
    assert actual == expected
    assert actual.get('foo') is not expected.get('foo')
    assert actual.get('qwer') is not expected.get('qwer')


# Unit tests for function _make_immutable

# Generated at 2022-06-13 16:05:31.002085
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import os
    import sys
    import tempfile

    # This is the weird part where we monkey patch the module so we can call super() because
    # Singleton doesn't work that way when unit-testing
    sys.modules['ansible.module_utils.common.global_cli_args'] = __import__(__name__)
    from ansible.module_utils.common import global_cli_args

    import ansible.module_utils.common.global_cli_args as gca

    # Create a fake CLIArgs object using the CLIArgs constructor
    test_mapping = {
        'start_at_task': 'foo',
        'tags': frozenset({'bar', 'baz'})
    }
    test_fake_cl_args = global_cli_args.CLIArgs(test_mapping)

    # Create the arguments

# Generated at 2022-06-13 16:05:41.083452
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    # The goal is to make sure the constructor works, which requires
    # any object of class GlobalCLIArgs to be a singleton object,
    # so we cannot create it directly.  Instead, we trigger the
    # creation of the singleton and then get access to the instance.
    GlobalCLIArgs.instance('dummy')
    cli_args = GlobalCLIArgs.get_instance()

    # cli_args will be an instance of GlobalCLIArgs and of ImmutableDict
    assert isinstance(cli_args, (GlobalCLIArgs, ImmutableDict))

    # Confirm that the arguments are not mutable

# Generated at 2022-06-13 16:05:44.046214
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    obj = GlobalCLIArgs({'a': 1, 'b': 2, 'c': {'x': 300}})
    assert obj['a'] == 1
    assert obj['c'] is not None
    assert obj['c']['x'] == 300



# Generated at 2022-06-13 16:05:49.775504
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import collections

    # Empty dict should be possible
    _ = CLIArgs({})
    _ = CLIArgs(dict())
    _ = CLIArgs(collections.OrderedDict())

    # Only allow immutable types
    immutable_dict = ImmutableDict({})
    immutable_list = tuple()
    immutable_set = frozenset()
    _ = CLIArgs({'dict': immutable_dict, 'list': immutable_list, 'set': immutable_set})

    # Immutable data types should not be allowed
    _ = CLIArgs({'dict': {}, 'list': [], 'set': set()})

# Generated at 2022-06-13 16:05:52.453422
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    instance = GlobalCLIArgs({'key1': 'value1', 'key2': 'value2'})
    assert instance == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2022-06-13 16:05:59.654677
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class _test__ABCSingleton1(object):
        __metaclass__ = _ABCSingleton
    class _test__ABCSingleton2(object):
        __metaclass__ = _ABCSingleton
    assert _test__ABCSingleton1() is _test__ABCSingleton2()
    assert isinstance(_test__ABCSingleton1(), _test__ABCSingleton2)
    assert isinstance(_test__ABCSingleton2(), _test__ABCSingleton1)



# Generated at 2022-06-13 16:06:21.492143
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class Test1(object):
        __metaclass__ = _ABCSingleton

    class Test2(object):
        __metaclass__ = _ABCSingleton

    assert Test1() is Test2()

# Generated at 2022-06-13 16:06:23.547783
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    args = GlobalCLIArgs({'foo': 'bar'})
    assert args['foo'] == 'bar'

# Generated at 2022-06-13 16:06:34.981045
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    Make sure that the metaclass for Singleton and ABCMeta based classes works as expected
    """
    class AbstractSingletonClassABCMeta(object):
        """
        The base class for this test.

        We must define this as a class so that Metaclass can read it as a class and that we can override abstract
        methods on this class.  If we did not do this then Metaclass would be a module and we would not be able to
        create our own class that inherits from Metaclass and override abstract methods.
        """
        __metaclass__ = _ABCSingleton

        @property
        def abstract_method(self):
            raise NotImplementedError("You must implement this abstract method.")


# Generated at 2022-06-13 16:06:38.744269
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonTestCls(object):
        __metaclass__ = _ABCSingleton
    cls1 = SingletonTestCls()
    cls2 = SingletonTestCls()
    assert id(cls1) == id(cls2)

# Generated at 2022-06-13 16:06:45.362800
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import unittest

    class TestCLIAguments(unittest.TestCase):
        def setUp(self):
            self.data = {'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']}

        def test_constructor(self):
            cli_args = CLIArgs.from_options(self.data)
            self.assertEqual(type(cli_args), CLIArgs)
            self.assertEqual(cli_args['numbers'], (1, 2, 3))
            self.assertEqual(cli_args['letters'], ('a', 'b', 'c'))

    unittest.main()

# Generated at 2022-06-13 16:06:55.104710
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    """
    This function serves as the unit test for class `_ABCSingleton`.
    Ideally this should be in a separate file in test directory, but
    we must write the unit test in the same module as the class so
    that it is executed as part of `python -m unittest ...`

    This test is equivalent to:
    >>> class A:
    ...     @add_metaclass(_ABCSingleton)
    ...     class B:
    ...         def __init__(self, value):
    ...             self.value = value
    ...         def __str__(self):
    ...             return self.value
    ...
    >>> A.B("abc")
    Traceback (most recent call last):
    ...
    abc
    """


# Generated at 2022-06-13 16:07:00.292567
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--verbose", action="store_true", help="increase verbosity", default=False)
    parser.add_option("--playbook-dir", default=None)
    (options, _) = parser.parse_args()
    GlobalCLIArgs(vars(options))


if __name__ == '__main__':
    test_GlobalCLIArgs()

# Generated at 2022-06-13 16:07:11.504235
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import datetime
    import pytz
    from collections import MutableMapping

    def _dont_call_me():
        return True

    def _also_not_me(a,b='c'):
        return False

    now = datetime.datetime.now(pytz.utc)
    test_dict = {'a': 'b',
                 'c': ['d', 'e', 'f'],
                 'g': {'h': 'i', 'j': 'k', 'l': [1, 2, 3]},
                 'm': {'n', 'o', 'p'},
                 'q': now,
                 'r': _dont_call_me,
                 's': _also_not_me}

    # Test that we can't mutate the resulting object
    cli_args = CLIArgs

# Generated at 2022-06-13 16:07:15.601622
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    from ansible.utils.collection_plugins.test_utils import TestImmutableDict
    TestImmutableDict.test_immutabledict(CLIArgs)

    # The class method from_options is used by AnsibleCLI to create the GlobalCLIArgs singleton
    # instance.  We do not test that here because the from_options implementation is dependent on
    # whether argparse is used to parse the command line options, so we can only test it in the
    # unit test for AnsibleCLI.

# Generated at 2022-06-13 16:07:21.508382
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class FooSingleton(object, metaclass=_ABCSingleton):
        pass

    class BarSingleton(object):
        __metaclass__ = _ABCSingleton

    class BazSingleton(object, metaclass=_ABCSingleton):
        __metaclass__ = _ABCSingleton

    class QuxSingleton(object):
        __metaclass__ = _ABCSingleton
        __metaclass__ = _ABCSingleton

# Generated at 2022-06-13 16:08:06.555561
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test that we correctly de-nest mutable data types into immutable data types
    mutable = {'a': {'b': 1}, 'c': set([{'d': 2}])}
    immutable = CLIArgs({'mutable': mutable})['mutable']
    assert isinstance(immutable, ImmutableDict)
    assert isinstance(immutable['a'], ImmutableDict)
    assert isinstance(immutable['c'], frozenset)
    assert isinstance(immutable['c'].pop(), ImmutableDict)


# Test that we create the singleton's class instance

# Generated at 2022-06-13 16:08:09.244801
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    # Define a class that subclasses both Singleton and ABCMeta
    class Foo(_ABCSingleton):
        pass
    global_foo = Foo()
    local_foo = Foo()
    assert global_foo is local_foo

# Generated at 2022-06-13 16:08:19.558820
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    import sys
    sys.argv.append("-vvvv")
    sys.argv.append("--check")
    sys.argv.append("--diff")
    sys.argv.append("--connection=local")
    sys.argv.append("--inventory-file=./my_inventory_file")
    sys.argv.append("--module-path=./my_module_path")
    sys.argv.append("--tags=my_tags")
    sys.argv.append("--skip-tags=my_skip_tags")
    sys.argv.append("--start-at-task=my_start_at_task")
    sys.argv.append("--extra-vars='username=tom'")
    sys.argv.append("--extra-vars='password=secret'")


# Generated at 2022-06-13 16:08:29.080865
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    with open('/tmp/test_json', 'w') as f:
        f.write('''
 {
   "one": 2,
   "three": [ 1, 2, 3, 4, 5 ],
   "six": {
     "six_inner": 6
   }
 }''')

    # This tests the ability to clone an existing dict
    conf = dict(one=1, two=2, three=3)
    conf2 = dict(conf)
    assert conf == conf2

    # This tests the ability to clone an existing dict (a better way)
    conf3 = dict(conf)
    assert conf == conf3

    # This tests the ability to clone a dict from a dict-like object
    conf4 = dict(conf)
    assert conf == conf4

    # This tests the ability to clone a dict from a dict-like

# Generated at 2022-06-13 16:08:32.202381
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    CLIArgs({'key1': 'value1',
             'key2': ['value2', 'value22', {'key3': 'value3'}],
             'key4': {'key5': 'value5'},
             })

# Generated at 2022-06-13 16:08:39.424498
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    # Test empty dict
    test_dict = {}
    dict_to_instantiate = CLIArgs(test_dict)
    assert not dict_to_instantiate
    assert isinstance(dict_to_instantiate, ImmutableDict)

    # Test dict with two elements
    test_dict = {"one": 1, "two": 2}
    dict_to_instantiate = CLIArgs(test_dict)
    assert isinstance(dict_to_instantiate, ImmutableDict)
    assert dict_to_instantiate.get("one") == 1
    assert dict_to_instantiate.get("two") == 2
    assert isinstance(dict_to_instantiate.get("one"), int)
    assert isinstance(dict_to_instantiate.get("two"), int)

    # Test dict with

# Generated at 2022-06-13 16:08:44.668255
# Unit test for constructor of class GlobalCLIArgs
def test_GlobalCLIArgs():
    import pytest
    from ansible.cli.arguments import optparse_helpers

    helpers = optparse_helpers()
    parser, options, args = helpers.parser.parse_args()

    cli_args = GlobalCLIArgs.from_options(options)
    assert cli_args['connection'] == 'smart'
    assert cli_args['remote_user'] == 'root'
    assert cli_args['remote_pass'] is None
    assert cli_args['private_key_file'] == '/root/.ssh/id_rsa'

    # Test root-level container is immutable
    with pytest.raises(TypeError):
        cli_args['connection'] = 'hello'

    cli_args2 = GlobalCLIArgs.from_options(options)
    cli_args3 = GlobalCLIArgs

# Generated at 2022-06-13 16:08:51.612550
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class SingletonMetaclass(metaclass=_ABCSingleton):
        pass
    class NonSingletonMetaclass(metaclass=_ABCSingleton):
        __metaclass__ = ABCMeta
    try:
        class SingletonAndNonSingletonMetaclass(metaclass=_ABCSingleton):
            # This class should never be defined
            __metaclass__ = SingletonMetaclass
    except TypeError:
        pass

# Generated at 2022-06-13 16:08:58.338795
# Unit test for constructor of class CLIArgs
def test_CLIArgs():
    args = CLIArgs({'a':5, 'b':['c','d','e','f'], 'g':{'h':7, 'i':10}})
    assert args == {'a':5, 'b':('c', 'd', 'e', 'f'), 'g':{'h':7, 'i':10}}
    assert args['g']['h'] == 7
    assert not isinstance(args, GlobalCLIArgs)


# Generated at 2022-06-13 16:09:03.722623
# Unit test for constructor of class _ABCSingleton
def test__ABCSingleton():
    class A1(object):
        __metaclass__ = _ABCSingleton
    class A2(object):
        __metaclass__ = _ABCSingleton
    assert A1 is A2
    assert issubclass(A1, object)
    assert issubclass(A2, object)
    assert issubclass(A1, A2)
    assert issubclass(A2, A1)
    assert isinstance(A1(), A2)
    assert isinstance(A2(), A1)