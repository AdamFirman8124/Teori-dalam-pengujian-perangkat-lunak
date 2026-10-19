

# Generated at 2022-06-12 19:58:46.674343
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    indices = Indices('foo')
    indices_slice = indices[2:10]
    assert isinstance(indices_slice, Indices)

# Generated at 2022-06-12 19:58:49.205915
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    indices_object = Indices('f')
    __tracebackhide__ = True
    assert indices_object[1:3] == Indices('f')
    assert indices_object[::2] == Indices('f')

# Generated at 2022-06-12 19:58:52.696999
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import Frame
    frame = Frame(f_globals={'x': {'x2': 3}})
    key = 'x'
    var = BaseVariable(key, exclude=('x2',))
    assert var.items(frame) == [('x', "{'x2': 3}")]



# Generated at 2022-06-12 19:59:02.339305
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pytest
    def items_test(variable, frame):
        return variable.items(frame)
    def items_test_normalize(variable, frame):
        return variable.items(frame, normalize=True)

    global_variable = Attrs('a', ('b',))
    local_variable = Attrs('_locals', ('b',))
    exception_variable = Attrs('False', ('b',))

    class Test:
        a = {'b': 2, 'c': 3}
    def test_func():
        a = Test()
        _locals = {'c': 5}
        return a, _locals

    _, frame = pytest.raises(NameError, test_func)

    assert items_test(global_variable, frame) == [('a', '<Test ()>')]

# Generated at 2022-06-12 19:59:09.315962
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def func1(v):
        a = 1
        b = [2, 3, 4]
        c = {"d": 5, "e": 6}
        f = (7, 8, 9)
        g = {'h', 'i'}
        return v

    res = BaseVariable('a').items(func1.__code__.co_varnames, func1.__code__.co_varnames)
    assert res == (('a', '1'),)
    pass


# Generated at 2022-06-12 19:59:14.619194
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types
    def test(): pass
    test.a = 1
    test.b = 2
    test.c = 3
    globals = {'a' : 1}
    locals = {'b' : 2, 'c' : 3}
    frame = types.FrameType(
        f_code = types.CodeType(0,0,0,0,0,0,0,0,0,0,0),
        f_locals = locals, f_globals = globals, f_lasti = 0, f_lineno = 0
    )
    source = 'test'

    v = BaseVariable(source)

    assert v.source == source
    assert v.exclude == ()

    attrs = Attrs(source)
    indices = Indices(source)
    keys = Keys(source)

# Generated at 2022-06-12 19:59:20.483430
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = CommonVariable('testvar')
    var2 = CommonVariable('testvar')
    var3 = CommonVariable('testvar2')
    assert var1.__eq__(var2)
    assert not var1.__eq__(var3)
    assert not var1.__eq__(int(1))

# Generated at 2022-06-12 19:59:24.219058
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    Indices('a[1]')[slice(1, 2)]._slice == slice(1, 2)
    Indices('a[1]')[slice(1, 2)].source == 'a[1]'
    Indices('a[1]')[slice(1, 2)].exclude == ()

# Generated at 2022-06-12 19:59:30.301774
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    
    v0 = BaseVariable('x', ('a', ))
    v1 = BaseVariable('x', ('a', ))
    v2 = BaseVariable('y', ('a', ))

    assert v0.__eq__(v1) == True
    assert v1.__eq__(v2) == False
    assert v2.__eq__(v0) == False


# Generated at 2022-06-12 19:59:34.404401
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from . import config
    from .exceptions import CommandError

    input_args = ['[a]', '[b]', '', '[c]']
    vars_list = config.get_annotated_variables(input_args, True)
    assert vars_list[-1].source == '[c]'

# Generated at 2022-06-12 19:59:52.713104
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import reporting
    from . import frames
    from .compat import collections_abc

    def get_frame():
        for frame in frames.walk_tb(None):
            return utils.FrameWithCode(frame)

    def check_variables(variables):
        for variable in variables:
            for name, value in variable.items(get_frame()):
                assert eval(name, get_frame().f_globals, get_frame().f_locals) == value


