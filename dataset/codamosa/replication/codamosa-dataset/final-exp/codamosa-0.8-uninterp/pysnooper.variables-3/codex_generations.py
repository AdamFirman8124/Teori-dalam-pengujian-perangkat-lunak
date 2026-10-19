

# Generated at 2022-06-12 19:58:50.479700
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    Code = BaseVariable
    assert Code("a").source == 'a'
    assert Code("a", "b").source == 'a'
    assert Code("a", "b").exclude == ('b', )
    assert Code("a", exclude="b").exclude == ('b', )
    assert Code("a", exclude=("b", "c")).exclude == ('b', 'c')
    with pytest.raises(TypeError) as e_info:
        Code("a", exclude=["b", "c"])
    assert 'tuple' in str(e_info.value)

# Generated at 2022-06-12 19:58:56.840685
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    x = CommonVariable('x', exclude=['y'])
    assert x.source == 'x'
    assert x.exclude == ('y',)
    assert x.code == compile('x', '<variable>', 'eval')
    assert x.unambiguous_source == 'x'

    x = CommonVariable('(x)', exclude=['y'])
    assert x.source == '(x)'
    assert x.exclude == ('y',)
    assert x.code == compile('(x)', '<variable>', 'eval')
    assert x.unambiguous_source == '(x)'

    x = CommonVariable("'a'[0]")
    assert x.source == '\'a\'[0]'
    assert x.exclude == ()

# Generated at 2022-06-12 19:59:00.121121
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('b')
    c = BaseVariable('a')
    assert (a == a) and (a == c) and (c == a)
    assert not (a == b) and not (b == a)

# Generated at 2022-06-12 19:59:02.348930
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    source = "'12345'"
    exclude = "()"
    variable = Indices(source, exclude)
    variable1 = variable[1:5:2]

    cmp_variable = variable._fingerprint
    cmp_variable1 = variable1._fingerprint

    assert cmp_variable == variable._fingerprint
    assert cmp_variable1 != variable1._fingerprint

# Generated at 2022-06-12 19:59:11.881220
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # local variable
    def foo(x):
        y = x + 1
        return y

    assert BaseVariable('x').items(foo.__code__.co_firstlineno + 1, foo.__globals__) == (('x', '1'),)
    assert BaseVariable('x').items(foo.__code__.co_firstlineno + 1, foo.__globals__, normalize=True) == (('x', '1'),)

    # global variable
    g_x = 1
    def f_g():
        return g_x

    assert BaseVariable('g_x').items(f_g.__code__.co_firstlineno - 1, f_g.__globals__) == (('g_x', '1'),)

    # builtin

# Generated at 2022-06-12 19:59:23.897367
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    
    x = 1
    y = 2
    d = {'a': 1, 'b':2}

    variable1 = CommonVariable('x', ['b'])
    variable2 = CommonVariable('y', ['b'])
    
    variable3 = CommonVariable('d', ['b'])
    variable4 = CommonVariable('d', ['b'])
    
    assert hash(variable1.source) == hash(variable1.source) 
    list1 = [variable1]
    list2 = [variable2]

    assert variable1 not in list1
    assert variable1 not in list2
    assert variable2 in list2

    list3 = [variable3]
    list4 = [variable4]
    assert variable3 in list3
    assert variable3 in list4
    assert variable1 not in list3


# Generated at 2022-06-12 19:59:25.351589
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')

# Generated at 2022-06-12 19:59:29.222668
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable(1, 2) == BaseVariable(1, 2)
    assert BaseVariable(1, 2) != BaseVariable(2, 1)
    assert BaseVariable(1, 2) != 1

# Generated at 2022-06-12 19:59:33.864505
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def run(cls):
        v1 = cls('foo')
        v2 = cls('foo')
        assert v1 == v2
        v3 = cls('bar')
        assert v1 != v3

    yield run, Keys
    yield run, Indices
    yield run, Attrs
    yield run, Exploding

# Generated at 2022-06-12 19:59:38.503462
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    from . import utils
    temp = CommonVariable(source='x',exclude=('_y','_z'))
    assert temp.source == 'x'
    assert temp.exclude == ('_y', '_z')
    assert utils.isclose(temp.code,compile('x', '<variable>', 'eval'))
    assert temp.unambiguous_source == 'x'



