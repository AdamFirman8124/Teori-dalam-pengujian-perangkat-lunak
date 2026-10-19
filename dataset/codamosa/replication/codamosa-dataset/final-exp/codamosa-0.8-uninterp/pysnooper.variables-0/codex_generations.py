

# Generated at 2022-06-12 19:58:54.786403
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class VariableA(BaseVariable):
        def __init__(self, source, exclude=()):
            super().__init__(source, exclude)

        def _items(self, main_value, normalize=False):
            return ()

    assert VariableA('a') == VariableA('a')
    assert VariableA('a') == VariableA('a', exclude=('b', ))
    assert VariableA('a', exclude=('b', )) == VariableA('a', exclude=('b', ))
    assert VariableA('a') != VariableA('a', exclude=('b', ))
    assert VariableA('a', exclude=('b', )) != VariableA('a')
    assert VariableA('a') != VariableA('b')
    assert VariableA('a', exclude=('b', )) != VariableA('b', exclude=('b', ))

#

# Generated at 2022-06-12 19:58:57.715838
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    source = 'my_variable'
    var = Indices(source)
    assert var[:]._slice == slice(None)
    assert var[1:5]._slice == slice(1, 5)

# Generated at 2022-06-12 19:59:01.504322
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    variable = Indices('foo', exclude=('bar', 'baz'))[1:5]
    assert variable == Indices('foo', exclude=('bar', 'baz'))[1:5]
    assert variable != Indices('foo', exclude=('bar', 'baz'))[2:5]

# Generated at 2022-06-12 19:59:05.497221
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, main_value)]

    var = MyVariable('test')
    assert var.items({'test': 1}) == [('test', 1)]

# Generated at 2022-06-12 19:59:07.345493
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("x")
    v2 = BaseVariable("x")
    assert v1 == v2



# Generated at 2022-06-12 19:59:12.281767
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('i').__eq__(BaseVariable('i'))
    assert BaseVariable('i').__eq__(BaseVariable('i', exclude=''))
    assert BaseVariable('i', exclude='').__eq__(BaseVariable('i'))

    assert not BaseVariable('i').__eq__(BaseVariable('i', exclude='a'))
    assert not BaseVariable('i', exclude='a').__eq__(BaseVariable('i'))

    assert BaseVariable('i').__eq__(Attrs('i'))
    assert BaseVariable('i').__eq__(Keys('i'))
    assert BaseVariable('i').__eq__(Indices('i'))

    assert not BaseVariable('i').__eq__(Exploding('i'))
    assert not Attrs('i').__eq__(Exploding('i'))
   

# Generated at 2022-06-12 19:59:24.308029
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test for method items of class BaseVariable
    from .test_utils import parse_and_run
    src = '''
    def foo(x):
        y = 33
        return x
    foo(1)
    '''
    initial_code_coverage = parse_and_run(src, 'foo', "foo(1)")
    
    # test for class Attrs
    src = '''
    class A:
        def __init__(self, x):
            self.x = x
        def foo(self):
            y = 33
            return self.x
    A(1).foo()
    '''
    attr1 = parse_and_run(src, 'A.__init__', "A(1)")

# Generated at 2022-06-12 19:59:32.674052
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class X(BaseVariable):
        def __init__(self, int1, int2, int3):
            self.i1 = int1
            self.i2 = int2
            self.i3 = int3

    x1 = X(1, 2, 3)
    x2 = X(1, 2, 3)
    x3 = X(4, 5, 6)
    print(x1 == x2)    # True
    print(x1 == x3)    # False
    print(x2 == x3)    # False


# Generated at 2022-06-12 19:59:40.535063
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from contextlib import contextmanager
    from io import StringIO
    import builtins
    original_print = builtins.print
    my_print_stream = StringIO()
    builtins.print = my_print_stream.write
    my_print_stream.truncate(0)
    my_print_stream.seek(0)

    @contextmanager
    def capture_print():
        from contextlib import contextmanager
        from io import StringIO
        import builtins
        original_print = builtins.print
        my_print_stream = StringIO()
        builtins.print = my_print_stream.write
        my_print_stream.truncate(0)
        my_print_stream.seek(0)
        yield my_print_stream
        builtins.print = original_print