# Generated at 2022-06-12 20:00:00.729374
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Create a list of keys and values as [[key0, val0], [key1, val1], ...]
    # where each key is a string and each value is a string or a number.
    keys_vals = [
        ['a', 'a_val'],
        ['b', 1],
        ['c', 'c_val'],
    ]
    keys = [pair[0] for pair in keys_vals]
    vals = [pair[1] for pair in keys_vals]

    # Create a dictionary that maps each key to its corresponding value.
    d = {key: value for key, value in keys_vals}

    # Create a dictionary that maps each key to its corresponding value,
    # but exclude the mapping from 'b' to 1 from the dictionary.

# Generated at 2022-06-12 20:00:10.344604
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from io import StringIO
    import sys
    import traceback
    import time
    def time_caller(func):
        def wrapper(*args, **kwargs):
            start = time.clock()
            func(*args, **kwargs)
            print('time taken:', time.clock() - start)

        return wrapper

    frame = sys._getframe()
    a = {'a': 1}
    b = (1,)
    c = [1]
    @time_caller
    def t1():
        bv = BaseVariable('a')
        bv.items(frame)
    @time_caller
    def t2():
        cv = CommonVariable('a')
        cv.items(frame)

    t1()
    t2()
    t1()
    t2()
    t1()

# Generated at 2022-06-12 20:00:16.283067
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from tokenize import generate_tokens
    from io import BytesIO
    from pprint import pprint
    def extract_identifier(key):
        print("key = {}, repr = {}".format(key, repr(key)))
        if len(key) >= 2:
            indent_len = len(key) - len(key.lstrip())
            key = key[indent_len:].rstrip()  # remove indenting and tailing spaces
            print("key after stripping = {}".format(key))

            tokens = list(generate_tokens(BytesIO(key.encode()).readline))
            print("tokens = {}".format(tokens))
            if len(tokens) == 1:
                tok_type, tok_str, begin, end, line = tokens[0]
               

# Generated at 2022-06-12 20:00:22.402392
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global x
    x = 4
    b = BaseVariable('x')
    assert type(b) is BaseVariable
    assert b.source == 'x'
    assert b.items('x') == (('x', '4'),)
    # Test various conditions of exclude parameter
    assert b.exclude == tuple()
    b.exclude = 'x'
    assert b.exclude == ('x',)
    b.exclude = ['x']
    assert b.exclude == ('x',)
    b.exclude = ('y', 'x')
    assert b.exclude == ('y', 'x')
    b.exclude = ['y', 'x']
    assert b.exclude == ('y', 'x')

# Generated at 2022-06-12 20:00:32.881076
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types
    import inspect
    import pdb
    frame = inspect.currentframe()
    frame = frame.f_back.f_back #Skip two frames to get the actual frame where 
                               # Variable was called

    # Prepare a functions for testing
    def foo(bar):
        """
        Function for testing
        """
        baz = bar + 5
        return baz

    foo.dict = {'a': 1, 'b': 2}
    foo.__slots__ = ['1', '2', '3']

# Generated at 2022-06-12 20:00:37.538087
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from _pytest.monkeypatch import MonkeyPatch
    mp = MonkeyPatch()
    mp.setattr('py.io.saferepr', lambda obj: repr(obj))
    from . import frames

    # Setup
    source = 'a'
    main_var = BaseVariable(source)
    exclude = ()
    frame = frames.my_frame()
    frame.f_locals['a'] = 3

    # Test
    items = main_var.items(frame)



# Generated at 2022-06-12 20:00:39.885305
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert CommonVariable('a').items({'a': 1}) == [('a', '1')]