# Generated at 2022-06-12 19:59:53.207160
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class TestClass(object):
        def __init__(self, x):
            self.x = x

    frame = utils.FakeFrame()
    frame.f_locals['a'] = 1
    frame.f_locals['b'] = TestClass(1)
    frame.f_locals['c'] = [2]

    var = BaseVariable('a')
    assert ('a', '1') in list(var.items(frame))
    var = BaseVariable('b')
    assert ('b', 'b') in list(var.items(frame))
    var = BaseVariable('c')
    assert ('c', '[2]') in list(var.items(frame))
    var = BaseVariable('c.x')
    assert ('c.x', '2') in list(var.items(frame))
    var = BaseVariable

# Generated at 2022-06-12 20:00:00.982308
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        x = 1
        g()
    def g():
        x = 2
        y = 3
        z = 4
        return x, y, z

    variables = [
        Attrs('x'),
        Keys('x'),
        Indices('x'),
        Exploding('x'),
    ]

    frame_f = inspect.currentframe()
    frame_g = inspect.currentframe(1)

    # parent of frame of g is frame of f
    assert frame_g.f_back is frame_f

    # x = 1
    # f()
    assert frame_f.f_locals == {'f': f, 'x': 1}
    for i, variable in enumerate(variables):
        assert variable.items(frame_f) == [('x', '1')]

    # x = 1

# Generated at 2022-06-12 20:00:10.491484
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import os
    import sys
    import random

    # test data

# Generated at 2022-06-12 20:00:19.829849
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Test(object):
        def __getitem__(self, item):
            return item
        def __getattr__(self, item):
            return item
    t = Test()
    assert Attrs('t')._items(t) == [('t', '<{}.Test object at 0x..>'.format(__name__)),
                                    ('t.__getattr__', '<method-wrapper \'__getattr__\' of {}.Test object at 0x..>'.format(__name__)),
                                    ('t.__class__', '<class \'{}.Test\'>'.format(__name__)),
                                    ('t.__dict__', '{}')]
    d = {'foo': 'bar'}

# Generated at 2022-06-12 20:00:26.086415
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types

    frame = types.SimpleNamespace(
        f_globals={'sys': sys},
        f_locals={'attrs': [1, 2]}
    )
    base_variable = BaseVariable('attrs')
    print(base_variable.items(frame))
    print(base_variable.items(frame, normalize=True))



# Generated at 2022-06-12 20:00:29.675521
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = BaseVariable('a', exclude='b')
    assert (bv.items(eval('a={b:1, c:2}', dict(vars()))) == ('a.b', '1'), 'a.c', '2')


# Generated at 2022-06-12 20:00:38.079299
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from types import FrameType
    import sys
    source_list = ['x', 'x.y', 'x[y]']
    def exp_items(source, exclude=()):
        source_exp = source

        def get_value(main_value, key):
            return main_value[key]

        if source in ('x', 'x.y'):
            source_exp = '({})'.format(source_exp)
        if source == 'x':
            item = 'x', utils.get_shortish_repr('value_x')
        else:
            item = '{}[{}]'.format(source_exp, utils.get_shortish_repr('y')), \
                   utils.get_shortish_repr('value_y')
        return (item,)


