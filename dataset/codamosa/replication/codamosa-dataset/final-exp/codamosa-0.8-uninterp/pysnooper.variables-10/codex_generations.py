

# Generated at 2022-06-12 19:58:46.164390
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    idx = Indices('t1')
    idx = idx[1:3]
    assert idx._slice.start == 1
    assert idx._slice.stop == 3
    return
# unit tests for method get_var_names_for_frame of class utils

# Generated at 2022-06-12 19:58:50.179228
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    t1 = Indices('foo')[:]
    print(t1._slice)
    t2 = Indices('foo')[3:7]
    print(t2._slice)
    t3 = Indices('foo')[::2][3:]
    print(t3._slice)

test_Indices___getitem__()

# Generated at 2022-06-12 19:58:51.576938
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("request", "request.user") == BaseVariable("request", "request.user")


# Generated at 2022-06-12 19:58:57.487180
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    _test_exploding_variable('a', {'a': 'b'})
    _test_exploding_variable('a.b', {'a': {'b': {'c': 'd'}}})
    _test_exploding_variable('a.b.c', {'a': {'b': {'c': 'd'}}})
    _test_exploding_variable('a[b]', {'a': {'b': {'c': 'd'}}})
    _test_exploding_variable('a.b[c]', {'a': {'b': {'c': 'd'}}})
    _test_exploding_variable('a[b].c', {'a': {'b': {'c': 'd'}}})

# Generated at 2022-06-12 19:58:58.905440
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = Attrs('a')
    a.items(3)



# Generated at 2022-06-12 19:58:59.725040
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    example_ = Indices("example")
    assert example_[:] == Indices("example")

# Generated at 2022-06-12 19:59:03.225091
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    obj = Indices("main_value")
    newobj = obj[::2]
    assert type(newobj) == Indices
    assert newobj._slice == slice(None, None, 2)
    assert newobj._fingerprint != obj._fingerprint



# Generated at 2022-06-12 19:59:12.018285
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # prepare some test cases
    a_dict = {"a" : 1, "b" : 2, "c" : 3}
    a_list = [1, 2, 3]
    a_set = {1, 2, 3}
    a_tuple = (1, 2, 3)
    a_obj = type('A', (object, ), {'a': 1, 'b': 2, 'c': 3})
    i = iter([1, 2, 3])

    # test for class Attrs
    v = Attrs("dict")
    assert v.items(F_GLOBALS) == [("dict", "dict(a=1, b=2, c=3)")]
    assert v.items(F_GLOBALS, normalize=True) == [("dict", "dict(...)")]

    v = Attrs

# Generated at 2022-06-12 19:59:16.492827
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Tester(BaseVariable):
        def _items(self, main_value, normalize=False):
            return main_value
    tester = Tester('main_value')
    assert tester.items({'main_value': 'value'}) == 'value'


# Generated at 2022-06-12 19:59:26.933540
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from abc import ABCMeta, abstractmethod
    from . import variables

    class BaseA(object):
        __metaclass__ = ABCMeta

        def __init__(self, source, exclude=()):
            self.source = source
            self.exclude = utils.ensure_tuple(exclude)

        @abstractmethod
        def items(self, frame, normalize=False):
            pass

        @property
        def _fingerprint(self):
            return (type(self), self.source, self.exclude)

        def __hash__(self):
            return hash(self._fingerprint)

        def __eq__(self, other):
            return (isinstance(other, BaseA) and
                                       self._fingerprint == other._fingerprint)


    class ClassA(BaseA):
        pass

   

# Generated at 2022-06-12 19:59:40.994154
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class A:
        a = 1

    a = A()
    assert list(Attrs('a').items(fake_frame(A, a))) == [
        ('a', '<__main__.A object at 0x...>'),
        ('a.a', '1')
    ]
    assert list(Keys('a').items(fake_frame(A, a))) == []
    assert list(Indices('a').items(fake_frame(A, a))) == []

    assert list(Attrs('a').items(fake_frame(A, a), normalize=True)) == [
        ('a', '<__main__.A object at 0x...>'),
        ('a.a', '1')
    ]
    assert list(Keys('a').items(fake_frame(A, a), normalize=True)) == []
   