# Generated at 2022-06-12 20:00:50.051898
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import traceback
    from . import debug

    def foo(a, b):
        return a + b

    def bar(c, d):
        foo(c, d)

    def main():
        try:
            bar(1, 2)
        except:
            tb = traceback.extract_stack()
            print(tb[-3])
            print(tb[-2])
            print(tb[-1])
            v = debug.Variables()
            v['a'] = v['b'] = v['c'] = v['d'] = v['foo'] = v['bar'] = v
            v['tb'] = tb
            print(v.items(tb[-2]))

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:00:55.095573
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class Dummy(object):
        pass

    # Data
    d = Dummy()
    d.attr = ''

    # Initialize
    bv = BaseVariable('d')
    # Execute
    actual_result = bv.items(d)
    # Compare
    assert actual_result == [(
        'd',
        repr(d)
    )]



# Generated at 2022-06-12 20:01:09.426879
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # create a frame object
    frame = inspect.currentframe()
    locals().update({'a': 5, 'b': 6, 'c': {'x': 7, 'y': 8}})
    var = Indices('c', exclude=['y'])
    items = var.items(frame)
    assert items == [('c[0]', '7')]
    items = var.items(frame, normalize=True)
    assert items == [('c[0]', '7')]
    var = Attrs('c')
    items = var.items(frame)
    assert items == [('c.x', '7'), ('c.y', '8')]
    items = var.items(frame, normalize=True)
    assert items == [('c.x', '7'), ('c.y', '8')]


# Generated at 2022-06-12 20:01:18.829433
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = StackFrame(None, self)
    for cls in [Attrs, Indices, Keys, Exploding]:
        var = cls('self')
        items = var.items(frame)
        assert isinstance(items, list)
        assert isinstance(items, Sequence)
        for item in items[1:]:
            assert isinstance(item, tuple)
            assert len(item) == 2
            assert isinstance(item[0], str)
            assert isinstance(item[1], str)
test_BaseVariable_items()

# Generated at 2022-06-12 20:01:30.026110
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect

    frame1 = inspect.currentframe()
    frame2 = inspect.currentframe().f_back
    frame3 = inspect.currentframe().f_back.f_back
    frame4 = inspect.currentframe().f_back.f_back.f_back

    # test default exclude of list
    def test_list():
        x = [[0, 1], [2, 3]]
        return x

    assert frame1.f_locals['__builtins__'] == frame2.f_locals['__builtins__'] == frame3.f_locals['__builtins__'] == frame4.f_locals['__builtins__']

# Generated at 2022-06-12 20:01:41.070896
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    main_value = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5}
    # main_value = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5, 'f':[6,7,8]}
    # main_value = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5, 'f':[6,7,8]
    #               'g':(9,10,11)}
    # main_value = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5, 'f':[6,7,8]
    #               'g':(9,10,11)
    #               'h':{'j':12,'k':

# Generated at 2022-06-12 20:01:43.535263
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = Attrs('a.b.c')
    assert len(bv.items(0)) == 0
    assert len(bv.items(None)) == 0


# Generated at 2022-06-12 20:01:48.877142
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    from .utils import getframe

    def f():
        x = 10
        g()

    def g():
        x = getframe()
        source = 'x'
        print(BaseVariable(source).items(x))
        print(Attrs(source).items(x))
        print(Indices(source).items(x))
        print(Exploding(source).items(x))
        print(Exploding(source)[2:5].items(x))
        print(Exploding(source)[:5].items(x))
        print(Exploding(source)[2:].items(x))

    f()

# Generated at 2022-06-12 20:01:50.660816
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect

# Generated at 2022-06-12 20:01:54.923874
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test for NoSuchVariableException
    # if you want to test, write "print(BaseVariable(<source>).items(<frame>))"
    # to line 36.
    print(BaseVariable('abc').items())

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:01:56.403686
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = BaseVariable()
    var.items()
    #TODO: implement the unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:02:02.760111
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from inspect import currentframe
    x = 10
    d = {'1': 10, '2': 20}
    cv = CommonVariable('x')
    cv2 = CommonVariable('d')
    av = Attrs('d')
    kv = Keys('d')
    iv = Indices('d')
    assert cv.items(currentframe()) == [('x', 10)]
    assert av.items(currentframe()) == [('d', {'1': 10, '2': 20})]
    assert kv.items(currentframe()) == [('d', {'1': 10, '2': 20})]
    assert iv.items(currentframe()) == [('d', {'1': 10, '2': 20})]
    kv2 = kv[:]