# Generated at 2022-06-12 19:59:47.186020
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def attrs(source):
        return Attrs(source).items(frame)

    def keys(source):
        return Keys(source).items(frame)

    def indices(source):
        return Indices(source).items(frame)

    def exploding(source):
        return Exploding(source).items(frame)

    g = {'some_module': some_module}
    frame = sys._getframe()
    frame.f_globals = g
    # g.update(frame.f_locals)

# Generated at 2022-06-12 19:59:56.247052
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from okonomiyaki.tests.utils import FakeFrame
    v = BaseVariable('a')
    assert v.items(FakeFrame({'a': 0})) == [('a', '0')]
    assert v.items(FakeFrame({'a': 1})) == [('a', '1')]


# Generated at 2022-06-12 20:00:07.837073
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import dis
    import random

    class C(object):
        x = 1
        y = 2

    utils.assert_not_raises(BaseException, locals(), globals())

    def items_test(f, n=100):
        for i in range(n):
            if i == n // 2:
                C.x = object()
            items = list(f(lambda: random.random()))
            dis.dis(f.__code__)
            for instruction in f.__code__.co_code:
                print(inspect.stack())
            assert items == [('x', 1)]

    items_test(lambda: C.x)
    items_test(lambda: C.x.y)
    items_test(lambda: (1, 2, 3)[C.x.y])


test

# Generated at 2022-06-12 20:00:10.887523
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Child(BaseVariable):
        def _items(self, key, normalize=False):
            return [(self.source, utils.get_shortish_repr(key))]
    obj = Child('a')
    assert obj.items(1) == [('a', '1')]

# Generated at 2022-06-12 20:00:20.185856
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from . import testutils
    from .testutils import strcontains
    from ..log import logger
    
    with testutils.temporary_directory() as tmpdir:
        with logger.catch_logs(tmpdir) as logs:
            testutils.make_executable_test_file(tmpdir, '''
                import os
                import pytest
                if hasattr(os, 'listdir'):
                    try:
                        os.listdir()
                    except OSError:
                        pass
                    else:
                        pytest.fail('Expected OSError')
                pytest.skip('os.listdir does not exist')
            ''')
            testutils.run_testdir(tmpdir, '-rX')
            assert strcontains(logs.out, 'line 5, *)')
            assert not strcont

# Generated at 2022-06-12 20:00:25.539062
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a', exclude=['x']) == BaseVariable('a', exclude=['x'])
    assert not (BaseVariable('a') == BaseVariable('b'))
    assert not (BaseVariable('a', exclude=['x']) == BaseVariable('a', exclude=['y']))

# Generated at 2022-06-12 20:00:34.997519
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    # Should work with a start
    indices1 = Indices('a')[1:]
    assert indices1._slice == slice(1, None, None)

    # Should work with a stop
    indices2 = Indices('a')[:1]
    assert indices2._slice == slice(None, 1, None)

    # Should work with an explicit step
    indices3 = Indices('a')[1:2:3]
    assert indices3._slice == slice(1, 2, 3)

    # Should work with a negative stop
    indices4 = Indices('a')[:-2]
    assert indices4._slice == slice(None, -2, None)

    # Should work with a negative start
    indices5 = Indices('a')[-1:]
    assert indices5._slice == slice(-1, None, None)

    # Should

# Generated at 2022-06-12 20:00:40.842448
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:00:41.498045
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:00:50.998208
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from .utils import is_string

    def _index(index, *args):
        return args[index]

    def _get_type_of_variable(index, *args):
        return type(args[index])

    def _convert_variable_to_string(index, *args):
        return str(args[index])

    def _dict_to_tuples(index, *args):
        if isinstance(args[index], dict):
            return tuple(args[index].items())
        else:
            return args[index]

    def _tuple_to_lists(index, *args):
        return [list(list_to_list) for list_to_list in args[index]]


# Generated at 2022-06-12 20:00:59.282284
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global result
    result = []
    class A:
        a = 1
        b = 2
        def __init__(self, x):
            self.x = x
    a = A(3)
    for v in ('x', 'a', 'v'):
        for cls in (Attrs, Keys, Indices):
            var = cls(v)
            result = var.items(frame = locals())
    var = Exploding('a')
    result = var.items(frame = locals())
    #print('result =', result)

test_BaseVariable_items()

