

# Generated at 2022-06-12 19:58:46.513093
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # instance created with default parameters
    variable_a = BaseVariable('a')
    assert variable_a == variable_a
    assert not variable_a != variable_a
    # instance created with default parameters
    variable_a_same = BaseVariable('a')
    assert variable_a == variable_a_same
    # instance created with default parameters
    variable_a_diff = BaseVariable('a', exclude = ('a',))
    assert variable_a != variable_a_diff


# Generated at 2022-06-12 19:58:48.118703
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    Indices("", [4,5]).__getitem__(slice(1,4))._slice == slice(1,4)

# Generated at 2022-06-12 19:58:51.624017
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    m_own = BaseVariable('a')
    assert not m_own.__eq__(BaseVariable('b'))
    assert not m_own.__eq__(BaseVariable('a', 1))
    assert m_own.__eq__(BaseVariable('a'))


# Generated at 2022-06-12 19:59:02.024077
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    d = {'a': '100'}
    l = ['100']
    class A:
        a = '100'
    a = A()
    class B:
        def __init__(self):
            self.a = '100'
    b = B()
    frame = utils.Frame(d, l, a, b)
    results = {}
    results['a'] = [('a', '"100"')]
    results['a.a'] = [('a.a', '"100"')]
    results['l[0]'] = [('l[0]', '"100"')]
    #results['a[0]'] = [('a[0]', '"100"')]
    results['a.a'] = [('a.a', '"100"')]
    #results['b

# Generated at 2022-06-12 19:59:11.133283
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Example 1:
    # create variables
    variable1 = BaseVariable('arg1')
    variable2 = BaseVariable('arg1')
    variable3 = BaseVariable('arg3')
    # test
    assert variable1 == variable2
    assert variable1 != variable3

    # Example 2:
    # create variables
    variable1 = BaseVariable('arg1', exclude=['key1'])
    variable2 = BaseVariable('arg1', exclude=['key1'])
    variable3 = BaseVariable('arg1', exclude=['key3'])
    variable4 = BaseVariable('arg1')
    # test
    assert variable1 == variable2
    assert variable1 != variable3
    assert variable1 != variable4


# Generated at 2022-06-12 19:59:22.924186
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys

    class TestClass:
        pass

    tc = TestClass()
    tc.att1 = 'att1'
    setattr(tc, 'att2', 'att2')
    tc.__dict__['att3'] = 'att3'
    tc._att4 = 'att4'
    tc._att5 = 'att5'
    tc.__slots__ = ['_att6', '_att7']
    tc._att6 = 'att6'
    tc._att7 = 'att7'

    frame = sys._getframe()
    attrs = Attrs('tc')

# Generated at 2022-06-12 19:59:31.292972
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types
    import array
    import math

    def as_tuple(inner_list):
        return tuple(tuple(inner_list))

    def check_items(v, normalize, expected):
        v.code = compile(v.source, '<variable>', 'eval')
        result = v.items(sys._getframe(), normalize=normalize)
        assert as_tuple(result) == as_tuple(expected)

    f = sys._getframe()

# Generated at 2022-06-12 19:59:38.011949
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    foo = inspect.currentframe().f_back
    foo2 = foo.f_back
    vr = BaseVariable('self', ('foo','foo2','self'))
    myclass = vr.__class__
    assert myclass == 'BaseVariable'
    result = vr.items(foo)
    #assert result == ([('self', '<frame object at 0x7fa47dddcdc0>')],)
    #assert result == ([('self', '<frame object>')],)
    assert result == ([('self', 'foo')],)

# Generated at 2022-06-12 19:59:49.097049
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from . import utils
    import sys
    import os
    import traceback
    import linecache
    import unittest

    def get_line(lineno=None):
        return linecache.getline(__file__, lineno)

    def get_traceback(lineno=None):
        lineno = lineno or sys._getframe().f_lineno + 1
        return traceback.extract_tb(sys.exc_info()[2])[-1]

    def get_frame(lineno=None):
        lineno = lineno or sys._getframe().f_lineno + 1
        frame = sys._getframe()
        while frame.f_lineno != lineno:
            frame = frame.f_back
        return frame