# Generated at 2022-06-12 20:02:20.229594
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test for Attrs
    attrs = Attrs('p')
    main_value = {'a': 'aa'}
    assert attrs.items(main_value) == [('p', "{'a': 'aa'}")]

    # test for Keys
    keys = Keys('p')
    main_value = {'a':'aa'}
    assert keys.items(main_value) == [('p', "{'a': 'aa'}"), ('p[a]', "'aa'")]

    # test for Indices
    indices = Indices('p')
    main_value = [1, 2, 3]

# Generated at 2022-06-12 20:02:30.083085
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def get_key1_value(val):
        return val['key1']
    def get_key2_value(val):
        return val.key2
    def get_key3_value(val):
        return val[3]
    def get_key4_value(val):
        return val[4]
    def get_index1_value(val):
        return val[1]
    def get_index2_value(val):
        return val[2]
    def get_index3_value(val):
        return val[3]

    class TestClass(object):
        def __init__(self):
            self.key2 = 'value2'
            self.key3 = 'value3'


# Generated at 2022-06-12 20:02:39.063039
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from inspect import currentframe

    d={'a':1,'b':2,'c':3}
    t=(1,2,3,4)

    def test_variable(variable):
        frame = currentframe(sys._getframe().f_back)
        #frame = sys._getframe(1)
        print(variable,file=sys.stdout)
        print(variable.items(frame))
        print('------------------------')

    variable=BaseVariable('d')
    test_variable(variable)

    variable=BaseVariable('d','a')
    test_variable(variable)
    variable=BaseVariable('d','z')
    test_variable(variable)

    variable=BaseVariable('d.a')
    test_variable(variable)

    variable=BaseVariable('t')
    test_variable(variable)
    variable

# Generated at 2022-06-12 20:02:47.598341
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from . import pycompat
    vi = BaseVariable
    v0= vi(source='locals()')
    v1= vi(source='globals')
    v2= vi(source='globals()')
    v3= vi(source='locals()', exclude=tuple(['__builtins__']))
    assert pycompat.is_py3
    # frame = frame of called function
    def foo():
        bar()
    def bar():
        return utils.caller_frame()
    frame = bar()
    items = v0.items(frame)
    items2 = v1.items(frame)
    items3 = v2.items(frame)
    items4 = v3.items(frame)
    assert items[0] == items2[0] == items3

# Generated at 2022-06-12 20:02:49.130319
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass


# Generated at 2022-06-12 20:02:50.375760
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import doctest
    doctest.testmod(BaseVariable)

# Generated at 2022-06-12 20:02:58.765237
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = utils.fake_frame(None)
    frame.f_globals['a'] = 'a'
    frame.f_globals['b'] = {'c': 'c'}
    frame.f_globals['c'] = ['c']

    frame.f_globals['x'] = [1, 2, 3]
    frame.f_globals['y'] = {'a': 1, 'b': 2}
    frame.f_globals['z'] = 'z'
    frame.f_globals['z_x'] = 'z_x'


# Generated at 2022-06-12 20:03:05.511381
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import ast
    import os
    import sys
    import hashlib
    import random

    class VariablesEqual():
        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2
        def __eq__(self, other):
            if (sorted(self.var1)== sorted(self.var2)):
                return True
            else:
                return False

    def basevariable_items(self, frame, normalize=False):
        main_value = eval(self.code, frame.f_globals or {}, frame.f_locals)
        return self._items(main_value, normalize)

    def test_basevariable_items(source):
        exclude = ()
        name = source
        frame = inspect.currentframe

# Generated at 2022-06-12 20:03:08.237931
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Foo:
        def __init__(self):
            self.a = 1

    f = Foo()
    f.b = 2

    frame = inspect.currentframe()
    frame.f_locals['f'] = f

    var = BaseVariable('f')
    for v in var.items(frame):
        print(v)