# Generated at 2022-06-12 20:00:48.859620
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class TestClass(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    test_obj = TestClass("xyz", 123)
    test_dict = {"a": 1, "b": 2}
    test_list = [1, 2, 3]

    class TestVariable(BaseVariable):
            def _items(self, main_value, normalize=False):
                return [("main", utils.get_shortish_repr(main_value, normalize=normalize))]

    # test case 1
    frame = sys._getframe()
    source = "test_obj"
    exclude = {'x'}
    test_items = tuple(TestVariable(source, exclude).items(frame))

# Generated at 2022-06-12 20:00:51.262335
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('request.POST')
    v2 = BaseVariable('request.POST')
    assert v1 == v2



# Generated at 2022-06-12 20:01:02.230510
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pdb
    import re
    source = 'pdb.set_trace'
    pdb.set_trace()
    reg_result = re.compile('^([a-zA-Z0-9_]+[ ]+[a-zA-Z0-9_]+)[ ]*=')
    dic_result = {}
    import inspect
    frame = inspect.currentframe()
    var = BaseVariable(source)
    var.items(frame)
    for item in var.items(frame):
        dic_result[item[0]] = item[1]
    for item in vars(frame).keys():
        if item in dic_result.keys():
            assert dic_result[item] == str(vars(frame)[item])
    print (dic_result)

# Generated at 2022-06-12 20:01:17.675051
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import math
    import numpy
    import random
    import re
    import string
    import time
    import scipy.misc

    locals_dict = inspect.currentframe().f_locals
    random_state = random.Random(0)
    random_str = lambda length: ''.join(random_state.choice(string.ascii_uppercase) for _ in range(length))
    random_int = lambda: random_state.randint(-100, 100)
    random_float = lambda: random_state.randint(-100, 100) * random_state.random()


# Generated at 2022-06-12 20:01:27.195712
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test():
        assert x == [] and y == []

    frame = sys._getframe()
    assert list(Attrs('a').items(frame))[1][0] == 'a.__doc__'
    assert list(Keys('{10: "a"}').items(frame))[1][0] == '{10: "a"}[10]'
    assert list(Indices('[1, 2, 3]')[2:-2].items(frame))[1][0] == '[1, 2, 3][2]'
    assert list(Exploding('a').items(frame))[1][0] == 'a.__doc__'

# Generated at 2022-06-12 20:01:35.035484
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class CustomBaseVariable(BaseVariable):
        def __init__(self):
            super(CustomBaseVariable, self).__init__(source='string',exclude='')

    custom_base_variable_1 = CustomBaseVariable()
    custom_base_variable_2 = CustomBaseVariable()
    assert(custom_base_variable_1.__eq__(custom_base_variable_2) == True)

    class CustomVariable_1(BaseVariable):
        def __init__(self):
            super(CustomVariable_1, self).__init__(source='string',exclude='string')

    class CustomVariable_2(BaseVariable):
        def __init__(self):
            super(CustomVariable_2, self).__init__(source='string',exclude='string')

    custom_variable_1 = CustomVariable_1()
    custom

# Generated at 2022-06-12 20:01:38.916907
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    local_vars = {'a':1}
    global_vars = {'b':2}
    frame = utils.Frame(local_vars, global_vars)
    v = BaseVariable('a', ('a'))
    v.items(frame)

# Generated at 2022-06-12 20:01:47.508139
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    #exclude_keys = ('x1', 'x2', 'x3')
    #env = {'a': [1, 2, 3], 'b': {'x1': 1, 'x2': 2, 'x3': 3, 'x4': 4}, 'c': 0}
    exclude_keys = ()
    env = {'a': [1, 2, 3], 'b': {'x1': 1, 'x2': 2, 'x3': 3, 'x4': 4}, 'c': 0}
    import inspect
    frame = inspect.currentframe()
    frame.f_globals = env
    frame.f_locals = env


# Generated at 2022-06-12 20:01:57.790043
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = dict(
        one=dict(two=2, three=dict(four=4, five='five', six=[6, 7, 8])),
        nine=10,
        eleven=11
    )
    frame['one']['three']['four'] = 4

    assert list(Attrs('one', exclude=['two']).items(frame)) == [
        ('one', '<dict>'),
        ('one.three', '<dict>'),
        ('one.three.five', "'five'"),
        ('one.three.four', '4'),
        ('one.three.six', '<list>')
    ]

    assert list(Keys('one', exclude=['two']).items(frame)) == [
        ('one', '<dict>'),
        ('one[three]', '<dict>')
    ]

# Generated at 2022-06-12 20:02:05.140822
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    frame = sys._getframe(2)
    # create a simple dictionary to test items of class BaseVariable
    d = {}
    d['3'] = 3
    d[3] = 3
    d[(3,)] = 3
    d['3.3'] = 3.3
    d[3.3] = 3.3
    d['three'] = 'three'
    d['three'+'three'] = 'threethree'
    d['three'*3] = 'three'*3
    d['B'] = {}
    d['B']['C'] = {}
    d['B']['C']['D'] = {}
    d['B']['C']['D']['E'] = {}

# Generated at 2022-06-12 20:02:14.262784
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    # Case when source is a variable which doesn't exist
    def test_accident_source():
        source = 'a'
        def f():
            pass
        frame = f.__code__.co_firstlineno
        assert b.items(frame) == ()

    # Case when source is a variable which exists
    def test_exist_source():
        source = 'a_exist'
        def f():
            pass
        frame = f.__code__.co_firstlineno
        assert b.items(frame) == (('a_exist', '0'))

    # Case when source is a variable with a variable in the exclude list
    def test_accident_exclude():
        source = 'a'
        exclude = ('a_none',)
        def f():
            pass
        frame = f.__code__.co_

# Generated at 2022-06-12 20:02:17.997445
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.stack()[0]
    frame = frame.frame
    print(frame.f_locals)
    variable = list(BaseVariable('frame', ['f_locals']).items(frame))
    print(variable)

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:02:28.639793
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    f_globals = {'x': [], 'y': {}}
    f_locals = {'a': {}, 'b': []}
    frame = {'f_globals': f_globals, 'f_locals': f_locals}

    BaseVariable("$x").items(frame)
    BaseVariable("$y").items(frame)
    Frame("$a").items(frame)
    Frame("$b").items(frame)

    BaseVariable("$x").items(frame)
    BaseVariable("$y").items(frame)

    Attrs("$x").items(frame)
    Attrs("$y").items(frame)

    Keys("$x").items(frame)
    Keys("$y").items(frame)

    Indices("$x").items(frame)

# Generated at 2022-06-12 20:02:41.550897
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    frame = sys._getframe(0)
    glob = frame.f_globals
    loc = frame.f_locals

    test_variable = BaseVariable('frame')

    assert test_variable.items(frame) == [('frame', '<frame object at 0x000001CB43E02E48>')]



# Generated at 2022-06-12 20:02:46.518727
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    baseVariable1 = BaseVariable('variable_source', ('exclude1', 'exclude2'))
    baseVariable2 = BaseVariable('variable_source', ('exclude1', 'exclude2'))
    baseVariable3 = BaseVariable('variable_source', ('exclude1', 'exclude3'))

    assert baseVariable1 == baseVariable2
    assert baseVariable1 != baseVariable3
    assert baseVariable2 != baseVariable3



# Generated at 2022-06-12 20:02:56.716997
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import pycompat
    from .pycompat import PY2
    import sys

    class C(object):
        class_var = 1

        def __init__(self, x, y, z=1):
            self._x = x
            self._y = y
            self._z = z

        def f(self, a, b, c=1):
            return a + b + c

        @property
        def x(self):
            return self._x

        @property
        def pi(self):
            return 3.14

        def __getitem__(self, item):
            return [1, 2, 3][item]

        def __len__(self):
            return 3

    class D(C):
        def g(self):
            return 2


# Generated at 2022-06-12 20:02:57.888763
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Variable('x') == Variable('x')


# Generated at 2022-06-12 20:02:59.384232
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass



# Generated at 2022-06-12 20:03:00.383898
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass



# Generated at 2022-06-12 20:03:02.784946
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('') == BaseVariable('')
    assert not BaseVariable('') == BaseVariable('x')
    assert not BaseVariable('') == object()

# Generated at 2022-06-12 20:03:05.160886
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pdb
    from . import pdb_clone
    old_pdb = pdb.Pdb
    pdb.Pdb = pdb_clone
    pdb.Pdb().set_trace()
    pdb.Pdb = old_pdb

# Generated at 2022-06-12 20:03:09.005704
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class TestBaseVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            super(TestBaseVariable, self).__init__(source, exclude)

        def _items(self, key, normalize=False):
            return ((self.source, key),)

    assert TestBaseVariable('x') == TestBaseVariable('x')
    assert not TestBaseVariable('x') == TestBaseVariable('y')
    assert not TestBaseVariable('x', exclude=('x')) == TestBaseVariable('x', exclude=('y'))

# Generated at 2022-06-12 20:03:16.906585
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # A and B have different sources
    assert not BaseVariable('A') == BaseVariable('B')
    # A and A have the same source, but different excludes
    assert not BaseVariable('A', ('x')) == BaseVariable('A', ('y'))
    # C and C are equal
    assert BaseVariable('C', ('x')) == BaseVariable('C', ('x'))
    source = 'A'
    exclude = ('a', 'b', 'c')
    assert BaseVariable(source, exclude) == BaseVariable(source, exclude)
    assert hash(BaseVariable(source, exclude)) == hash(BaseVariable(source, exclude))

# Generated at 2022-06-12 20:03:34.493011
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import doctest
    doctest.testmod()

# Generated at 2022-06-12 20:03:38.068242
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("test", ['p'])
    v2 = BaseVariable("test", ['p'])
    assert v1 == v2
    v3 = BaseVariable("test2", ['p'])
    assert v1 != v3


# Generated at 2022-06-12 20:03:48.086904
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    def f():
        a = 1
        return a
    def g():
        b = 2
        return b
    def h():
        c = 3
        return c
    def test():
        a = 1
        b = 2
        c = 3
        return a, b, c
    test_output = utils.items_of_blocks(
        {Attrs('a'): [f], Keys('b'): [g], Indices('c'): [h], Exploding('d'): [test]}
    )

# Generated at 2022-06-12 20:03:57.537513
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types
    import importlib
    def f():
        x = 1
        y = 2
        z = 3
        return locals()
    frame = f.__code__.co_firstlineno
    frame = frame.f_back
    print(type(frame), frame.f_globals, frame.f_locals)
    # print([(key, value) for key, value in frame.f_globals.items()])
    # print([(key, value) for key, value in frame.f_locals.items()])

    # print(frame.f_locals['__builtins__'])
    # print(frame.f_locals['__name__'])

    print(frame.f_locals['__name__'])

# Generated at 2022-06-12 20:04:04.162962
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(variable):
        d = {'a': 'a value'}
        f = {'d': d}
        t = (1, )
        return variable.items(frame={'d': d, 'f': f, 't': t})

    assert test(BaseVariable('d')) == [('d', 'd')]
    assert test(BaseVariable('d.a')) == [('d.a', "'a value'")]
    assert test(BaseVariable('d[a]')) == [('d[a]', 'None')]
    assert test(BaseVariable('d.a.b')) == [('d.a', "'a value'")]
    assert test(BaseVariable('f.d.a')) == [('f.d.a', "'a value'")]

# Generated at 2022-06-12 20:04:05.356269
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a', exclude=1)
    var2 = BaseVariable('a')
    assert var1 == var2



# Generated at 2022-06-12 20:04:10.592553
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def tester(method, source, result):
        assert method(source) == result

    class BaseVariableTest(BaseVariable):
        def __init__(self, source):
            super(BaseVariableTest, self).__init__(source)

        def _items(self, key, normalize=False):
            return key

    v = BaseVariableTest('apollo')
    #TODO: test exclude
    tester(v.items, 'BaseVariableTest', 'BaseVariableTest')
    tester(v.items, 'apollo', 'apollo')

# Generated at 2022-06-12 20:04:15.290258
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    import unittest


    class TestBaseVariable(unittest.TestCase):
        def test_items(self):
            frame = sys._getframe()
            # Initialize a common variable
            key = 'a'
            source = 'source'
            code = 'a'
            common_var = CommonVariable(source=source)
            # Initialize an attribute variable
            attr_name = 'attr_name'
            attr_var = Attrs(source=source)
            attr_var._format_key = lambda key: attr_name
            # Initialize an index variable
            index = '0'
            index_var = Indices(source=source)
            index_var._format_key = lambda key: index
            # Initialize a keys variable

# Generated at 2022-06-12 20:04:24.987554
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import debug

    class Counter:
        def __init__(self):
            self.call_counter = 0

        def __call__(self):
            result = self.call_counter
            self.call_counter += 1
            return result

    class BaseVariable(BaseVariable):
        def items(self, frame, normalize=False):
            if frame is not None:
                if frame.f_locals['throw_KeyError']():
                    raise KeyError
                elif frame.f_locals['throw_KeyError_inside_items']():
                    raise KeyError
                else:
                    pass
            return super(BaseVariable, self).items(frame, normalize)

    def bad_items(frame, normalize=False):
        raise RuntimeError

    throw_KeyError = Counter()
    throw_KeyError_inside

# Generated at 2022-06-12 20:04:33.176803
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # TODO: this should raise an error with the current code of BaseVariable,
    # but it doesn't. Why is this?
    from .utils import BadInputException
    from .models import frame
    from . import utils


# Generated at 2022-06-12 20:05:17.382228
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test case 1: exception in code
    source = '1/0'
    variable = BaseVariable(source)
    assert not variable.items(1)
    assert not variable.items(1)

    # Test case 1: test items for mapping
    source = 'case'
    b = {'1':1, '2':2}
    variable = BaseVariable(source)
    assert variable.items(b) == [('case', '{}'), ('case.1', 1), ('case.2', 2)]

    # Test case 2: test items for sequence
    source = 'case'
    b = [1,2]
    variable = BaseVariable(source)
    assert variable.items(b) == [('case', '[1, 2]'), ('case[0]', 1), ('case[1]', 2)]


# Generated at 2022-06-12 20:05:29.804680
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import pandas as pd
    from pandas._libs.tslibs.timestamps import Timestamp
    df = pd.DataFrame(data=[[1,2,3],[4,5,6]], index=None, columns=['a', 'b', 'c'])
    df.index = ['row{}'.format(i) for i in range(len(df.values))]
    dtype = {"A": "category", 'B':'float32', 'C':'datetime64[ns]'}
    df1 = pd.DataFrame(np.random.random((3, 3)),
                       columns=['A', 'B', 'C'],
                       index=[1, 2, 3],
                       dtype=dtype)


# Generated at 2022-06-12 20:05:32.618362
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import test_data

    var = BaseVariable("data")
    assert var.items(test_data.__dict__) == []



# Generated at 2022-06-12 20:05:41.579415
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import random
    import string

    def foo():
        a = random.randint(3, 10)
        b = random.sample(string.digits, a)
        c = random.sample(string.ascii_letters, a)
        d = dict(zip(b, c))
        return d

    variable = variable_names_of_values_of_localvars(inspect.currentframe(), foo, 'd')

    for item in variable.items(frame=inspect.currentframe()):
        assert item[0] in locals()
        assert eval(item[0], locals()) == locals()[item[0]]

# Generated at 2022-06-12 20:05:46.724484
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('x')
    v2 = BaseVariable('x')
    assert v1 == v2
    v3 = BaseVariable('y')
    assert v1 != v3
    v4 = BaseVariable('x', exclude=['y'])
    assert v1 != v4

# Generated at 2022-06-12 20:05:55.938118
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # when
    py_object = (1,2,3) 
    py_list = [1, 2, 3]
    py_tuple = (1, 2, 3)
    py_dict = {'age': 1, 'name': 'Amei'}
    py_set = set([1,2,3])
    
    # and
    variable = BaseVariable("py_object")
    variable_list = BaseVariable("py_list")
    variable_tuple = BaseVariable("py_tuple")
    variable_dict = BaseVariable("py_dict")
    variable_set = BaseVariable("py_set")

    # then
    assert variable.items(py_object)==("py_object", "1, 2, 3")

# Generated at 2022-06-12 20:05:59.081558
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable("s")
    var2 = BaseVariable("s")
    var3 = BaseVariable("s", "")
    assert var1 == var2
    assert not var2 == var3
    assert var1 == var1


# Generated at 2022-06-12 20:06:08.768714
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('a').items({'a':0},True)==('a', '0')
    assert BaseVariable('a').items({'a':[]},True)==('a', '[]')
    assert BaseVariable('a').items({'a':'abc'},True)==('a',"'abc'")
    assert BaseVariable('a').items({'a':{}},True)==('a', '{}')
    assert BaseVariable('a').items({'a':(1,2)},True)==('a', '(1, 2)')
    assert BaseVariable('a').items({'a':(1,)},True)==('a', '(1,)')
    assert BaseVariable('a').items({'a':(1)},True)==('a', '1')

# Generated at 2022-06-12 20:06:14.088204
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert(len(Attrs('x').items('x')) == 0)
    assert(len(Attrs('x').items('')) == 0)
    assert(len(Attrs('x').items(1)) == 0)
    assert(len(Attrs('x').items(None)) == 0)
    assert(len(Attrs('x').items([])) == 0)
    assert(len(Attrs('x').items(())) == 0)
    assert(len(Attrs('x').items({})) == 0)
    

test_BaseVariable_items()

# Generated at 2022-06-12 20:06:19.579411
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # string
    bm_var = BaseVariable('s', exclude = [])
    assert bm_var.items(FrameInfo()) == (('s', '\''),)

    # int
    bm_var = BaseVariable('i', exclude = [])
    assert bm_var.items(FrameInfo()) == (('i', '0'),)

    # float
    bm_var = BaseVariable('f', exclude = [])
    assert bm_var.items(FrameInfo()) == (('f', '0.0'),)

    # list
    bm_var = BaseVariable('li', exclude = [])
    assert bm_var.items(FrameInfo()) == (('li', '[]'),)

    # dictionary
    bm_var = BaseVariable('di', exclude = [])
    assert bm_var.items

# Generated at 2022-06-12 20:07:29.717368
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    b1 = BaseVariable('foo')
    b2 = BaseVariable('foo')
    assert b1 == b2
    assert b1 != 'bar'
    b1.exclude = ('bar',)
    assert b1 != b2
    assert b1 != 'bar'

# Generated at 2022-06-12 20:07:37.615240
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    indent = "  "
    func = inspect.currentframe().f_code.co_name
    print_test_subject(func, indent)
    print_test_infos(func, indent)

    var1 = BaseVariable('src1', ('exc',))
    var2 = BaseVariable('src1', ('exc',))
    var3 = BaseVariable('src1', ('exc2',))
    var4 = BaseVariable('src2', ('exc',))
    print_test_result(func, indent, (var1 == var2) and not (var1 == var3) and not (var1 == var4))


# Generated at 2022-06-12 20:07:40.570070
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import pycompat

    a = BaseVariable('a')
    assert a == a
    assert not a == BaseVariable('b')

    if pycompat.PY2:
        assert a == BaseVariable  # superclass is not the same as subclass



# Generated at 2022-06-12 20:07:51.320573
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('') == BaseVariable('')
    assert BaseVariable('') != BaseVariable('a')
    assert BaseVariable('') != BaseVariable('', exclude=('a',))
    assert BaseVariable('') != BaseVariable('a', exclude=('a',))
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a') != BaseVariable('a', exclude=('a',))
    assert BaseVariable('a') != BaseVariable('b', exclude=('a',))
    assert BaseVariable('a', exclude=('a',)) == BaseVariable('a', exclude=('a',))
    assert BaseVariable('a', exclude=('a',)) != BaseVariable('b', exclude=('a',))

# Generated at 2022-06-12 20:07:57.642461
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from . import pycompat

    class FakeFrame:
        f_locals = {}
        f_globals = {}

    frame = FakeFrame()
    # Check that instance of class BaseVariable can be call the method items
    # successfully.
    # 1. instances of classes that are inherited from BaseVariable.
    attrs = Attrs('self', exclude=('self',))
    result = attrs.items(frame)
    assert not result

    keys = Keys('self', exclude=('self',))
    result = keys.items(frame)
    assert not result

    index = Indices('self', exclude=('self',))
    result = index.items(frame)
    assert not result

    explode = Exploding('self', exclude=('self',))
    result = explode.items(frame)

# Generated at 2022-06-12 20:08:02.730957
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(BaseVariable):
        def __init__(self):
            self.source = 'MyVariable'
            self.code = compile('MyVariable', '<variable>', 'eval')

        def _items(self, main_value, normalize=False):
            return [('MyVariable', 'MyVariable')]

    assert MyVariable().items({'MyVariable': 'MyVariable'}) == [('MyVariable', 'MyVariable')]


# Generated at 2022-06-12 20:08:08.067211
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable_1 = Attrs('a', exclude='b')
    variable_2 = Attrs('a', exclude='b')
    variable_3 = Attrs('a', exclude='d')
    variable_4 = Attrs('b', exclude='b')
    variable_5 = Keys('a', exclude='b')
    assert variable_1 == variable_2
    assert variable_1 != variable_3
    assert variable_1 != variable_4
    assert variable_1 != variable_5 


# Generated at 2022-06-12 20:08:11.858712
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'x'
    exclude = 'y'
    def eval(source):
        return ''

    x = 'x'

    class BaseVariable(CommonVariable):
        def _keys(self, main_value):
            return ''

    b = BaseVariable(source, exclude)
    b.items(x, eval)
    b._items(x)



# Generated at 2022-06-12 20:08:17.320267
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    x = BaseVariable('a')
    assert x == x
    assert x != BaseVariable('a')
    assert x != BaseVariable('b')
    assert x != BaseVariable('a', 'b')
    assert x != BaseVariable('b', 'b')
    assert x != BaseVariable(1)
    assert x != 1


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-12 20:08:19.755945
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import pytest

    variable_1 = BaseVariable('x')
    variable_2 = BaseVariable('y')

    assert variable_1 == variable_1
    assert variable_1 != variable_2