# Generated at 2022-06-12 19:59:57.355602
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert(BaseVariable("Hello") == BaseVariable("Hello"))
    assert(BaseVariable("Hello") == BaseVariable("Hello", exclude=['World']))
    assert(BaseVariable("Hello", exclude=['World']) == BaseVariable("Hello", exclude=['World']))
    assert(not (BaseVariable("Hello") == BaseVariable("", exclude=['World'])))
    assert(not (BaseVariable("Hello") == BaseVariable("Hello", exclude=['World'])))
    assert(not (BaseVariable("") == BaseVariable("Hello", exclude=['World'])))

# Generated at 2022-06-12 20:00:10.564179
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # assert x in [1, 2, 3]
    def check_items(variable_cls):
        class A(object):
            def __init__(self, b):
                self.y = b

        a = A(1)
        a.x = 4
        a.z = a

        for normalize in [False, True]:
            for frame in [{}, {'a': a}]:
                for want_items in [[('x', '4'), ('y', '1'), ('z', '<A>'), ('<globals>.a', '<A>')],
                                   [('x', '4'), ('y', '1'), ('z', '<A>')]]:
                    # want_items must be in result namedtuple
                    result = tuple(variable_cls('a').items(frame, normalize))


# Generated at 2022-06-12 20:00:19.860784
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Testing for Attrs
    l1 = dict(a="a str", b={"b key": "b-value"}, c=["a tuple"], d=3, e=["a list"])
    l2 = ["a list", "a list", {"a list-dict": "a list-dict-value"}, {"a list-dict-2": "a list-dict-2-value"}]
    l3 = {"a dict": "a dict-value", "a dict-2": "a dict-2-value"}
    l4 = "a string"
    l5 = [(1, 2), (3, 4), (5, 6)]
    l6 = set((1, 2, 3))
    # create a variable "l1"
    frame = MagicMock()

# Generated at 2022-06-12 20:00:22.441501
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('test')
    var2 = BaseVariable('test')

    assert(var1 == var2)


# Generated at 2022-06-12 20:00:25.945421
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """
    Test method __eq__ of class BaseVariable
    """
    var1 = BaseVariable('request')
    var2 = BaseVariable('request')
    assert var1 == var2
    

# Generated at 2022-06-12 20:00:35.337625
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pprint
    import sys
    import traceback
    from os import path

    class Variable(BaseVariable):
        def _items(self, key, normalize=False):
            return (("a", "1234"), ("b", "4321"))

    def get_test_frame():

        def test():
            def _test():
                raise

            _test()

        try:
            test()
        except:
            return sys.exc_info()[2].tb_frame.f_back

    # test items with normalize=False
    result = Variable('test').items(get_test_frame())
    assert result == (('a', '1234'), ('b', '4321'))

    # test items with normalize=True
    result = Variable('test').items(get_test_frame(), normalize=True)


# Generated at 2022-06-12 20:00:40.774677
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    s = 'x'
    var1 = BaseVariable(s)
    var2 = BaseVariable(s)
    var3 = BaseVariable(s, ['y'])
    assert var1 == var2
    assert var1 == var3
    assert var1.__eq__('x') is False


# Generated at 2022-06-12 20:00:43.957023
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from copy import deepcopy
    Index = Indices("A")
    Idx_slice = Index[:]
    assert type(Idx_slice) == Indices, "Error in class Indices method __getitem__"

# Generated at 2022-06-12 20:00:48.546815
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    obj = BaseVariable
    x = BaseVariable('x')
    y = BaseVariable('y')
    assert not x.__eq__(obj.__eq__)
    assert not x.__eq__(y)
    assert not x.__eq__('x')
    assert x.__eq__(x)