# Generated at 2022-06-12 20:03:10.825304
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import pycompat
    pycompat.test_items(BaseVariable)
    

# Generated at 2022-06-12 20:03:34.873502
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    d = {}
    frame = utils.Frame(d, d)
    v = BaseVariable('x', exclude='y')
    assert v.items(frame, normalize=True) == ('x', '<unknown>')

    class MyDict(dict):
        pass

    d = MyDict()
    d['x'] = 1
    d['y'] = 2
    v = Keys('d')
    assert v.items(frame, normalize=True) == (('d[x]', '1'), ('d[y]', '2'))
    d = MyList(range(10))
    v = Indices('d')

# Generated at 2022-06-12 20:03:45.573380
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from . import pycompat
    from . import variables_map

    import sys
    import inspect
    from collections import Mapping, Sequence
    from copy import deepcopy
    from . import utils
    from . import pycompat
    from . import variables_map

    def get_type_name(obj, frame):
        module = inspect.getmodule(frame)
        if module:
            module_name = module.__name__

            if utils.is_same_type(obj, type):
                obj = obj.__name__

                if module_name != '__builtin__':
                    obj = module_name + '.' + obj

            elif module_name == '__builtin__':
                obj = type(obj).__name__
        else:
            obj = type(obj).__name__

# Generated at 2022-06-12 20:03:55.184955
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import stdlib_version

    def make_f_locals(**kwargs):
        return type('FakeFrameLocals', (), kwargs)

    def call_items(cls, **kwargs):
        return cls('var', exclude=('x',)).items(make_f_locals(var=kwargs))
 
    if stdlib_version < (3,):
        # keys() and values() were not methods of dict before Python 3.0
        assert call_items(Keys, {1: 10, 'x': 'foo', 2: 30}) == [
            ('var', '{1: 10, 2: 30}'),
            ('var[1]', '10'),
            ('var[2]', '30'),
        ]

# Generated at 2022-06-12 20:03:57.274823
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test case 1: variable_source == 'a'
    variable_source = 'a'
    variable = BaseVariable(variable_source)
    assert variable.source == variable_source
    # Test case 2: variable = explode('x')
    variable = Exploding('x')
    assert variable.source == 'x'

# Generated at 2022-06-12 20:04:04.026975
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import errors
    from .utils import MockFrame
    from .backends.asyncio import AsyncioBackend
    def a(x):
        return x**2

    def b(x):
        raise errors.CustomType(x)

    def c(x=None):
        if x:
            raise KeyError(x)

    def d(*args):
        return a(*args)**2

    def e(x, y):
        return x*y

    def f(x, y=None):
        if y:
            raise KeyError(y)
        return x

    def g(x, y=None):
        if y:
            raise KeyError(y)
        return b(y)


# Generated at 2022-06-12 20:04:10.112777
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = sys._getframe()

    def f():
        return {1: 'one', 2: 'two'}

    var = Keys('f()')
    assert var.items(frame) == [
        ('f()', '{1: \'one\', 2: \'two\'}'),
        ('f()[1]', '\'one\''),
        ('f()[2]', '\'two\'')
    ]


VARIABLES = {
    'attrs': Attrs,
    'indexes': Indices,
    'keys': Keys,
    'explode': Exploding,
}

# Generated at 2022-06-12 20:04:16.484550
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
	# Variables used in test
	a = 1
	b = 2 

	# Test for keywords
	v1 = BaseVariable('a + b')
	assert v1.items(frame) == [('a + b', '3')]

	# Test for sequence
	v2 = BaseVariable('(a, b)')
	assert v2.items(frame) == [('(a, b)', '(1, 2)')]

# Generated at 2022-06-12 20:04:23.121393
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = None
    variables = (
        Attrs('sys', exclude=['executable']),
        Keys('sys.modules', exclude=['__main__']),
        Indices('sys.argv', exclude=['qt']),
        Exploding('sys'),
        Exploding('sys'),
        Exploding('sys.modules'),
        Exploding('sys.modules'),
        Exploding('sys.argv'),
        Exploding('sys.argv')
    )

    assert all(v.items(frame) for v in variables)