# Generated at 2022-06-12 19:59:50.062947
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import variables
    from .pycompat import unicode
    
    var = variables.CommonVariable('x', exclude='y')
    assert var == var
    
    var2 = variables.CommonVariable('x', exclude='y')
    assert var == var2
    assert var2 == var
    
    var3 = variables.CommonVariable('y', exclude='y')
    assert var != var3
    assert var3 != var
    
    var4 = variables.CommonVariable('x', exclude='x')
    assert var != var4
    assert var4 != var
    
    var5 = variables.CommonVariable(unicode('x'), exclude='y')
    assert var == var5
    assert var5 == var

# Generated at 2022-06-12 19:59:54.884764
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a')
    v2 = BaseVariable('a')
    v3 = BaseVariable('b')
    assert v1 == v2
    assert v1 != v3


# Generated at 2022-06-12 19:59:58.385930
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import pprint
    frame = inspect.currentframe()
    bv = BaseVariable('frame')
    print(bv.items(frame))
    pprint.pprint(bv.items(frame))
    print(bv.items(frame, normalize=True))


# Generated at 2022-06-12 20:00:08.694337
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = utils.get_frame('utils.py')
    var = BaseVariable('frame')

# Generated at 2022-06-12 20:00:09.868157
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("a") == BaseVariable("a")


# Generated at 2022-06-12 20:00:19.144701
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect, sys, builtins
    all_globals = vars(sys.modules[__name__]).copy()
    all_globals.update(vars(builtins))
    frame = inspect.currentframe()
    def check(variable, expected):
        assert variable.items(frame, normalize=False) == expected
    check(Attrs('x'), [('x', '{}')])
    check(Indices('x'), [('x[0]', '{}'), ('x[1]', '{}')])
    check(Keys('x'), [('x[0]', '{}'), ('x[1]', '{}')])
    check(Exploding('x'), [('x[0]', '{}'), ('x[1]', '{}'), ('x.a', '{}')])


# Generated at 2022-06-12 20:00:27.424552
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    item1 = BaseVariable('a')
    item11 = BaseVariable('a', exclude=1)
    item12 = BaseVariable('a', exclude='b')
    item2 = Attrs('a')
    item3 = Keys('a')
    item4 = Indices('a')
    item5 = Exploding('a')

    assert item1 != item11
    assert item11 != item12
    assert item1 != item2
    assert item2 != item3
    assert item3 != item4
    assert item4 != item5
    assert item5 != item1

# Generated at 2022-06-12 20:00:33.803422
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = inspect.currentframe().f_back.f_back
    s = "s"
    v = BaseVariable(s)
    assert v.items(frame)[0] == (s, "''")

    s = "a_variable"
    v = BaseVariable(s)
    assert v.items(frame)[0] == (s, "5")
    # help(Attrs)
    # help(Keys)
    # help(Indices)
    # help(Exploding)


# Generated at 2022-06-12 20:00:37.468382
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # In both side, the source is a none value
    v1 = BaseVariable(None)
    v2 = BaseVariable(None)
    # In both side, the source is a none value and the type is Attrs
    v3 = Attrs(None)
    # The class in both side are different.
    assert(v1 == v2)
    assert(v1 != v3)

# Generated at 2022-06-12 20:00:51.493422
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """
    Test equality of two BaseVariable objects of the same type
    """
    source1 = "var1"
    source2 = "var2"
    source3 = "var3"
    exclude1 = "ex1"
    exclude2 = "ex2"
    exclude3 = "ex3"
    code1 = "code1"
    code2 = "code2"
    code3 = "code3"
    unambiguous_source1 = "us1"
    unambiguous_source2 = "us2"
    unambiguous_source3 = "us3"
    bv1_1 = BaseVariable(source1, exclude1)
    bv1_2 = BaseVariable(source1, exclude1)
    bv2_1 = BaseVariable(source2, exclude2)

# Generated at 2022-06-12 20:00:53.954390
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a',exclude=('b','c'))==BaseVariable('a',exclude=('b','c'))


# Generated at 2022-06-12 20:00:56.536916
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("foo.bar") == BaseVariable("foo.bar")
    assert BaseVariable("foo.bar") != BaseVariable("foo.baz")

# Generated at 2022-06-12 20:01:04.623524
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert (Attrs('x') == Attrs('x'))
    assert (Keys('x') == Keys('x'))
    assert (Indices('x') == Indices('x'))
    assert (Exploding('x') == Exploding('x'))

    assert (Attrs('x') != Attrs('y'))
    assert (Keys('x') != Keys('y'))
    assert (Indices('x') != Indices('y'))
    assert (Exploding('x') != Exploding('y'))

    assert (Attrs('x') != Keys('x'))
    assert (Indices('x') != Exploding('x'))
    assert (Exploding('x') != Indices('x'))