# Generated at 2022-06-12 20:00:59.987483
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import StringIO
    import sys
    import unittest

    # Input
    locals_ = {'z': 'z', 'x': 'x'}

    # Code for testing
    frame = inspect.currentframe()

    # Expected output
    expected_results = [('x', "'x'"), ('z', "'z'")]

    # Test
    def test_frame(frame):
        from .cframevar import Variables, Variable
        variables = Variables(frame, tuple(), 0)
        results = []
        for variable in variables:
            for key, value in variable.items(frame):
                results.append(key, value)
        self.assertEqual(results, expected_results)

    class FrameTester(unittest.TestCase):
        def test_trivial(self):
            test

# Generated at 2022-06-12 20:01:07.453235
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import format_frame
    frame = format_frame('test_frame', {})
    frame.f_locals['a'] = 'a'
    l = [1, 2, 3]
    frame.f_locals['l'] = l
    d = {'1': 1, '2': 2}
    frame.f_locals['d'] = d
    class C(object):
        def __init__(self):
            self.a = 1
    frame.f_locals['C'] = C 
    c = C()
    frame.f_locals['c'] = c
    assert BaseVariable('a').items(frame) == [('a', 'a')]

# Generated at 2022-06-12 20:01:20.717925
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .frames import Frame
    from . import exec_function_source

    # Test for a base variable
    frame, _, _ = exec_function_source('frame_for_BaseVariable_items_abs')
    abs_lib = BaseVariable(source='abs')
    assert [('abs', '<built-in function abs>')] == abs_lib.items(frame)

    # Test for a variable with its own attributes and keys
    frame, _, _ = exec_function_source('frame_for_BaseVariable_items_x')
    x = BaseVariable(source='x')
    # Test for a variable with its own attributes and keys
    assert [('x', '42'), ('x.z', '42'), ('x.a', '"abc"')] == x.items(frame)
    # Test for a variable with its own attributes, keys

# Generated at 2022-06-12 20:01:30.595994
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'x'
    exclude = ()
    code = compile(source, '<variable>', 'eval')
    v = BaseVariable(source, exclude)
    # check 11 attributes
    assert v.source == source
    assert v.exclude == exclude
    assert v.code == code
    # check if needs parentheses
    assert needs_parentheses(source) == True
    assert needs_parentheses('()') == False
    assert v.unambiguous_source == '({})'.format(source)
    # set default key and value
    frame = {'x': 1}
    key = 'x'
    value = 1
    # check if it returns the right value
    assert v.items(frame) == [(source, utils.get_shortish_repr(value))]
    # check if it returns the right value with a different

# Generated at 2022-06-12 20:01:31.396336
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:01:37.783840
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import threading
    import traceback

    def run_test(cls, var, expected):
        print(cls.__name__, 'object:', var)
        var_obj = cls(var)
        result = var_obj.items(sys._getframe(1))
        print('Expected:', expected)
        print('Received:', result)
        assert result == expected

    # test1
    run_test(Attrs, 'attrs.foo.bar', [])
    run_test(Attrs, 'attrs', [])
    run_test(Attrs, 'foo', [])

    class Foo:
        pass
    foo = Foo()
    foo.bar = 1
    foo.baz = False

# Generated at 2022-06-12 20:01:46.727088
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    def f(x):
        return x.hello

    def g(x):
        x.hello = 'helloworld'

    def h():
        return x.hello

    def i():
        global j
        j = 1

    def k():
        global j
        global k

    # test for regular variables
    frame = inspect.currentframe()
    variables = BaseVariable('x', exclude = 'hello')
    items = variables.items(frame, normalize = False)
    assert items[0][0] == 'x'
    assert items[0][1] == '<module \'__main__\' (built-in)>'
    # test for regular variables with dot
    variables = BaseVariable('x.f_code', exclude = 'hello')
    items = variables.items(frame, normalize = False)