# Generated at 2022-06-12 20:01:10.448704
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # base variable
    assert BaseVariable("a") == BaseVariable("a")
    assert BaseVariable("a") == BaseVariable("a",("a","b"))
    assert BaseVariable("a",("a","b")) == BaseVariable("a")
    assert BaseVariable("a") != BaseVariable("b")
    assert BaseVariable("a",("a","b")) != BaseVariable("a",("a","b","c"))
    # other variable
    assert BaseVariable("a") == Attrs("a")
    assert BaseVariable("a") == Attrs("a",("a","b"))
    assert BaseVariable("a") != Attrs("a",("a","b","c"))



# Generated at 2022-06-12 20:01:15.867816
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('x', 'y') == BaseVariable('x', 'y')
    assert BaseVariable('x', 'y') != BaseVariable('x', 'z')
    assert BaseVariable('x', 'y') != BaseVariable('a', 'z')


# Generated at 2022-06-12 20:01:19.186092
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
	a = {'b': [1, 2, 3]}
	assert Indices('a').__getitem__(slice(0, 1)) == (Indices('a', exclude=('b',)))._items(a)

# Generated at 2022-06-12 20:01:24.997969
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    var1 = Indices('a', exclude=('foo',))
    var2 = var1[5:10]
    assert isinstance(var2, Indices)
    assert var2._slice == slice(5, 10)
    assert var2.source == 'a'
    assert var2.exclude == ('foo',)


# Generated at 2022-06-12 20:01:27.885739
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    v = BaseVariable('sys', exclude=['argv'])
    for k,v in v.items(sys._getframe()):
        print(k,v)


# Generated at 2022-06-12 20:01:29.200094
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')



# Generated at 2022-06-12 20:01:31.059359
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = "locals().items()"
    v1 = BaseVariable(source)
    v2 = BaseVariable(source)
    assert v1 == v2

# Generated at 2022-06-12 20:01:37.591101
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = pycompat.fake_frame()
    frame.f_locals = {'test': {'test_test'}}
    assert BaseVariable('test').items(frame) == (('test', '{...}'),)
    assert BaseVariable('test').items(frame, normalize=True) == (('test', '{"test_test": None}'),)
    assert BaseVariable('test', 'test_test').items(frame) == (('test', '{...}'),)
    assert BaseVariable('test', 'test_test').items(frame, normalize=True) == (('test', '{"test_test": None}'),)
    assert Attrs('test').items(frame) == (('test', '{...}'), ('test.test_test', None))
    assert Attrs('test').items(frame, normalize=True)

# Generated at 2022-06-12 20:01:44.867998
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import pycompat
    from .utils import get_shortish_repr
    from .tracer import Tracer

    global source, main_value, result
    source = 'whatever'
    main_value = 'any_value'

    def _items(self, frame, normalize=False):
        global result
        result = True
        return [(source, get_shortish_repr(main_value, normalize=normalize))]

    tracer = Tracer()
    tracer.variable_class.items = _items
    tracer.start()
    tracer.stop()

    assert result



# Generated at 2022-06-12 20:01:47.049115
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert (BaseVariable('x',exclude=(1,2)) == BaseVariable('x',exclude=(1,2)))
    assert not (BaseVariable('x',exclude=(1,2)) == BaseVariable('x',exclude=(2,1)))

# Generated at 2022-06-12 20:02:00.806177
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from pprint import pprint
    from . import local
    try:
        from .fake import FakeFrame
    except ImportError:
        from . import fake
        FakeFrame = fake.FakeFrame
    class Dummy:
        pass
    class DummySub(Dummy):
        pass
    class DummySlotted(Dummy):
        __slots__ = ('a',)
    class DummySuper(Dummy):
        pass
    class DummyB(Dummy):
        pass
    dummy = Dummy()
    dummysub = DummySub()
    dummyslotted = DummySlotted()
    dummysuper = DummySuper()
    dummysuper.a = DummyB()
    dummysuper.b = DummyB()
    dummydict = dict(a=1, b=2)

# Generated at 2022-06-12 20:02:05.694798
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = BaseVariable('a')
    a2 = BaseVariable('a')
    b = BaseVariable('b')
    assert a1 == a2
    assert a1 != b
    assert a2 != b