# Generated at 2022-06-12 20:01:11.213140
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Parse the following lines
    # 1. to ensure that exceptions are NOT raised when running the _items method
    # 2. to ensure that get_shortish_repr is called
    lines = ['File "test.py", line 22, in test_BaseVariable_items',
             '    assert not_a_valid_variable_name is local_var',
             'UnboundLocalError: local variable \'not_a_valid_variable_name\' referenced before assignment']

    # Exception-handling variables
    local_var = 0
    not_a_valid_variable_name = 1
    # Expected result
    result = [('local_var', '0'),
              ('not_a_valid_variable_name', '1')]
    # Expected result with normalization

# Generated at 2022-06-12 20:01:14.422190
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    x = BaseVariable('@', 'a')
    assert x == x
    assert x == BaseVariable('@', 'a')
    assert not x == BaseVariable('@', 'b')
    assert not x == BaseVariable('@', 'a', 'b')
    assert not x == BaseVariable('$', 'a')
    assert not x == BaseVariable('@', 'a', 'b')

# Generated at 2022-06-12 20:01:19.854626
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Test(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass
    s = Test('source')
    assert (s == Test('source')) is True
    assert (s == Test('source', 'a')) is True
    assert (s == Test('source', 'a', 'b')) is False
    assert (s == Test('another')) is False
    assert (s == Test('another', 'a')) is False
    assert (s == Test('another', 'a', 'b')) is False
    assert (s == Test('source', 'b')) is False
    assert (s == Test('another', 'b')) is False



# Generated at 2022-06-12 20:01:30.579476
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    print(sys.version)

    import types
    import inspect
    import __main__

    scope = globals()
    scope['__name__'] = '__main__'

    import re
    exclude_pattern = re.compile(r'_|imp')

    class FakeFrame(object):

        def __init__(self, local_vars):
            self.f_locals = local_vars

    def get_variables(local_vars):
        result = {}
        for (name, value) in local_vars:
            if exclude_pattern.match(name):
                continue
            if isinstance(value, types.ModuleType):
                continue
            if not inspect.isclass(value):
                vars_class = BaseVariable

# Generated at 2022-06-12 20:01:33.124914
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    x = BaseVariable('a')
    y = BaseVariable('a')
    assert (x == y) == True
    assert (x == 2) == False
    z = {x}
    assert x in z
    assert 2 not in z


# Generated at 2022-06-12 20:01:43.658338
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', exclude=1) != BaseVariable('a')
    assert BaseVariable('a', exclude=1) != BaseVariable('a', exclude=2)
    assert Attrs('a') != BaseVariable('a')
    assert Keys('a') != BaseVariable('a')
    assert Indices('a') != BaseVariable('a')
    assert Indices('a')[3:] != Indices('a')
    assert Indices('a')[3:] != BaseVariable('a')
    assert Indices('a')[3:5] == Indices('a')[3:5]
    assert Indices('a')[3:5] != Indices('a')[3:6]


# Generated at 2022-06-12 20:01:51.342666
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable('1')
    var2 = BaseVariable('2')
    var3 = BaseVariable('1')

    assert var == '1'
    assert var != '2'
    assert var == var3
    assert var != var2
    
# Unit tests for method items of class BaseVariable

# Generated at 2022-06-12 20:02:00.006571
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    b1 = BaseVariable('v1')
    b2 = BaseVariable('v2')
    b3 = BaseVariable('v1')
    b4 = CommonVariable('v1')
    b5 = CommonVariable('v2')
    b6 = CommonVariable('v1')
    b7 = Attrs('v1')
    b8 = Attrs('v2')
    b9 = Attrs('v1')
    b10 = Keys('v1')
    b11 = Keys('v2')
    b12 = Keys('v1')
    b13 = Indices('v1')
    b14 = Indices('v2')
    b15 = Indices('v1')
    b16 = Exploding('v1')
    b17 = Exploding('v2')
    b18 = Exploding('v1')


# Generated at 2022-06-12 20:02:02.867531
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = Attrs(0)
    assert a == a
    assert a == Attrs(0)
    assert a != Attrs(1)
    assert a != Attrs(0, exclude=1)
    assert a != Attrs(0, exclude=set())


# Generated at 2022-06-12 20:02:11.424747
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = '123'
    frame = 123
    normalize = False
    result = BaseVariable(source).items(frame, normalize)
    print(result)
    assert isinstance(result, tuple), "Method items of class BaseVariable returns a tuple"
    assert result == (), "Method items of class BaseVariable returns a empty tuple"
    assert len(result) == 0, "Method items of class BaseVariable returns a empty tuple"
    source = 'dctVariable'
    frame = {'dctVariable': {'key': 'value'}}
    result = BaseVariable(source).items(frame, normalize)
    print(result)
    assert isinstance(result, tuple), "Method items of class BaseVariable returns a tuple"

# Generated at 2022-06-12 20:02:15.379835
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    x1 = BaseVariable("x", exclude=(1,))
    x2 = BaseVariable("x", exclude=(1,))
    x3 = BaseVariable("y", exclude=(1,))
    x4 = BaseVariable("x", exclude=(2,))
    assert x1 == x2
    assert not x1 == x3
    assert not x1 == x4

# Generated at 2022-06-12 20:02:24.279886
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from pprint import pprint
    class DerivedVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            self.source = source
            self.exclude = exclude
    var1 = DerivedVariable('1')
    var2 = DerivedVariable('2')
    var3 = DerivedVariable('2', ('2'))
    var4 = DerivedVariable('3', ('3',))
    var5 = DerivedVariable('3', ('3',))
    pprint((var1 == var2, var2 == var3, var3 == var4, var4 == var5))

if __name__ == '__main__':
    test_BaseVariable___eq__()

# Generated at 2022-06-12 20:02:31.018133
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('index') == BaseVariable('index')
    assert BaseVariable('index') != BaseVariable('indexa')
    assert BaseVariable('index') != BaseVariable('indexaa')
    assert BaseVariable('index', ['x']) == BaseVariable('index', ['x'])
    assert BaseVariable('index', ['x']) != BaseVariable('index', ['a'])
    assert BaseVariable('index', ['x']) != BaseVariable('indexa', ['x'])
    assert BaseVariable('index', ['x']) != BaseVariable('indexa', ['a'])
    assert BaseVariable('index', ['a']) != BaseVariable('index', ['x'])

# Generated at 2022-06-12 20:02:34.737426
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')
    assert BaseVariable('a') != object()



# Generated at 2022-06-12 20:02:37.394955
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert torch.isnan(torch.tensor([float('nan')]))
    assert torch.isnan(torch.tensor([float('nan')]))
    assert torch.isnan(torch.tensor([float('nan')]))

# Generated at 2022-06-12 20:02:43.060377
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import generator
    from . import pycompat
    from .utils import get_shortish_repr

    frame1 = generator.frame()
    pycompat.setitem(frame1.f_locals, 'a', 1)
    assert BaseVariable('__foo__').items(frame1) == ()
    assert BaseVariable('a').items(frame1) == (('a', '1'),)
    assert Attrs('a').items(frame1) == (('a', '1'),)

    pycompat.setitem(frame1.f_locals, 'b', 'abc')
    assert Attrs('b').items(frame1) == (('b', "'abc'"),)

    pycompat.setitem(frame1.f_locals, 'c', [1, 'spam'])

# Generated at 2022-06-12 20:02:53.547090
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v_a = BaseVariable('a')
    v_a1 = BaseVariable('a')
    v_b = BaseVariable('b')
    # __eq__ 不会报错
    assert v_a == v_a1
    assert not (v_a == v_b)
    assert not (v_a == 'a')



# Generated at 2022-06-12 20:02:55.949375
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('foo')
    var2 = BaseVariable('foo')
    assert var1 == var2

    var3 = BaseVariable('foo', 'bar')
    assert not (var1 == var3)

# Generated at 2022-06-12 20:03:04.266149
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    myVar = BaseVariable('x')
    print('Test method __eq__ of class BaseVariable')
    print('1)')
    print(myVar == myVar)
    print('2)')
    print(myVar == 'x')
    print('4)')
    print(myVar == '')
    print('5)')
    print(myVar == 5)
    print('6)')
    print(myVar == [])
    print('7)')
    print(myVar == [5,5,5])
    print('8)')
    print(myVar == (5,5,5))

test_BaseVariable___eq__()

# Unit test  for method items of class BaseVariable

# Generated at 2022-06-12 20:03:07.381497
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
  with capture_stdout(main) as output:
    assert Attrs('a').__eq__(Attrs('a')) == True
    assert Attrs('a') == Attrs('a') == True
    print("test_BaseVariable___eq__() PASSED")

if __name__ == '__main__':
  import __main__
  main = __main__.__file__
  test_BaseVariable___eq__()

# Generated at 2022-06-12 20:03:18.215211
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import ast
    from . import utils, pycompat
    import functools

    def to_code(source: str) -> ast.AST:
        tree = ast.parse(source)
        if len(tree.body) != 1:
            raise ValueError('Expected only one Python statement')
        return tree.body[0]

    def to_code_object(source: str) -> pycompat.CodeType:
        return compile(to_code(source), '<variable>', 'eval')

    def get_value(code: pycompat.CodeType, frame: pycompat.FrameType) -> object:
        return eval(code, frame.f_globals, frame.f_locals)

    def create_frame(var_name: str, var_value: str):
        frame = pycompat.create_

# Generated at 2022-06-12 20:03:21.767996
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('s') == BaseVariable('s')
    assert BaseVariable('s', 'a') == BaseVariable('s', 'a')
    assert BaseVariable('s') != BaseVariable('s', 'a')
    assert BaseVariable('s', 'a') != BaseVariable('s', 'b')
    assert BaseVariable('s') != 's'



# Generated at 2022-06-12 20:03:31.099364
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('locals', exclude=('value',)) == BaseVariable('locals', exclude=('value',))
    assert BaseVariable('locals', exclude=('value',)) != BaseVariable('locals', exclude=('value',))
    assert BaseVariable('locals', exclude=('value',)) != BaseVariable('locals', exclude=('value', 'test'))
    assert BaseVariable('locals', exclude=('value',)) != BaseVariable('locals', exclude=('value', 'test'))
    assert BaseVariable('locals', exclude=('value', 'test')) != BaseVariable('locals', exclude=('value', 'test'))

# Unit tests for class BaseVariable
# It does not actually test the class as we cannot instanciate a class with ABC methods.

# Generated at 2022-06-12 20:03:33.770716
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import pytest
    # test exception will be raise when input is not instance of BaseVariable
    a = BaseVariable('xyz')
    with pytest.raises(TypeError):
        a.__eq__(2)



# Generated at 2022-06-12 20:03:36.875850
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = Keys("params")
    v2 = Keys("params")
    v3 = Keys("params", exclude=("foo", "bar"))

    assert(v1 == v2)
    assert(not v1 == v3)

# Generated at 2022-06-12 20:03:47.278264
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import Frame

    def foo():
        x = dict(a=1, b='2', c=dict(d=3))
        y = [6, 7, 8]

    frame = Frame.from_callable(foo)
    frame.f_locals['x'] = {'a': 1, 'b': '2', 'c': {'d': 3}}
    frame.f_locals['y'] = [6, 7, 8]

# Generated at 2022-06-12 20:04:01.384569
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import pycompat

    class someclass(pycompat.ABC):
        def __init__(self):
            self.x = 123
            self.y = 456
        def foo(self):
            return 789
    # test for class Attrs
    s = someclass()
    attrs = Attrs('s')
    assert attrs.items(sys._getframe(0)) == [('s', 'someclass()'), ('s.x', '123'), ('s.y', '456')]
    assert attrs.items(sys._getframe(0), normalize=True) == [('s', 'someclass()'), ('s.x', '123'), ('s.y', '456')]

# Generated at 2022-06-12 20:04:09.684334
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    frame = frame.f_back
    local_variables = frame.f_locals
    print(type(local_variables))
    print(local_variables)
    a = local_variables["a"]
    print(type(a))
    print(a)
    print(type(a[1]))
    print(a[1])
    print(type(a[1][1][1]))
    print(a[1][1][1])
    base_variable_test = BaseVariable('a',exclude='__module__')
    print(base_variable_test.source)
    print(base_variable_test.exclude)
    print(base_variable_test.code)
    print(base_variable_test.unambiguous_source)


# Generated at 2022-06-12 20:04:13.814907
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('(dict([(1, dict([(2, dict([(3, dict([(4, dict([(5, dict())])]))]))]))]))', None)
    print (v.items(None))



# Generated at 2022-06-12 20:04:16.443144
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def check(func, source, items):
        b = BaseVariable(source, exclude=())
        print(b.items(items))
    
    

# Generated at 2022-06-12 20:04:26.000415
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import pdb
    print('sys.path is: {}'.format(sys.path))
    a=1
    b=2
    c=3
    d=4

    # <module>()->None
    # -> <code object <module> at 0x0000026D6A73A1B0, file "E:/learn/my-py-debugger/my-py-debugger/test_base.py", line 22>
    f_globals = sys._getframe().f_globals
    f_locals = sys._getframe().f_locals

    # test code:
    # my_var = Keys('a')
    # print(my_var.items(sys._getframe())) # => [('a', '1')]
    #
    # my_var = Keys('b')

# Generated at 2022-06-12 20:04:33.693897
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # When main_value is None, the result should be all passed in
    # tuples.
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (1, 2), (3, 4)
    assert TestVariable('source', exclude=('x')).items(None) == ((1, 2), (3, 4))
    # When main_value is not None, the result should contain the
    # tuples passed in, plus a new first tuple containing the source
    # and the short representation of the main_value.
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (1, 2), (3, 4)

# Generated at 2022-06-12 20:04:42.453334
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        a = 1
        b = [1, 2, 3]
        c = {'hello': 'world'}

        x = {'a': a, 'b': b, 'c': c}
        return x

    frame = utils.make_fake_frame(f)
    variables = [
        Attrs('self'),
        Keys('self.x'),
        Indices('self.x["b"]'),
        Exploding('self.x["c"]')
    ]
    for variable in variables:
        print(variable.items(frame))


if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:04:52.239893
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import numpy as np

    a = np.array([1, 2, 3])
    import pandas as pd
    d = pd.DataFrame([1, 2, 3])
    variables = [
        ('a.tolist()', a.tolist()),
        ('a.ndim', a.ndim),
        ('a.shape', a.shape),
        ('a.flags', a.flags),
        ('a.strides', a.strides),
        ('a.dtype', a.dtype),
        ('a.base', a.base),
        ('a.itemsize', a.itemsize),
        ('a.nbytes', a.nbytes),
        ('a.base_dtype', a.base_dtype),
        ('a.data', a.data)
    ]

# Generated at 2022-06-12 20:05:04.184793
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frame
    class DummyStack(object):
        def __init__(self, traceback):
            self.traceback = traceback

        def walk_traceback(self, tb):
            yield frame.Frame(None, self, tb)

    import sys
    dummy_traceback = utils.Traceback()
    dummy_stack = DummyStack(dummy_traceback)
    dummy_frame = next(dummy_stack.walk_traceback(dummy_traceback))
    globals = {
        'isinstance': isinstance,
        'sys': sys,
        'utils': utils,
    }

# Generated at 2022-06-12 20:05:14.974747
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame =  "frame"
    frame_obj = utils.Frame("file", "line", "function", "code", "frame")
    frame_obj.f_locals = {"frame_obj" : frame_obj}
    frame_obj.f_globals = {"frame_obj" : frame_obj}
    # test 1
    class Extract(BaseVariable):
        def __init__(self, source="source", exclude=()):
            super(BaseVariable, self).__init__(source, exclude)
            self.source = "source"
            self.exclude = "exclude"
            self.code = "code"
            self.unambiguous_source = "unambiguous_source"
        def items(self, frame, normalize=False):
            pass
    extract = Extract()
    # test 2

# Generated at 2022-06-12 20:05:30.222411
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    code = compile('a', '<variable>', 'eval')
    variable = BaseVariable('a', exclude = "b")
    variable.__dict__['source'] = 'a'
    variable.code = code
    variable.__dict__['exclude'] = 'b'
    variable.items(None)



# Generated at 2022-06-12 20:05:41.790714
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = Keys('event')
    print(v.items(h))

if __name__ == '__main__':
    class D(object):
        def __init__(self, a):
            self.a = a

    d = D(3)

    h = {'test': 3}
    h['h'] = {}
    h['h']['a'] = 'b'
    h['h']['b'] = 'c'
    h['h']['d'] = d
    h['h']['event'] = {
        'x': 1, 'y': 2, 'z': 3,
        '__dict__': {'a': 1, 'b': 2, 'c': 2}
    }
    test_BaseVariable_items()

# Generated at 2022-06-12 20:05:47.824722
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVar(BaseVariable):
        def __init__(self, source, value, exclude=()):
            super(TestVar, self).__init__(source, exclude)
            self.value = value

        def _items(self, key, normalize=False):
            return self.value

    class TestVar2(TestVar):
        def __init__(self, source, value, exclude=()):
            super(TestVar2, self).__init__(source, value, exclude)
            self.count = 0

        def _items(self, key, normalize=False):
            self.count += 1
            return self.value

    class TestVar3(TestVar):
        def __init__(self, source, value, exclude=()):
            super(TestVar3, self).__init__(source, value, exclude)

# Generated at 2022-06-12 20:05:56.432130
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import os
    import inspect
    import pytest
    from pytest_mock import mocker
    from pytest import approx
    import test_scenario
    from ..utils import get_shortish_repr
    from ..var_types import BaseVariable
    from ..var_types import Attrs
    from ..var_types import Exploding
    from ..var_types import Indices
    from ..var_types import Keys
    from ..var_types import needs_parentheses
    # Test with no subtests
    # get_fixed_context

# Generated at 2022-06-12 20:05:59.648409
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(v):
        print(v.items(globals()))
    test(Attrs('globals()'))
    test(Keys('globals()'))
    test(Indices('globals()'))
    test(Exploding('globals()'))
    test(Attrs('globals()["Indices"]'))
    test(Attrs('globals()["Indices"].__call__(globals()["globals"]())'))



# Generated at 2022-06-12 20:06:08.053144
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from types import FrameType
    frame = FrameType(
        f_code=lambda: None,
        f_globals=globals(),
        f_locals={'a': {'b': 2}, 'c': [1, 2], 'd': 1},
        f_back=None
    )
    keys = {1: 'a', 2: 'c[0]', 3: 'd'}  # key: source
    for key, source in keys.items():
        bv = BaseVariable(source)
        print(bv.items(frame))
        for x, y in bv.items(frame):
            print(x, y)


# Generated at 2022-06-12 20:06:15.183028
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import variables
    from . import utils
    import inspect

    frame = inspect.getouterframes(inspect.currentframe(), 2)[1][0]

    def my_func(arg1, arg2):
        return arg1, arg2

    var = variables.BaseVariable('my', 'arg')
    assert var.items(frame) == []

    var = variables.BaseVariable('my_func(arg1, arg2)', 'arg1')
    assert var.items(frame, normalize=True) == [('my_func(arg1, arg2)', '(\'a\', \'b\')')]

    var = variables.BaseVariable('my_func(arg1, arg2)', 'arg2')

# Generated at 2022-06-12 20:06:18.814371
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    frame = sys._getframe()
    for key in inspect.getouterframes(frame)[1][0].f_locals:
        print(key)
    for key,value in BaseVariable('x').items(sys._getframe()):
        print(key,value)

# Generated at 2022-06-12 20:06:26.545888
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import datetime
    frame = inspect.currentframe()
    file_name, line_no, func_name, code_line, code_index = inspect.getframeinfo(frame)
    
    # test data
    main_value = datetime.datetime.now().isoformat()
    exclude = 'test'
    source = 'a'
    # test code
    obj = BaseVariable(source, exclude)
    tp = type(obj)
    assert obj.source == source
    assert obj.exclude == exclude
    assert utils.get_shortish_repr(obj.code, normalize=True) == "<code object <module> at 0x7fdb260a3e20, file '<variable>', line 1>"
    assert obj.unambiguous_source == source
    assert obj.items(frame)

# Generated at 2022-06-12 20:06:32.985050
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    a = sys._getframe().f_back
    # print("a.f_code.co_name= %r" %a.f_code.co_name)
    # print("a.f_code.co_varnames= %r" %a.f_code.co_varnames)
    # print("a.f_code.co_names= %r" %a.f_code.co_names)
    # print("a.f_locals= %r" %a.f_locals)
    # print("a.f_globals= %r" %a.f_globals)
    # print("a.f_code.co_filename= %r" %a.f_code.co_filename)
    # print("a.f_code.co

# Generated at 2022-06-12 20:07:01.429997
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    code = compile('a[0][0]', '<variable>', 'eval')
    v = BaseVariable('a[0][0]', exclude=(0,))
    v.code = code
    assert [('a[0][0]', 'x')] == list(v.items({'a': [['x']]}))

    code = compile('1', '<variable>', 'eval')
    v = BaseVariable('a[0][0]', exclude=(0,))
    v.code = code
    assert [] == list(v.items({'a': [['x']]}))



# Generated at 2022-06-12 20:07:12.258844
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import pdb
    from .pdb import Pdb
    from .pdb import (Frame, FuncWrapper, SourceFileName,
                      EntityType, PdbPrompt, Code)

    def raise_exception():
        raise NameError("example")

    def create_frame(code):
        return Frame(Pdb(), code, 0, 0, False,
                     FuncWrapper(raise_exception, raise_exception.__code__,
                                 raise_exception.__globals__),
                     SourceFileName(raise_exception.__code__), EntityType.LOCAL,
                     PdbPrompt("(Pdb) ", "Pdb"), False, False)

    # 1. test with module level

# Generated at 2022-06-12 20:07:19.517148
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import re
    import io

    # Capture the standard output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()

    class MyClass(object):
        def __init__(self, name):
            self.name = name
        def hello(self):
            print('hello, %s' % self.name)
        def __repr__(self):
            return 'MyClass(%r)' % self.name
        def __str__(self):
            return 'MyClass(%s)' % self.name

    # Create a new instance of the class
    c = MyClass('world')

    # initialize the BaseVariable object
    my_variable = BaseVariable(c)

# Generated at 2022-06-12 20:07:23.004314
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = BaseVariable('bv','exclude')
    assert bv.items('frame') == (), "test_BaseVariable_items failed"
    

# Generated at 2022-06-12 20:07:30.522554
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def func(x, y, z, *more):
        a = 5
        b = 7
        c = 8
        d = [1, 2, 3]
        e = {'x': 1, 'y': 2}
        f = (1, 2, 3)
        g = -1

    f_locals = func.__code__.co_varnames
    f_globals = func.__globals__
    f_code = func.__code__
    f_frame = PyFrameObject()
    f_frame.f_code = f_code
    f_frame.f_locals = f_locals
    f_frame.f_globals = f_globals

    var1 = BaseVariable('d')
    var2 = BaseVariable('e')

# Generated at 2022-06-12 20:07:40.091732
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def _test(source, exclude, frame, want):
        got = BaseVariable(source, exclude).items(frame)
        assert got == want, '\nsource: {}\nframe: {}\ngot: {}\nwant: {}'.format(
            source, frame, got, want
        )

    _test('req', [],
          utils.get_frame(),
          ((
              'req',
              '<Request "GET /" [GET]>'
          ),))

    _test('req.args', [],
          utils.get_frame(),
          ((
              'req.args',
              'ImmutableMultiDict([])'
          ),))


# Generated at 2022-06-12 20:07:47.498616
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import bdb
    def bar():
        return "bar"
    def foo():
        return "foo"
    def spam():
        spam.x = 1
        spam.y = 2
        spam.spam = spam
        spam.bar = bar
        spam.foo = foo
    debug_tracer = bdb.Bdb()
    debug_tracer.runcall(spam)
    frame = bdb.Bdb.get_stack(debug_tracer)[0][0]
    a = Attrs('spam')

# Generated at 2022-06-12 20:07:56.249285
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import re
    import inspect

    def items(var):
        g = re.search("_items\((.+?), normalize=False\)", inspect.getsource(BaseVariable._items))
        if g is None:
            raise Exception("Failed to find items(var, normalize=False)")
        return eval(g.group(1), {'var': var, 'self': self}, {})

    def test(var, expected):
        assert list(items(var)) == expected

    test(1, [("1", "1")])
    test(1.0, [("1.0", "1.0")])
    test("Hello", [("'Hello'", "'Hello'")])

# Generated at 2022-06-12 20:08:03.953560
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = frame_function()
    frame.f_globals = {'a':0,'b':1,'c':2}
    frame.f_locals = {}
    print(Attrs('globals()').items(frame))
    print(Attrs('locals()').items(frame))
    print(Attrs('a').items(frame))
    print(Attrs('c').items(frame))
    print(Attrs('a.__doc__').items(frame))
    print(Attrs('b.__doc__').items(frame))


##############################################################################
# End of BaseVariable
##############################################################################



# Generated at 2022-06-12 20:08:11.943938
# Unit test for method items of class BaseVariable
def test_BaseVariable_items(): 
    def f(a):
        x = a
        y = a[0]
        z = a[:1]
        return x, y, z

    from . import variables

    frame = utils.get_code_frame(f)
    x, y, z = f((1,2))

    variables_to_test = {
        'x': (('a', '1'), ('a[0]', '1'), ('a[:1]', '(1,)')),
        'y': (('a', '1'), ('a[0]', '1'), ('a[:1]', '(1,)')),
        'z': (('a', '1'), ('a[0]', '1'), ('a[:1]', '(1,)')),
    }
    tested_variables = {}