# Generated at 2022-06-12 20:04:31.608230
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import traceback
    from .utils import get_traceback

    class _(BaseVariable):
        def _items(self, main_value):
            yield ('', 'base')
            for x in ('a', 'b'):
                try:
                    yield (x, x)
                    for y in ('aa', 'bb'):
                        yield (x + y, y)
                        raise Exception(x)
                except Exception:
                    s = get_traceback(exit=False)
                    yield (x + 'x', s)
                    yield (x + 'y', traceback.format_exc())

    def check(source, *result):
        assert result[::2] == list(zip(*_(source).items(frame)))[0]
        assert result[1::2] == list(zip(*_(source).items(frame)))[1]

   

# Generated at 2022-06-12 20:04:38.903622
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frames
    from .tracer import Tracer
    from .test.test_tracer import BrokenTestCase
    class TestCase(BrokenTestCase):
        def test_bv(self):
            bv = BaseVariable('foo.item')
            frame = frames.Frame(None, globals(), locals())
            bv.items(frame)
            bv.items(frame)
            bv.items(frame)
            bv.items(frame)
    TestCase().test_bv()

# Generated at 2022-06-12 20:05:30.185269
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import LocalVariables

    def func():
        return [object()]

    def test(variables, expected):
        assert variables.items(func.__code__.co_firstlineno) == expected

    # object
    test(LocalVariables.tuple(), ())
    test(LocalVariables.dict(), ())

    # class
    class Foo:
        pass
    test(LocalVariables.tuple(cls=Foo), ())
    test(LocalVariables.dict(cls=Foo), ())

    # instance
    foo = Foo()
    test(LocalVariables.tuple(obj=foo), ())
    test(LocalVariables.dict(obj=foo), ())

    # callable
    test(LocalVariables.tuple(func=func), ())

# Generated at 2022-06-12 20:05:31.516638
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('a').items(sys._getframe()) == ()

# Generated at 2022-06-12 20:05:34.292754
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass


# Generated at 2022-06-12 20:05:43.577963
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    import sys
    import copy
    
    def test_base_variable_items(source, exclude, value, excepted_result, normalize=False):
        variable = BaseVariable(source, exclude)
        frame = sys._getframe()
        frame.f_globals['value'] = value
        result = variable.items(frame, normalize=normalize)
        assert result == excepted_result

    data_str = 'abcdefg'
    data_list = [1, 2, 3, 4, 5, 6]
    data_dict = {'key1': 1, 'key2': 2, 'key3': 3}

# Generated at 2022-06-12 20:05:46.274756
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'value'
    bv = BaseVariable(source)
    result = bv.items()
    assert result == []

# Generated at 2022-06-12 20:05:55.593458
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import test_utils
    from .utils import AssertListEqual

    def dump_tb_info(exc_type, exc_val, exc_tb, variables=()):
        return utils.get_reprs_from_locals(
            variables=variables,
            locals={'__traceback__': exc_tb}
        )

    def check_keys(frame, variables, expected):
        result = dump_tb_info(
            None, None, frame, {
                '__traceback__': frame,
                '_variables': variables
            }
        )
        AssertListEqual(result, expected)

    class A:
        pass

    class B:
        pass

    l = [A(), B()]
    m = {'l': l}


# Generated at 2022-06-12 20:05:58.115487
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    obj = {
        'f': 'f',
        'b': 'a',
    }
    obj['self'] = obj
    bv = BaseVariable(source='self')
    assert bv.items(obj) == ('self', '{0:<3}'.format(obj))


# Generated at 2022-06-12 20:06:07.978036
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .test_utils import MockFrame
    from .test_utils import get_test_repr
    local_variables = {'a': {'b': {'c':1, 'd':'b'}, 'e': [{'x':'y'}, {'z':'p'}]}}
    frame = MockFrame(f_locals=local_variables)