# Generated at 2022-06-12 20:02:10.708122
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    x = 1
    y = 2
    main_value = BaseVariable('y')
    m = main_value.items(frame=None, normalize=False)
    assert str(m) == "(('y', 2),)"

    x = 1
    y = 2
    main_value = BaseVariable('x')
    m = main_value.items(frame=None, normalize=False)
    assert str(m) == "(('x', 1),)"


# Generated at 2022-06-12 20:02:15.623729
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert not BaseVariable("a") == 1

    assert not BaseVariable("a") == BaseVariable("b")
    assert BaseVariable("a") == BaseVariable("a")

    assert not BaseVariable("a") == BaseVariable("a", "b")
    assert not BaseVariable("a", "b") == BaseVariable("a")
    assert BaseVariable("a", "b") == BaseVariable("a", "b")



# Generated at 2022-06-12 20:02:19.135520
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('').items({}) == ()
    assert Attrs('').items({}) == ()
    assert Attrs('foo').items({'foo': 'bar'}) == (('foo', "'bar'"))


# Generated at 2022-06-12 20:02:25.948922
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(BaseVariable):
            def _items(self, key, normalize=False):
                if key == 'toto':
                    return (('tata', 'titi'),)
                else:
                    return ()
    frame = {
        'toto': 'tutu'
    }
    assert MyVariable('toto').items(frame) == []
    assert MyVariable('toto').items(frame) == [('tata', 'titi')]

# Generated at 2022-06-12 20:02:34.497862
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .container import Container

    # Instantiating a Container object
    obj = Container()

    """    
    Container object of class Container is made available to the namespace
    of the caller using keyword argument "globals". This is a requirement
    for method items of class BaseVariable to work.
    """


    # Instantiating a Keys object
    k = Keys('obj')

    # Accessing the attribute items of object k
    items = k.items(globals())

    # Checking that items is a sequence
    assert(isinstance(items, tuple))

    # Checking that items is not empty
    assert(len(items) > 0)

    # Checking that the first element of items is a tuple
    assert(isinstance(items[0], tuple))

    # Checking that the second element of items is a string

# Generated at 2022-06-12 20:02:44.359267
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from sys import getsizeof

    a = dict(one=11, two=22, three=33)
    b = dict(eleven=11, twelve=22, thirteen=33)
    c = 'hello world'
    d = ['foo', 'bar', 'baz']
    e = dict(a=a, b=b, c=c, d=d)

    def size_helper(g, a):
        """Helper for getting the size of 2 byte strings"""
        return getsizeof(g) + getsizeof(a)

    e_size = size_helper('e', '.') + sum(size_helper(k, '') for k in ['a', 'b', 'c', 'd'])

# Generated at 2022-06-12 20:02:49.174203
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable("a")
    b = BaseVariable("a")
    c = BaseVariable("b")
    d = BaseVariable("a", "b")
    e = BaseVariable("a", "b")
    assert a == b
    assert a != c
    assert d == e
    assert d != a
    assert d != c


# Generated at 2022-06-12 20:02:57.987362
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class BaseVariable(pycompat.ABC):
        def __init__(self, source, exclude=()):
            self.source = source
            self.exclude = utils.ensure_tuple(exclude)
            self.code = compile(source, '<variable>', 'eval')
            if needs_parentheses(source):
                self.unambiguous_source = '({})'.format(source)
            else:
                self.unambiguous_source = source

        def items(self, frame, normalize=False):
            try:
                main_value = eval(self.code, frame.f_globals or {}, frame.f_locals)
            except Exception:
                return ()
            return self._items(main_value, normalize)


# Generated at 2022-06-12 20:03:19.693144
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'test'
    exclude = 'test'
    v1 = BaseVariable(source, exclude)
    v1.code = compile(source, '<variable>', 'eval')
    v2 = BaseVariable(source, exclude)
    v2.code = compile(source, '<variable>', 'eval')
    v3 = BaseVariable(source, exclude)
    v3.code = compile(source, '<variable>', 'exec')
    assert v1 == v2
    assert not v1 == v3
    source = 'test'
    exclude = 'test'
    v1 = BaseVariable(source, exclude)
    v1.code = compile(source, '<variable>', 'eval')
    v2 = BaseVariable(source, exclude)
    v2.code = compile(source, '<variable>', 'eval')