# Generated at 2022-06-12 20:01:50.516413
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from . import frame
    f = frame.Frame(sys._getframe())
    bv = BaseVariable(f.f_locals["__name__"])
    print(bv.items(f.frame))

# Generated at 2022-06-12 20:01:59.533386
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect

    def template(local_var):
        frame = inspect.currentframe()

# Generated at 2022-06-12 20:02:08.516986
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        x = {'a': 'b'}
        BaseVariable('x').items(locals())

    try:
        f()
    except Exception:
        pass

    x1 = BaseVariable('x').items(locals())
    x2 = BaseVariable('x').items(locals(), normalize=True)
    attrs = Attrs('x').items(locals())
    keys = Keys('x').items(locals())
    indices = Indices('x').items(locals())
    exploding = Exploding('x').items(locals())
    assert x1 == attrs
    assert x2 == attrs
    assert keys == indices
    assert x1 == exploding

# Generated at 2022-06-12 20:02:17.496920
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    try:
        test_dict.__dict__['d'] = 4
        print('BaseVariable_items testing dict')
        for var in [Attrs('test_dict'), Keys('test_dict'), Indices('test_dict')]:
            items = var.items(utils.current_frame())
            assert items == [('test_dict', '{...}'),
                             ('test_dict.d', '4'),
                             ('test_dict[a]', '1'),
                             ('test_dict[b]', '2'),
                             ('test_dict[c]', '3')], items
    except AttributeError:
        print('BaseVariable_items testing dict --> Dict does not has __dict__ ')

# Generated at 2022-06-12 20:02:28.339604
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = stack.extract_stack()[0]
    array = [1, 2, 3]
    result = [('array', 'list'), ('array[0]', 1), ('array[1]', 2), ('array[2]', 3)]
    assert Indices('array').items(frame) == result
    assert Indices('array')[:].items(frame) == result
    assert Indices('array')[1:].items(frame) == [('array[1]', 2), ('array[2]', 3)]

    array = [1, 2, 3]
    result = [
        ('s', 'str'),
        ('s.lower', 'str'),
        ('s.upper', 'str')
    ]
    assert Attrs('s').items(frame) == result
    assert Keys('array').items(frame) == result



# Generated at 2022-06-12 20:02:50.294573
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import math
    import numpy as np
    a = 10
    b = 10.5+1j
    c = 'python'
    d = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    e = {'dict': 'python', 'list': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
         'set': {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}}
    f = Exploding(math.sqrt(a))
    g = Keys('b')
    h = Indices('c')
    i = math.exp(a)
    k = np.zeros((2, 3, 4))
    l = np.ones((2, 3, 4))

    print()

# Generated at 2022-06-12 20:02:58.736443
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        a = {'a': 'b'}
        b = [1, 2]
        c = '123'
        1/0
    
    import sys
    frame = sys._getframe()
    frame = frame.f_back
    g = {'a': 'b', 'c': 'd'} # frame.f_globals
    l = {} # frame.f_locals
    # test for Attrs
    source = 'a'
    cls = Attrs(source)
    cls.items(frame, normalize=True)
    # test for Keys
    source = 'b'
    cls = Keys(source)
    cls.items(frame, normalize=True)
    # test for Indices
    source = 'c'
    cls = Indices(source)
   

# Generated at 2022-06-12 20:03:02.757047
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(argument):
        source = 'test'
        exclude = 'test'
        frame = 'test'
        normalize = 'test'
        a = BaseVariable(source, exclude)
        a.items(frame, normalize)

    exc = None
    try:
        test(1)
    except TypeError as e:
        exc = e

    assert exc is not None
    assert type(exc) == TypeError
    assert exc.args[0] == "Can't instantiate abstract class BaseVariable with abstract methods _items"