# Generated at 2022-06-12 20:06:15.154702
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Globals
    a = 17
    b = 'banana'
    c = {'one': 1, 'two': 2, 'three': 3}
    d = ('one', 'two', 'three')
    def e():
        pass

    # Local
    f = type(a)

    # test data

# Generated at 2022-06-12 20:06:20.238134
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import dis
    import __main__
    code_obj = compile("x.y", "", "eval")
    code = code_obj.co_code
    code_idx = 0
    while code_idx < len(code):
        op_code = code[code_idx]
        operation = dis.opname[op_code]
        print("\n%s" % operation)
        if operation == "LOAD_ATTR":
            attr_idx = code[code_idx + 1]
            attr_opcode = code_obj.co_names[attr_idx]
            print("   attr:%s" % attr_opcode)
        code_idx = code_idx + 1


# Generated at 2022-06-12 20:07:50.464362
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = BaseVariable(source="name")
    assert var.items()==()


# Generated at 2022-06-12 20:07:57.070712
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [('variable', main_value)]
    
    class TestFrame:
        def __init__(self, main_value):
            self.f_locals = {}
            self.f_locals['main_value'] = main_value

        def get_var(self, var):
            var.items(self, normalize=False)

    # test for int
    frame = TestFrame(42)
    var = TestVariable('main_value')
    result = var.items(frame, normalize=False)
    test_result = [('main_value', '42')]
    assert result == test_result, "BaseVariable.items(frame) method fails"

# Generated at 2022-06-12 20:08:05.838975
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import frame_var
    frame_var.context = [frame_var.context[0][0]]
    frame_var.vars = {
        "name": "abc",
        "a": {"b": {"name": "abc"}},
        "c": {"b": {"name": "abc"}}
    }
    utils.logger.info('>>> Variable: name')
    var = BaseVariable('name')
    res = [(k, v) for k, v in var.items(var.code.co_filename)]
    utils.logger.info('name: {}'.format(res))
    assert res == [('name', 'abc')]
    utils.logger.info('>>> Variable: a.b')
    var = BaseVariable('a.b')

# Generated at 2022-06-12 20:08:14.737198
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class A(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __int__(self):
            return self.x + self.y

    class B(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __index__(self):
            return self.x + self.y
        def __abs__(self):
            return abs(self.x)

    class C(object):
        def __init__(self, x):
            self.x = x
        def __index__(self):
            return self.x
        def __abs__(self):
            return abs(self.x)
        def __float__(self):
            return self.x + 0.

# Generated at 2022-06-12 20:08:22.645085
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def foo1():
        a = 1
        return bar1()

    def bar1():
        b = 2
        return c

    def foo2():
        a = 1
        return bar2()

    def bar2():
        b = 2
        return c()

    def foo3():
        a = 1
        return bar3()

    def bar3():
        b = 2
        return c().x

    def foo4():
        a = 1
        return bar4()

    def bar4():
        b = 2
        return c.x

    def foo5():
        a = 1
        return bar5()

    def bar5():
        b = 2
        return c[3]

    def foo6():
        a = 1
        return bar6()

    def bar6():
        b = 2
        return c

# Generated at 2022-06-12 20:08:26.120736
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    main_value = utils.get_test_var()
    topframe = inspect.currentframe().f_back
    while True:
        print(topframe.f_code.co_name)
        if topframe.f_code.co_name == 'test_BaseVariable_items':
            break
        topframe = topframe.f_back
    for source, value in BaseVariable(main_value).items(topframe):
        print(source + ": " + value)

# Generated at 2022-06-12 20:08:27.964193
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert list(BaseVariable('a', '').items(None, normalize=False)) == []
    #assert list(BaseVariable('a', '').items(frame)) == []
    #assert list(BaseVariable('a', '').items(frame, normalize=True)) == []


# Generated at 2022-06-12 20:08:33.561956
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()

    def assert_items(expected):
        for source, value in expected:
            assert (source, value) in BaseVariable(source).items(frame)