# Generated at 2022-06-12 20:03:30.449559
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import contextlib
    import sys
    import io

    @contextlib.contextmanager
    def capture_streams(stdout=None, stderr=None):
        '''
        Context manager that captures the output to sys.stdout and/or
        sys.stderr, to be restored once the context exits.
        '''
        oldout, olderr = sys.stdout, sys.stderr

# Generated at 2022-06-12 20:03:34.835661
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import collections
    import types
    import functools

    format = functools.partial(lambda s: '<{}>'.format(s), inspect.getabsfile(inspect.currentframe()))

    def fake_frame(**locals):
        return types.SimpleNamespace(f_locals=locals)


# Generated at 2022-06-12 20:03:38.117916
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = BaseVariable('a')
    a2 = BaseVariable('a')
    a3 = BaseVariable('b')
    assert (a1 == a2)
    assert not (a1 == a3)



# Generated at 2022-06-12 20:03:48.146697
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = utils.FakeFrame()
    frame.f_locals = {'d': {'x': 1, 'y': 2}}

    v = Keys('d')
    assert v.items(frame) == [('d', "'{x: 1, y: 2}'"), ('d[x]', '1'), ('d[y]', '2')]

    v = Indices('d')
    assert v.items(frame) == [('d', "'{x: 1, y: 2}'"), ('d[0]', '1'), ('d[1]', '2')]

    v = Exploding('d')
    assert v.items(frame) == [('d', "'{x: 1, y: 2}'"), ('d[x]', '1'), ('d[y]', '2')]

# Unit test

# Generated at 2022-06-12 20:03:49.741479
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BaseVariable() == BaseVariable()



# Generated at 2022-06-12 20:03:54.991115
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class TestClass(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]

    test1 = TestClass('a', 'b')
    test2 = TestClass('a', 'b')
    assert test1 == test2

# Generated at 2022-06-12 20:03:59.276819
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from pprint import pprint

    class F:
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return 'F({})'.format(self.x)

    class G:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'G({}, {})'.format(self.x, self.y)

    b = {}

    def foo(x, y):
        a = F(x)
        b['x'] = 1
        return G(a, a.x)

    i = Indices('something')

# Generated at 2022-06-12 20:04:05.246565
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    x = 1
    frame = inspect.currentframe()
    result_Attrs = Attrs('x').items(frame)
    assert result_Attrs == [('x', "1"), ('x.__class__', "int")]
    result_Indices = Indices("[x,x]").items(frame)
    assert result_Indices == [("[x,x]", "[1, 1]"), ("[x,x][0]", "1"), ("[x,x][1]", "1")]

# Generated at 2022-06-12 20:04:07.383132
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
	bv1 = BaseVariable(source="", exclude=())
	bv2 = BaseVariable(source="", exclude=())
	assert bv1 == bv2


# Generated at 2022-06-12 20:04:43.877649
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import operator as op
    import sys
    import os
    import random as rd
    import string as st

    # Ensure it only works for Python 3.6+
    f = lambda a, b: (a*b)**2
    func = """
        def f(a, b):
            return (a * b) ** 2
    """
    var = sys._getframe().f_code.co_name
    var = var[:-1] + ' ' + var[-1]
    try:
        name = next(n for n, v in inspect.getmembers(op, inspect.isbuiltin) if v is f)
    except StopIteration:
        name = 'f'
    name = os.path.basename(__file__) + '.' + name

    # Source and exclude

# Generated at 2022-06-12 20:04:47.881339
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys
    import inspect_fixtures.testspecs.explode
    frame = inspect.currentframe()
    while frame is not None:
        if frame.f_code.co_filename.endswith('testspecs/explode.py'):
            break
        frame = frame.f_back
    assert frame
    cvar = CommonVariable('x.y')
    assert cvar.items(frame) == [('x.y', "dict_keys(['z', 'a'])")]


VARIABLES = {'attrs': Attrs, 'keys': Keys, 'indices': Indices, 'explode': Exploding}