# Generated at 2022-06-12 20:03:09.713798
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_frame():
        x = {'y': 1}
        x1 = {'key': 'value'}
        x2 = {1:2}
        a = 15
        b = [3,4,5]
        c = 'hello'
        d = (7,8,9)
        e = {'key': 10}
        list_ = [a,b,c,x,x1]
        t = (1,2,3)
        return locals()

    frame = test_frame()
    base = BaseVariable('x1')
    print(base.items(frame))
    print(base.items(frame, normalize=True))
    keys = Keys('x1')
    print(keys.items(frame))
    print(keys.items(frame, normalize=True))
    indics = Ind

# Generated at 2022-06-12 20:03:19.001654
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import re
    import pickle
    class A(object):
        pass
    # if __debug__:
    #     A.x = 5
    #     A.y = 6
    A.x = 5
    A.y = 6

    a = A()
    a.z = 7
    a.t = 8

    b = A()
    b.z = 8

    a.b = b

    attrs = [(v, items) for (k, items) in Attrs('a').items(sys._getframe()) for (v, _) in items]
    keys = [(v, items) for (k, items) in Keys('a').items(sys._getframe()) for (v, _) in items]

# Generated at 2022-06-12 20:03:25.771284
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class A(BaseVariable):
        def _items(self, *args, **kw):
            pass

    source1 = 'a'
    source2 = 'b'
    exclude1 = 'aa'
    exclude2 = 'bb'
    av1_1 = A(source1, exclude1)
    av1_2 = A(source1, exclude1)
    av1_3 = A(source1, exclude2)
    av2 = A(source2, exclude1)
    av1_1_true = av1_1 == av1_2
    av1_2_true = av1_1 == av1_3
    av1_3_true = av2 == av1_1

    assert av1_1_true == True
    assert av1_2_true == False
    assert av1_3_true == False

# Generated at 2022-06-12 20:03:34.175986
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('main_value')
    var2 = BaseVariable('main_value')
    var3 = BaseVariable('main_values')
    var4 = BaseVariable('main_value', exclude=1)
    var5 = BaseVariable('main_value', exclude=2)
    var6 = BaseVariable('main_value', exclude=(1, 2))
    var7 = BaseVariable('main_value', exclude=(1,))
    var8 = BaseVariable('main_value', exclude=((1, 2),))
    var9 = BaseVariable('main_value', exclude=((1, 2),))
    assert(var1.__eq__(var2))
    assert(not var1.__eq__(var3))
    assert(not var1.__eq__(var4))

# Generated at 2022-06-12 20:03:36.916492
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = BaseVariable('var_name')
    assert var.items({'var_name' : 'var_value'}) == [('var_name', 'var_value')]


# Generated at 2022-06-12 20:03:47.302760
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    code = inspect.currentframe().f_code
    class A(object):
        x = 1
        y = 2

    a = A()
    if hasattr(a, '__dict__'):
        var = Attrs('a')
        assert var.items(code) == []
        assert var.items(code) == [('a', 'A()')]
        assert var.items(code) == [('a.x', '1'), ('a.y', '2')]
    else:
        var = Attrs('a')
        assert var.items(code) == []
        assert var.items(code) == [('a', 'A()')]
        assert var.items(code) == [('a.x', '1'), ('a.y', '2')]

# Generated at 2022-06-12 20:03:52.080941
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('x', 'y')
    v2 = BaseVariable('x')
    v3 = Indices('x')
    assert v1 != v2
    assert v1 != v3
    v1b = BaseVariable('x', 'y')
    assert v1 == v1b

# Generated at 2022-06-12 20:04:27.696816
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .tests.examples import ExampleClass, example_func
    variable = BaseVariable(source='a')
    assert variable.source == 'a'
    assert variable.items(frame=None) == ()
    # test with no excluded elements for the variable
    variable = BaseVariable(source='ExampleClass.a')
    assert variable.items(frame=None) == (('ExampleClass.a', '2.3'))
    assert variable.exclude == ()
    # test with excluded element for the variable
    variable = BaseVariable(source='ExampleClass.a', exclude='a')
    assert variable.items(frame=None) == ()
    assert variable.exclude == ('a')
    # test with excluded elements for the variable
    variable = BaseVariable(source='ExampleClass.a', exclude=('a', 'ExampleClass.a'))
    assert variable

