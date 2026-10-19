

# Generated at 2022-06-12 19:58:48.458886
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        v = BaseVariable(source='x', exclude='yes')
        assert v.items(frame) == ((v.source, 'yes'),)
    frame = utils.get_frame_from(f)
    x = 'yes'
    f()
    
    

# Generated at 2022-06-12 19:58:50.517490
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Does not throw an exception
    try:
        BaseVariable('').items(None)
    except Exception:
        assert False, 'BaseVariable.items should not raise an exception'



# Generated at 2022-06-12 19:58:54.478280
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    source = 'test_variable'
    variable = Indices(source)
    result = variable.__getitem__(slice(1, 2))

    assert isinstance(result, Indices)
    assert type(result) != type(variable)
    assert type(result) != variable
    assert result.source == variable.source
    assert result.exclude == variable.exclude
    assert result._slice == slice(1, 2)

# Generated at 2022-06-12 19:59:03.398193
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(source, exclude, frame, expected_result, normalize=False):
        variable = BaseVariable(source, exclude)
        assert variable.items(frame, normalize) == expected_result

    def test_exception(source, exclude, frame, normalize=False):
        variable = BaseVariable(source, exclude)
        with pytest.raises(Exception):
            variable.items(frame, normalize)

    # Test for class BaseVariable
    test('a', (), {'a': 1}, [('a', '1')])
    test('a.b', (), {'a': lambda: 1}, [('a.b', '<function 1>')])
    test('a.b', (), {'a': 1}, [('a.b', '<could not evaluate>')])

# Generated at 2022-06-12 19:59:07.954214
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('test', exclude=['a', 'b'])
    b = BaseVariable('test', exclude=('a', 'b'))
    c = BaseVariable('test', exclude='a')
    d = BaseVariable('test')

    assert a == a
    assert a == b
    assert a == c
    assert a != d


# Generated at 2022-06-12 19:59:13.428511
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    a = Indices('a')[1:3]
    assert a._slice.start == 1
    assert a._slice.stop == 3
    assert a._slice.step is None
    b = a[:]
    assert b._slice.start == a._slice.start
    assert b._slice.stop == a._slice.stop
    assert b._slice.step == a._slice.step


KEYWORDS = {}
KEYWORD_ALIASES = {}
DEFAULT_KEYWORDS = [
    '_', '__'
]
DEFAULT_KEYWORD_ALIASES = {
    'value': '_',
    'result': '__'
}

for keyword in DEFAULT_KEYWORDS:
    KEYWORDS[keyword] = keyword



# Generated at 2022-06-12 19:59:24.004166
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Variable with different name must compare equal
    assert BaseVariable('x') == BaseVariable('y')
    # Variable with different source must compare not equal
    assert BaseVariable('x') != BaseVariable('x+1')
    assert BaseVariable('x', exclude='y') == BaseVariable('x', exclude='z')
    assert BaseVariable('x', exclude='y') != BaseVariable('x', exclude='y,z')
    # Variable with different exclude must compare not equal
    assert BaseVariable('x', exclude='y') != BaseVariable('x')
    # Variable with different type must compare not equal
    assert BaseVariable('x') != Variable('x')
    assert BaseVariable('x') != Indices('x')

# Generated at 2022-06-12 19:59:27.603908
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')


if __name__ == '__main__':
    test_BaseVariable___eq__()

# Generated at 2022-06-12 19:59:37.601878
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('x').items({'x': 123}) == []
    assert Keys('x').items({'x': 123}) == [('x[]', '{}')]
    assert Keys('x').items({'x': {'y': 123}}) == [('x[]', '{}'), ('x[y]', 123)]
    assert Indices('x').items({'x': [123]}) == [('x[]', '{}'), ('x[0]', 123)]
    assert Attrs('x').items({'x': Attrs}) == [('x', 'Attrs'), ('x.__dict__', None)]
    assert Exploding('x').items({'x': {'y': 123}}) == [('x[]', '{}'), ('x[y]', 123)]

# Generated at 2022-06-12 19:59:45.193778
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_shortish_repr