# Generated at 2022-06-12 20:04:56.342290
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class test_cls(BaseVariable):
        def __init__(self, source, exclude=()):
            self.source = source
            self.exclude = utils.ensure_tuple(exclude)
            self.code = compile(source, '<variable>', 'eval')
            if needs_parentheses(source):
                self.unambiguous_source = '({})'.format(source)
            else:
                self.unambiguous_source = source

        def _items(self, key, normalize=False):
            print("Main key is:", key)
            results = []
            for keys in self._safe_keys(key):
                try:
                    if keys in self.exclude:
                        continue
                    values = self._get_value(key, keys)
                except Exception:
                    continue

# Generated at 2022-06-12 20:05:07.046353
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # call self.items() of class BaseVariable with the given inputs
    # and check the result
    # args: input parameters, expected: expected result
    # skip: IDs of the test cases to be skipped
    def __test(t, args, expected, skip=()):
        if t.case_id in skip:
            t.skipTest('skipped')
        if args:
            res = t.test_object.items(*args)
        else:
            res = t.test_object.items()
        t.assertEqual(res, expected)

    from unittest import TestCase
    import six

    # generate test cases
    if six.PY2:
        raise RuntimeError('Python 2 is not supported yet'
                           ' because importlib is not available')
    import importlib

    from . import pycompat

# Generated at 2022-06-12 20:05:17.229099
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect

    class Test(object):
        def __init__(self, a, b=None, c=1):
            self.a = a
            self.b = b
            self.c = c

        def foo(self, bar, baz=None):
            return bar * self.c + baz

    with open(inspect.getsourcefile(sys._getframe(1))) as f:
        source_lines = f.readlines()

    v = BaseVariable('frame')
    result = v.items(sys._getframe(1), True)
    print(result)
    assert result == [('frame', '<frame ' + str(sys._getframe(1).f_lineno) + '>')]

    v = BaseVariable('a')

# Generated at 2022-06-12 20:05:20.960497
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = utils.FakeFrame()
    frame.f_globals = {'x': 3}
    frame.f_locals = {'y': 4}
    assert Keys('x').items(frame) == [('x', '3')]
    assert Keys('y').items(frame) == [('y', '4')]
    assert Keys('x').items(frame) == [('x', '3')]


# Generated at 2022-06-12 20:05:27.187369
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return [('MyKey', utils.get_shortish_repr(key))]
    v = MyVariable('variable_name')
    items = v.items({'variable_name':[1,2,3]})
    assert items == [('variable_name', '[1, 2, 3]')]



# Generated at 2022-06-12 20:05:32.705463
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # mock frame and globals
    frame = MagicMock()
    frame.f_globals = {'foo': 1}
    frame.f_locals = {'foo': 0}

    # test index of list
    index = Indices("foo")
    index.items(frame)

    # test key of dict
    key = Keys("foo")
    key.items(frame)

    # test item of obj
    item = Attrs("foo")
    item.items(frame)

    # test exploding item
    explode = Exploding("foo")
    explode.items(frame)



# Generated at 2022-06-12 20:05:38.120788
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    b = BaseVariable('d')
    test_dict = {'a': 1}
    assert b.items(test_dict) == [('1','1')]  # Test single character
    assert b.items(test_dict, True) == [('1','1')]  # Test normalize True


# Generated at 2022-06-12 20:05:45.783903
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import numpy as np
    frame = inspect.currentframe()
    x = [1, 2, 3]
    a = np.array([1, 2, 3])
    m = {'a': 1}
    c = {'a': 1, 'b': 'abc'}
    t = (1, 2, 3)
    r = range(1, 10)
    l = [m, c, t, r]
    h = ['1', '2', '3', l]
    f = {'a': [1, 2, 3], 'b': a}
    z = {'x': x, 'a': a, 'm': m, 'c': c, 't': t, 'r': r, 'l': l, 'h': h, 'f': f}

# Generated at 2022-06-12 20:06:42.126902
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import numpy as np
    import pandas as pd
    import datetime
    x = np.array([1,2,3])
    y = pd.DataFrame({'a':[1,2,3]})
    z = datetime.date.today()
    variables = [x,y,z]
    for variable in variables:
        assert type(variable) in [type(x),type(y),type(z)]
        assert len(type(variable).__mro__) == 2
        assert type(variable) in [np.ndarray,pd.core.frame.DataFrame,datetime.date]
        assert isinstance(type(variable)(),type(x))
        assert isinstance(type(variable)(),type(y))
        assert isinstance(type(variable)(),type(z))