# Generated at 2022-06-12 20:04:29.172408
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("a") == BaseVariable("a")
    assert BaseVariable("a") != BaseVariable("b")


# Generated at 2022-06-12 20:04:37.039415
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import dis
    test_source = 'test_source'
    test_exclude = ('test_exclude1', 'test_exclude2')
    new_BaseVariable = BaseVariable(test_source, test_exclude)
    class Frame(object):
        def __init__(self):
            self.f_globals = {}
            self.f_locals = {}
    frame = Frame()
    frame.f_globals = {}
    frame.f_locals = {test_source: 1}
    new_BaseVariable.items(frame)

# Generated at 2022-06-12 20:04:46.985323
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    globals = {'some_function': lambda a, b: None}
    locals = {'a': None, 'b': None, 'c': None}

    def test(source, expected):
        assert tuple(BaseVariable(source)({}, globals, locals).items()) == expected

    # test for method _items of class CommonVariable
    test('a', (('a', 'None'),))
    test('some_function(*[a, b])', (
        ('some_function(*[a, b])', 'some_function(*[a, b])'),
        ('some_function(*[a, b]).__class__', 'None'),
        ('some_function(*[a, b]).__doc__', 'None'),
    ))

# Generated at 2022-06-12 20:04:49.284714
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'something'
    exclude = 'something'
    string = BaseVariable(source, exclude)
    string.items(source, normalize=True)

# Generated at 2022-06-12 20:04:55.487448
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    f = inspect.currentframe()
    globals = {'x': 1}
    vars = {'y': 2}
    locals = {'z': 3}

    x = BaseVariable('z')
    print('tuple x: ', x.items(f, globals, vars, locals))

    y = BaseVariable('x')
    print('str y: ', y.items(f, globals, vars, locals))

    z = BaseVariable('x[:-1]')
    print('list z: ', z.items(f, globals, vars, locals))

# Generated at 2022-06-12 20:05:02.491263
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    l1 = [1,2,3]
    l1.a = 4
    l1.b = 5
    l2 = [1,2,3]
    l2.a = 4
    l2.b = 5
    bv1 = BaseVariable(l1)
    bv2 = BaseVariable(l2)
    assert bv1.items(l1) == bv2.items(l2)


# Generated at 2022-06-12 20:05:06.674952
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Given
    class A:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    a = A(1, 2, 3)
    frame = inspect.currentframe()
    frame.f_locals['a'] = a

    # When
    variable = Exploding('a')
    result = variable.items(frame)
    # Then
    assert result == (
        ('a', '<tests.test_exploding.A at 0x%x>' % id(a)),
        ('a.a', '1'),
        ('a.b', '2'),
        ('a.c', '3'),
    )

    # When
    variable = Keys(variable.source, ('a', 'b'))
    result = variable.items

# Generated at 2022-06-12 20:05:16.804256
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # CommonVariable
    assert CommonVariable('a').items({'a': Object()}) == [
        ('a', '<object>'),
        ('a.__class__', 'type'),
        ('a.__dict__', '{}'),
        ('a.__module__', '__main__'),
        ('a.__weakref__', 'None'),
        ('a.__slots__', '()')
    ]

    class Object2(Object):
        __slots__ = 'a', 'b', 'c'


# Generated at 2022-06-12 20:05:27.368704
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import os

    class DummyVariable(BaseVariable):
        def __init__(self, key):
            self.source = "frame"
            self.code = compile("frame.", '<variable>', 'eval')
            self.unambiguous_source = "frame."
            self.key = key

        def _items(self, key, normalize=False):
            return [(self.source, "val")]
        
    frame = inspect.currentframe()
    os.environ['frame'] = "val"
    v = DummyVariable("frame")
    print(v.items(frame))
    del os.environ['frame']
    