# Generated at 2022-06-12 19:59:57.097584
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("var", ('var',))
    v2 = BaseVariable("var", ('var',))
    v3 = BaseVariable("var", ('var', '3'))
    assert v1 is v1
    assert v1 == v1
    assert v1 == v2
    assert v1 != v3
    assert v1 != "var"
    assert v3 != v2


# Generated at 2022-06-12 20:00:07.877960
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import MockFrame
    from .local_variables import LocalVariable

    # Test for magic methods
    frame = MockFrame({'a': [1, 2, 3]})
    variable = LocalVariable('a')

# Generated at 2022-06-12 20:00:14.130660
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from .pycompat import with_metaclass,ABCMeta
    class BaseClass(with_metaclass(ABCMeta,object)):
        def __init__(self,*args,**kwargs):
            pass

    BaseVariable.__abstractmethods__=frozenset()

    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') == BaseVariable('a',[])
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a',['a']) != BaseVariable('a')
    assert BaseVariable('a',['b']) != BaseVariable('a',['b','c'])
    assert BaseVariable('a') != BaseClass('a')

# Generated at 2022-06-12 20:00:21.685598
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    _frame = lambda **kwargs: pycompat.namedtuple('Frame', 'f_globals f_locals')(**kwargs)
    frame = _frame(
        f_globals={'a': 1, 'b': [2, 3], 'c': {4: 5}},
        f_locals={'a': 6, 'b': 7, 'c': 8},
    )

    assert list(Attrs('a').items(frame)) == [('a', '1')]

# Generated at 2022-06-12 20:00:29.335971
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("test.test") == BaseVariable("test.test")
    assert BaseVariable("test.test") != BaseVariable("test.test2")
    assert BaseVariable("test.test", exclude=["test"]) == BaseVariable("test.test", exclude=["test"])
    assert BaseVariable("test.test", exclude=["test"]) != BaseVariable("test.test", exclude=["test2"])
    assert BaseVariable("test.test", exclude=["test"]) != BaseVariable("test.test", exclude=["test", "test2"])

# Generated at 2022-06-12 20:00:32.048319
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = Attrs('a')
    b = Attrs('a')
    assert a == b
    assert hash(a) == hash(b)


# Generated at 2022-06-12 20:00:39.249616
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Attrs(BaseVariable):
        def _items(self, key, normalize=False):
            return [
                (self.source, 1),
            ]
    class Keys(BaseVariable):
        def _items(self, key, normalize=False):
            return [
                (self.source, 2),
            ]
    class Indices(BaseVariable):
        def _items(self, key, normalize=False):
            return [
                (self.source, 3),
            ]
    class Exploding(BaseVariable):
        def __init__(self, source, exclude=()):
            super(Exploding, self).__init__(source, exclude)
        def _items(self, key, normalize=False):
            if isinstance(key, Mapping):
                cls = Keys

# Generated at 2022-06-12 20:00:45.832132
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var_1 = BaseVariable(source="X")
    var_2 = BaseVariable(source="X", exclude="x")
    var_3 = BaseVariable(source="X", exclude="x")

    assert var_1 == var_1
    assert var_2 == var_2
    assert var_3 == var_3

    assert var_1 != var_2
    assert var_2 != var_3
    assert var_1 != var_3



# Generated at 2022-06-12 20:00:52.974591
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Case 1
    var_1 = BaseVariable(source='test.var', exclude=('var.1',))
    var_2 = BaseVariable(source='test.var', exclude=('var.1',))
    result = var_1 == var_2
    if result == True:
        print("Case 1 passed")
    else:
        print("Case 1 failed")

    # Case 2
    var_1 = BaseVariable(source='test.var', exclude=('var.1',))
    var_2 = BaseVariable(source='test.var', exclude=('var.2',))
    result = var_1 == var_2
    if result == False:
        print("Case 2 passed")
    else:
        print("Case 2 failed")

    # Case 3

# Generated at 2022-06-12 20:01:03.370370
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_shortish_repr 

    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, get_shortish_repr(main_value, normalize=normalize))]

    class DemoClass:
        def __init__(self, a, b):
            self.b = b
            self.c = a

    def demo_func(a, b):
        c = a
        d = a
        e = a
        return d

    scope = {'a': 12345, 'b': 'asdf', 'DemoClass': DemoClass, 'demo_func': demo_func}

    main_variable = TestVariable('a')
    assert main_variable.items(scope) == [('a', '12345')]

   