# Generated at 2022-06-12 20:06:51.389352
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pytest
    from pytest import raises
    
    class foo():
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    
    a = foo(1, 2, 3)
    b = foo(1, 2, 3)
    b.a = 4
    c = foo(1, 2, 3)
    c.a = foo(1, 2, 3)
    
    example1 = [{'a': 2, 'b': 3}, [1, 2, 3, 4, 5], a]
    example2 = [{'a': 2, 'b': 3}, [1, 2, 3, 4, 5], b]

# Generated at 2022-06-12 20:07:01.104664
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    stack = utils.Stack()[0]
    attrs = stack.attrs
    assert len(attrs) == 5
    assert attrs[0][0] == 'self'
    assert attrs[0][1] == 'Instance of class class with id id'
    assert attrs[1][0] == 'self.__class__'
    assert attrs[1][1] == 'Instance of class class with id id'
    assert attrs[2][0] == 'self.__class__.__name__'
    assert attrs[2][1] == 'class'
    assert attrs[3][0] == 'self.__class__.__mro__'
    assert attrs[3][1] == ('Instance of class tuple with id id',
                           'Instance of class type with id id', 'object')

# Generated at 2022-06-12 20:07:09.138887
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'request'
    main_value = ['a','b','c','d']
    frame = type('Frame', (object,), {'f_globals':{},'f_locals':{
        'request': main_value,
    }})()
    base = BaseVariable(source)
    assert base.items(frame) == [
        ('request', "['a', 'b', 'c', 'd']"),
    ]

if __name__ == '__main__':
    import pytest
    pytest.main(['-s', __file__])
    exit()

# Generated at 2022-06-12 20:07:17.778861
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # given
    import sys
    sys.setrecursionlimit(sys.getrecursionlimit() * 4)

    class A():
        def __init__(self, x):
            self.x = x

    class B(A):
        def __init__(self, x, y):
            super().__init__(x)
            self.y = y

        def __repr__(self):
            return 'B({}, {})'.format(self.x, self.y)

    class C(A):
        def __init__(self, x, y):
            super().__init__(x)
            self.y = y

        def __repr__(self):
            return 'C({}, {})'.format(self.x, self.y)

        def __getitem__(self, item):
            return self

# Generated at 2022-06-12 20:07:28.737825
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    tp = type('', (), {})()
    tp2 = type('', (), {})()

# Generated at 2022-06-12 20:07:39.168122
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import re
    # Test Case 1:
    # test_frame
    # > import re
    # > dir(re)
    # ['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_cache_repl', '_compile

# Generated at 2022-06-12 20:07:49.068724
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    from . import utils
    from . import pycompat

    class Foo(object):
        pass

    obj = Foo()
    obj.a = 1
    obj.b = 2
    obj.c = 3

    stack_frame = pycompat.get_frame_info(inspect.currentframe())
    stack_frame.f_locals['obj'] = obj
    stack_frame.f_globals['get_wrap_info'] = utils.get_wrap_info

    source = 'obj.a'
    exclude = 'c'
    expected_result = [(source, '1'), ('obj.b', '2')]
    result = BaseVariable(source, exclude).items(stack_frame)
    assert result == expected_result
    # Negative cases
    source2 = 'a'

# Generated at 2022-06-12 20:07:54.509964
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class X(object):
        abc = 3
        def __str__(self):
            return 'X'
        def __getitem__(self, item):
            return self.abc if isinstance(item, int) else 'hi'

    frame = None
    base = BaseVariable('x', exclude=('abc',))
    result = {'abc', 'hi', 'X'}
    assert set(base.items(frame, normalize=True)) == result



# Generated at 2022-06-12 20:08:03.962338
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import math
    frame = inspect.currentframe()
    v_a = BaseVariable('a')
    print('test_BaseVariable_items(): Test case 1')
    v_a_items = v_a.items(frame)
    y_a_items = [('a', '2')]
    assert v_a_items == y_a_items, '''v_a.items(frame) != y_a_items'''
    print('test_BaseVariable_items(): Test case 2')
    v_a_items = v_a.items(frame, normalize=True)
    y_a_items = [('a', '2')]
    assert v_a_items == y_a_items, '''v_a.items(frame, normalize=True) != y_a_items'''
    