test_BaseVariable_items()

# Generated at 2022-06-12 20:06:23.788862
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('x')
    b = BaseVariable('x')
    c = BaseVariable('y')
    d = BaseVariable('x', exclude=('a'))

    assert a == b
    assert a != c
    assert d != a



# Generated at 2022-06-12 20:06:27.759801
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, utils.get_shortish_repr(main_value))]
    variable = TestVariable('variable')
    frame = utils.get_frame_from_function(lambda variable: variable)
    variable.items(frame, 'variable')

# Generated at 2022-06-12 20:06:30.361586
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('abc')
    v2 = BaseVariable('abc')
    v3 = BaseVariable('cde')
    assert v1 == v2, "Error of method __eq__ of BaseVariable"
    assert v1 != v3, "Error of method __eq__ of BaseVariable"

# Generated at 2022-06-12 20:06:30.808167
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:06:42.470434
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .test_context import test_frame

    import pickle
    fingerprint = BaseVariable('source')._fingerprint
    assert pickle.loads(pickle.dumps(fingerprint)) == fingerprint
    fingerprint = CommonVariable('source')._fingerprint
    assert pickle.loads(pickle.dumps(fingerprint)) == fingerprint
    fingerprint = Attrs('source')._fingerprint
    assert pickle.loads(pickle.dumps(fingerprint)) == fingerprint
    fingerprint = Keys('source')._fingerprint
    assert pickle.loads(pickle.dumps(fingerprint)) == fingerprint
    fingerprint = Indices('source')[1:]._fingerprint
    assert pickle.loads(pickle.dumps(fingerprint)) == fingerprint

    source = 'range(3)'
    variable = CommonVariable(source)

# Generated at 2022-06-12 20:06:44.922147
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('x')
    frame = {'x': 'value'}
    pairs = v.items(frame)
    assert list(pairs) == [('x', "'value'")]


# Generated at 2022-06-12 20:06:53.745046
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # 1. test class Attrs
    # 1.1 test method items when the main_value is a class
    class cls(object):
        def __init__(self):
            pass
        clsvar1 = 'clsvar1'
        __slots__ = ('instvar1', 'instvar2')

    clsinst = cls()

    attr = Attrs('clsinst')
    attr.__dict__['exclude'] = ('instvar1',)

    result = attr.items(clsinst.__dict__)
    assert result == [('clsinst.__dict__', '{}'), ('clsinst.instvar2', 'None'), ('clsinst.clsvar1', "'clsvar1'")]

    # 1.2 test method items when the main_value is a dict


# Generated at 2022-06-12 20:06:57.501533
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
    >>> import io
    >>> io
    <module 'io' (built-in)>
    >>> vble = BaseVariable("io")
    >>> tuple(vble.items(dict(io=io)))
    ('io', "<module 'io' (built-in)>")
    """

# Generated at 2022-06-12 20:07:01.962655
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    normal_var = BaseVariable('x')
    assert normal_var == normal_var
    assert not (normal_var != normal_var)
    d = {'x': normal_var}
    assert d[normal_var] == normal_var
    assert normal_var in d
    d[normal_var] = 1
    assert d['x'] == 1
    d['x'] = 2
    assert d[normal_var] == 2
    del d['x']
    assert normal_var not in d
    assert d.get(normal_var) is None
    assert normal_var != 1
    assert not (normal_var == 1)

# Generated at 2022-06-12 20:07:06.776221
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = sys._getframe()
    source = 'frame'
    items = BaseVariable(source).items(frame)
    assert items[0][1] == '<traceback.FrameSummary file <variable>, line unknown, code <module> at 0x7f6ec967e0a0>'