# Generated at 2022-06-12 20:01:29.821634
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from inspect import currentframe
    from pytest import raises
    from sugar import tools

    class Dummy(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass

    assert Dummy('a') == Dummy('a')

    assert Dummy('a') != Dummy('b')
    assert Dummy('a', exclude=['a']) != Dummy('a', exclude=['b'])

    assert Dummy('a') == Dummy('a', normalize=False)
    assert Dummy('a') != Dummy('a', normalize=True)

    assert Dummy(currentframe()) == Dummy(currentframe())
    assert Dummy('a') != Dummy('a').items(currentframe())

    assert Dummy('a') != 42
    assert Dummy('a') != 'a'
   

# Generated at 2022-06-12 20:01:36.819397
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys

    @utils.as_variable
    def none():
        return None
    @utils.as_variable
    def hello(name):
        return 'Hello {}'.format(name)

    #
    def f1():
        def f2():
            return sys._getframe()
        return f2()
    #
    frame = f1()

    # TODO: add more test cases
    assert 'hello' in {item[0] for item in BaseVariable('_').items(frame)}
    assert 'hello' in {item[0] for item in BaseVariable('_', exclude='hello').items(frame)}
    assert 'hello' not in {item[0] for item in BaseVariable('_', exclude='hello').items(frame)}
    #

# Generated at 2022-06-12 20:01:43.330886
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import pytest
    from ..utils import evalue_from_frame as ef
    frame = sys._getframe()
    for key in frame.f_globals:
        if key in ('BaseVariable', 'GLOBAL_VARIABLES'):
            continue
        try:
            value = frame.f_globals[key]
        except Exception:
            value = '<unavailable>'
        assert ef(key, frame) == value


# Generated at 2022-06-12 20:01:49.053779
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    result = Attrs('dict(a=10)').items(frame)
    assert result == [('dict(a=10)', "<class 'dict'>: {'a': 10}"), ('dict(a=10).a', "10")]
    result = Attrs('(dict(a=10), 2)').items(frame)
    assert result == [('(dict(a=10), 2)', "<class 'tuple'>: (dict(a=10), 2)"), ('(dict(a=10), 2)[0].a', "10")]
    result = Keys('dict(a=10)').items(frame)

# Generated at 2022-06-12 20:01:51.499722
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Variable(BaseVariable):
        def _items(self, main_value, normalize=False):
            if main_value == 'value':
                return [('source', 'value')]
            raise Exception()

    variable = Variable('source')
    variable2 = Variable('source2')

    variable.items(None)
    variable2.items(None)

# Generated at 2022-06-12 20:01:52.445335
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass


# Generated at 2022-06-12 20:02:00.668849
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import random
    import string
    import collections
    import sys
    sys.modules['__main__'] = sys.modules[__name__]
    from . import pycompat
    from . import utils
    from .context_variables import BaseVariable, CommonVariable, Attrs, Keys, Indices, Exploding
    frame_class = pycompat.Frame
    frame = frame_class(0, 'test', {}, {'v': 'hello'})
    v = BaseVariable('v', 'v')
    assert list(v.items(frame)) == [('v', "'hello'")]
    #print "base items:", list(v.items(frame))

    def _random_vars():
        """get random variables"""
        var_items = [('v', 'hello')]

# Generated at 2022-06-12 20:02:05.355218
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frame

    class ConcreteVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return self.source, utils.get_shortish_repr(key, normalize)
    var = ConcreteVariable('x')
    f = frame.Frame.from_code('', 'locals', ['x'], {'x': 'val'})
    x = tuple(var.items(f))
    assert x[0][1] == "'val'"
# End unit test


# Generated at 2022-06-12 20:02:07.582128
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable("__len__", "__len__")
    b = BaseVariable("__len__", "__len__")
    # True
    assert a == b


# Generated at 2022-06-12 20:02:12.208551
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    exp1 = BaseVariable('user')
    exp2 = BaseVariable('user')
    exp3 = BaseVariable('user2')
    exp4 = BaseVariable('user', exclude=['username'])
    exp5 = BaseVariable('user', exclude=['username'])
    exp6 = BaseVariable('user', exclude=['email'])
    assert exp1 == exp2
    assert exp1 != exp3
    assert exp4 == exp5
    assert exp4 != exp6


# Generated at 2022-06-12 20:02:38.632145
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Foo(BaseVariable):
        pass

    class Bar(BaseVariable):
        pass

    foo_a = Foo('a', 'b')
    foo_b = Foo('a', 'c')
    foo_c = Foo('b')
    bar_1 = Bar('a')
    bar_2 = Bar('a', 'b')

    # a == a
    assert foo_a == foo_a
    assert foo_a != foo_b
    assert foo_a != foo_c
    assert foo_a != bar_1
    assert foo_a != bar_2

    # b == b
    assert foo_b == foo_b
    assert foo_b != foo_a
    assert foo_b != foo_c
    assert foo_b != bar_1
    assert foo_b != bar_2

    # c == c


# Generated at 2022-06-12 20:02:47.182662
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # add __repr__ method to class Frame
    def __repr__(self):
        return "<class '_thread._local'>\n"
    Frame.__repr__ = __repr__
    stack = inspect.stack()
    frame = stack[0][0]

    # test the method with the source = 'aa', 'aa.bb', 'aa.bb[cc]', 'aa.bb[cc][dd]'
    for source in ['aa', 'aa.bb', 'aa.bb[cc]', 'aa.bb[cc][dd]']:
        for exclude in [None, [], (), ('bb',), ('bb', 'dd')]:
            test_obj = BaseVariable(source, exclude)
            test_obj.items(frame)

    # test the method with the source = '1', '1.bb', '1.bb

# Generated at 2022-06-12 20:02:54.248112
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a.b.c')
    var2 = BaseVariable('a.b.c')
    var3 = BaseVariable('a.b.c', exclude=('a',))
    assert isinstance(var1, BaseVariable)
    assert isinstance(var2, BaseVariable)
    assert isinstance(var3, BaseVariable)
    assert var1 == var1
    assert var1 == var2
    assert var1 != var3
    assert var2 != var3


# Generated at 2022-06-12 20:03:03.541246
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    local_var = {'x': 1}
    globals_var = {'x': 2}
    attrs_var = [{'x': 3}, {'x': 4}]
    keys_var = [({'x': 5}, {'x': 6})]
    indexes_var = {'x': [7, 8, 9]}
    attrs_normalize_var = [{'x': [1,2,3], 'y': [4,5,6]}]
    keys_normalize_var = [({'x': 4, 'y': 5}, {'x': 6, 'y': 7})]
    indexes_normalize_var = {'x': [[1,2,3], [4,5,6]]}


# Generated at 2022-06-12 20:03:16.059355
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('x')
    items = v.items(g_frame)
    assert items[0][0] == 'x'
    assert items[0][1] == '7'
    #test non-existing key
    nk = BaseVariable('__missing_key__')
    assert nk.items(g_frame) == ()
    #test nested key
    a = BaseVariable('__d_var')
    assert a.items(g_frame)[0][1] == '3'
    assert a.items(g_frame)[1][1] == '4'
    #test non-existing nested key
    na = BaseVariable('__d_var.__non_exist')
    assert na.items(g_frame) == ()
    #test exclude

# Generated at 2022-06-12 20:03:18.507182
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable(1, 2)
    b = BaseVariable(1, 2)
    c = BaseVariable(1, 3)
    d = BaseVariable(2, 3)

    assert a == b
    assert a != c
    assert a != d
    assert c != d



# Generated at 2022-06-12 20:03:22.642945
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return []

    a = TestVariable("some string")
    b = TestVariable("some string")
    assert a == b
    assert (hash(a) == hash(b))

    c = TestVariable("some other string")
    assert a != c
    assert (hash(a) != hash(c))


# Generated at 2022-06-12 20:03:26.604964
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    value = {'a':{'b':1}}
    variable = BaseVariable('value')
    items = variable.items(value)
    assert items == (('value', '{...}'), ('value.a', '{...}'), ('value.a.b', '1'))



# Generated at 2022-06-12 20:03:30.134527
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('x').items(None) == []
    assert not BaseVariable('x').items(None)
    assert BaseVariable('x').items(None) is not None
    assert BaseVariable('x').items(None) == BaseVariable('x').items(None)

# Generated at 2022-06-12 20:03:32.298908
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = "dat"
    with pytest.raises(NotImplementedError):
        BaseVariable(source, exclude=()).items('frame')



# Generated at 2022-06-12 20:04:08.392021
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
	obj1 = BaseVariable(source=None, exclude=None)
	obj2 = BaseVariable(source=None, exclude=None)
	assert obj1 == obj2

# Generated at 2022-06-12 20:04:18.735041
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import unittest
    import __builtin__

    class MockFrame(object):
        f_globals = None
        f_locals = None

    class MyType(object):
        def __init__(self, x, y, z=42):
            self.x = x
            self.y = y
            self.z = z

    class Test_BaseVariable(unittest.TestCase):
        def setUp(self):
            self.frame = MockFrame()
            self.frame.f_globals = sys.modules['__main__'].__dict__
            self.frame.f_locals = {
                'a': 1,
                'b': 2,
                'data': [0, 1, 2, 3],
                'c': MyType('a', 'b')
            }

# Generated at 2022-06-12 20:04:23.162370
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import frame
    v1 = frame.Exploding(source='v1')
    v2 = frame.Exploding(source='v1')
    assert v1 == v2
    v3 = frame.Exploding(source='v3')
    assert not v1 == v3


# Generated at 2022-06-12 20:04:26.599694
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a', exclude=())
    assert a == a
    assert not a == 1
    assert not a == BaseVariable('a', exclude=())
    assert not a == BaseVariable('a', exclude=(1,))
    assert not a == BaseVariable('b', exclude=())


# Generated at 2022-06-12 20:04:33.948543
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('v1')
    v2 = BaseVariable('v2')
    v3 = Attrs('v3')
    v4 = Attrs('v4')
    v5 = Keys('v5')
    v6 = Keys('v6')
    v7 = Indices('v7')
    v8 = Indices('v8')
    v9 = Exploding('v9')
    v10 = Exploding('v10')
    assert v1.source == v2.source
    assert v3.source == v4.source
    assert v5.source == v6.source
    assert v7.source == v8.source
    assert v9.source == v10.source
    assert v1.source == v2.source == v3.source == v4.source == v5.source == v6.source

# Generated at 2022-06-12 20:04:35.978989
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'x'
    bv = BaseVariable(source)
    assert bv == bv



# Generated at 2022-06-12 20:04:43.774855
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable('x', exclude=tuple())
    assert var == var
    assert var == BaseVariable('x', exclude=tuple())
    assert not (var != BaseVariable('x', exclude=tuple()))
    assert var != BaseVariable('y', exclude=tuple())
    assert var != BaseVariable('x', exclude=('spam',))
    # Type should also be considered
    assert var != object()
    assert not (var == object())
    # Need to check type even when not equal
    assert not (var == Attrs('x', exclude=tuple()))


# Generated at 2022-06-12 20:04:45.587046
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'print'
    assert BaseVariable(source) == BaseVariable(source)


# Generated at 2022-06-12 20:04:54.728198
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class A0(list):
        def items(self):
            yield 'items', 'items'
            yield 'keys', 'keys'

    class A1(A0):
        def keys(self):
            yield 'a'
            yield 'b'

    a2 = A1()
    a2.a = 1
    a2.b = 2
    a2.append(4)
    a2.append(5)
    assert list(BaseVariable('a2').items(sys._getframe())) == [
        ('a2', '<__main__.A1 at 0x7f3a6f0>'),
        ('a2.a', '1'),
        ('a2.b', '2'),
        ('a2[0]', '4'),
        ('a2[1]', '5')
    ]


# Generated at 2022-06-12 20:05:00.359858
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def check(var, f, expected):
        #var = BaseVariable(source)
        for frame, expected_result in expected:
            res = var.items(frame)
            if res != expected_result:
                print('In frame {}:'.format(f(frame)))
                print('Expected: {}'.format(expected_result))
                print('Got: {}'.format(res))
            assert res == expected_result

    source = 'x'
    expected = [(dict(x=1), (('x', '1'),)),
                (dict(x=[1]), (('x', '[1]'), ('x[0]', '1')))]
    check(BaseVariable(source), utils.format_frame_info, expected)

    source = 'x.y'

# Generated at 2022-06-12 20:06:15.667889
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class CustomVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            # main_value will be the value of the variable defined in the code
            return [(self.source, 'custom {}'.format(main_value))]

    s = 'test_BaseVariable_items_s'
    l = 'test_BaseVariable_items_l'

    # Get the value of a variable inside a function
    def test_variable(var):
        return var

    # Get the value of a variable inside a class
    class TestClass(object):
        var = 0

        def __init__(self):
            self.var = l

    test_class = TestClass()

    # These are the variables that we will search for

# Generated at 2022-06-12 20:06:19.062929
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable(10, 20)  # NOTE: '__init__' method is not abstract
    var2 = BaseVariable(10, 20)
    assert(var1 == var2)

    var3 = BaseVariable(10, 21)
    assert(var1 != var3)



# Generated at 2022-06-12 20:06:26.749509
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pytest
    from . import debugger
    from .values import FrameInfo
    import copy
    import iotbx.phil
    from io import StringIO

    def get_items(variable_inst):
        # local function
        line = 'items() function: line_no={}, source={}'.\
            format(get_items.__code__.co_firstlineno, get_items.__code__.co_filename)
        frame_info = FrameInfo(get_items.__code__.co_filename,
                               line,
                               get_items.__code__.co_firstlineno,
                               None,
                               None,
                               None,
                               copy.copy(get_items.__globals__),
                               copy.copy(get_items.__locals__))

# Generated at 2022-06-12 20:06:29.737279
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')
    assert BaseVariable('a') != object()



# Generated at 2022-06-12 20:06:41.220135
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f():
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        return (a,b,c,d,e,f,g)
    a,b,c,d,e,f,g = f()
   
    # check that source works with eval
    assert eval(BaseVariable("a").source) == a
    assert eval(BaseVariable("b").source) == b
    assert eval(BaseVariable("c").source) == c
    assert eval(BaseVariable("d").source) == d
    assert eval(BaseVariable("e").source) == e
    assert eval(BaseVariable("f").source) == f
    assert eval(BaseVariable("g").source) == g

    # check that "(" is added if needed
    assert eval

# Generated at 2022-06-12 20:06:49.303336
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('aaa', 'bbb')
    variable2 = BaseVariable('aaa', 'bbb')

    variable3 = BaseVariable('aaa')
    variable4 = variable3

    variable5 = BaseVariable('ccc', 'ddd')

    print('variable1 == variable1? {}'.format(variable1 == variable1))
    print('variable1 == variable2? {}'.format(variable1 == variable2))
    print('variable3 == variable3? {}'.format(variable3 == variable3))
    print('variable3 == variable4? {}'.format(variable3 == variable4))
    print('variable1 == variable5? {}'.format(variable1 == variable5))


# Generated at 2022-06-12 20:06:51.658040
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = "BaseVariable(source='name', exclude='at')"
    result = BaseVariable(source).items(frame)
    assert result == (('name', '"value"'),)


# Generated at 2022-06-12 20:07:01.105506
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Example(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(key, utils.get_shortish_repr(value, normalize=normalize)) for key, value in main_value.items()]
    
    # Example 1
    frame = {'x': {'xa': 1, 'xb': 2}}
    exp_var = Example('x')
    result_expected = [('x', '{\'xa\': 1, \'xb\': 2}'), ('x.xa', '1'), ('x.xb', '2')]
    assert exp_var.items(frame) == result_expected
    
    # Example 2
    frame = {'x': [{'xa': 1, 'xb': 2}, {'xa': 3, 'xb': 4}]}

# Generated at 2022-06-12 20:07:05.115201
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('',[]).items(1) == ()
    assert BaseVariable('',[]).items(1, True) == ()
    assert BaseVariable('',[]).items(1, False) == ()

# Generated at 2022-06-12 20:07:07.992611
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    l = [
        ('a', 'b'), ('c', 'd'),
    ]
    print(3 in l)
    print([1, 2] in l)

test_BaseVariable___eq__()