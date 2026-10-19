

# Generated at 2022-06-12 19:58:52.193542
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class FooVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return ()
    assert (FooVariable('x') == FooVariable('x')) is True
    assert (FooVariable('x') == FooVariable('y')) is False
    assert (FooVariable('x') == object()) is False    # isinstance(object(), BaseVariable) is False



# Generated at 2022-06-12 19:58:58.904735
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("var_1", "exclude") == BaseVariable("var_1", "exclude")
    assert BaseVariable("var_1", "exclude") is not BaseVariable("var_1", "exclude")
    assert BaseVariable("var_1", "exclude") is not BaseVariable("var_2", "exclude")
    assert BaseVariable("var_1", "exclude") is not BaseVariable("var_1", "exclude_2")


# Generated at 2022-06-12 19:59:01.805298
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    obj_str = Indices("str")
    print("obj_str: " + str(obj_str))
    print("obj_str[slice(0, 1)]: " + str(obj_str[slice(0, 1)]))

# Generated at 2022-06-12 19:59:11.908616
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    #def sample_func():
    #    class Some:
    #        def __init__(self, a, b, c=1, d=20):
    #            self.a = a
    #            self.b = b
    #            self.c = c
    #            self.d = d

    #    return Some(10, 20, d=30)

    #expect = [
    #    ('a', '10'),
    #    ('b', '20'),
    #    ('c', '1'),
    #    ('d', '30'),
    #    ('s', 'Some(a=10, b=20, c=1, d=30)'),
    #]
    #assert_result(sample_func, expect, ['s'])


# Generated at 2022-06-12 19:59:13.574073
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    i = Indices('a')
    assert i[:2] == Indices('a', slice(None, 2))

# Generated at 2022-06-12 19:59:25.389742
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


# Generated at 2022-06-12 19:59:36.252317
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = utils.new_frame()
    frame.f_globals = {'a': 1, 'b': 2}
    frame.f_locals = {'c': 3, 'd': 4}

    assert BaseVariable('a').items(frame) == (('a', '(1,)'),)
    assert BaseVariable('a+b').items(frame) == (('a+b', '(3,)'),)
    assert BaseVariable('a+b+c').items(frame) == (('a+b+c', '(6,)'),)
    assert BaseVariable('a+b+c+d').items(frame) == (('a+b+c+d', '(10,)'),)
    assert BaseVariable('a.x').items(frame) == (('a.x', 'None'),)

# Generated at 2022-06-12 19:59:40.035142
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('main_value')
    variable2 = BaseVariable('main_value')
    variable3 = BaseVariable('main_value2')

    assert variable1 == variable2
    assert variable2 == variable1
    assert variable1 != variable3
    assert variable3 != variable1
    assert variable2 != variable3
    assert variable3 != variable2

# Generated at 2022-06-12 19:59:49.958753
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from sentry_sdk.hub import Hub
    from sentry_sdk.scope import add_global_event_processor
    class TestVariable(BaseVariable):
        def __init__(self, source, exclude = ()):
            super().__init__(source, exclude)
        
        def _items(self, main_value, normalize = False):
            return [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]

    def test_processor(event, hint):
        test_variable = TestVariable('test_variable', ())
        items = test_variable.items(Hub.current.get_frame(), normalize=False)
        
        for item in items:
            if item[0] == 'test_variable':
                assert item[1] == '"Test"'
                return

# Generated at 2022-06-12 19:59:55.967453
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a.b')
    var2 = BaseVariable('a.b')
    assert(var1 == var2)
    var3 = BaseVariable('a.b', 'b')
    assert(var1 != var3)
    assert(var2 != var3)

# Generated at 2022-06-12 20:00:11.183257
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import os
    import re

    def f1():
        var1 = 1
        var2 = 'str'
        return var1, var2 

    def f2():
        a = 2
        b = 'str2'
        return a, b 

    def f3(a):
        b = 'str3'
        return a, b
    f3.__code__ = f1.__code__

    scope = {}

    for func in [f1, f2, f3]:
        func.__name__ = "f" + str(len(scope) + 1)
        scope[func.__name__] = func

    frame1 = inspect.currentframe()
    frame1 = frame1.f_back
    while frame1:
        code = frame1.f_code

# Generated at 2022-06-12 20:00:17.451754
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class My(BaseVariable):
        def _items(self, main_value, normalize=False):
            return ()
    assert My('a', ('b', 'c')) == My('a', ('b', 'c'))
    assert My('a', ('b', 'c')) != My('a', ('b', 'c', 'd'))
    assert My('a', ('b', 'c')) != My('a', ('b', 'c', 'd'))


# Generated at 2022-06-12 20:00:23.403263
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # 1.Test example 1
    example1 = BaseVariable('some_var_name')
    assert example1.items({'some_var_name':'test'})==[('some_var_name', "'test'")]
    assert example1.items({'some_var_name':'test', 'other_var':'other'})==[('some_var_name', "'test'")]
    # 2.Test example 2
    example2 = BaseVariable('some_var_name', 'some_var_name')
    assert example2.items({'some_var_name':'test'})==[]
    # 3.Test example 3
    example3 = BaseVariable('some_var_name', 'other_var_name')

# Generated at 2022-06-12 20:00:27.430051
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect

    class A(object):
        b = 1

    a = A()
    locals_ = locals()
    a.c = A()
    a.c.b = 2
    keys = ('a', 'a.b', 'a.c', 'a.c.b', 'a.c.b.c')

    test_1 = BaseVariable(keys[0]).items(locals_)

    assert(test_1[0][0] == 'a')
    assert(test_1[0][1] == '<__main__.A object at 0x0000021F9CBE1B48>')

    test_2 = BaseVariable(keys[1]).items(locals_)

    assert(test_2[0][0] == 'a.b')

# Generated at 2022-06-12 20:00:36.481558
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    # *****************
    # test for Attrs
    print('\n' + '----->Start Unit Test for Attrs<------')
    a = Attrs('a')
    b = Attrs('b')
    c = Attrs('c')
    print(a.items(inspect.currentframe()))
    print(b.items(inspect.currentframe()))
    print(c.items(inspect.currentframe()))
    print('\n' + '----->End Unit Test for Attrs<------')
    # *****************
    # test for Keys
    print('\n' + '----->Start Unit Test for Keys<------')
    d = Keys('d')
    e = Keys('e')
    f = Keys('f')

# Generated at 2022-06-12 20:00:48.118953
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class MyBaseVariable(BaseVariable):
        def _items(self, key, normalize=False):
            pass
            
    obj1 = MyBaseVariable("main_value", exclude=())
    obj2 = MyBaseVariable("main_value", exclude=())
    obj3 = MyBaseVariable("main_value", exclude=('.','.'))
    obj4 = MyBaseVariable("my-value", exclude=())
    obj5 = MyBaseVariable("my-value", exclude=('.','.'))
    obj6 = MyBaseVariable("my-value", exclude=('.','.'))
    obj7 = MyBaseVariable("my-value", exclude=('.','.'))
    obj8 = MyBaseVariable("my-value", exclude=('.','.'))
    obj9 = MyBaseVariable("my-value", exclude=('.','.'))
   

# Generated at 2022-06-12 20:00:53.239345
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # this is the stack frame you want to extract locals from
    frame = sys._getframe(0)
    # get the locals from the frame
    locals = frame.f_locals
    get_items = BaseVariable('')
    output = get_items.items(frame)
    print(output)

# Generated at 2022-06-12 20:01:03.563315
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a.b') == BaseVariable('a.b')
    assert not (BaseVariable('a') == BaseVariable('b'))
    assert not (BaseVariable('a.b') == BaseVariable('a.c'))
    assert not (BaseVariable('a.b') == BaseVariable('a.b.c'))
    assert not (BaseVariable('a.b') == BaseVariable('a.b', 'c'))
    assert not (BaseVariable('a.b') == BaseVariable('a.b', ('c', )))
    assert not (BaseVariable('a.b') == BaseVariable('a.b', 'c'))
    assert not (BaseVariable('a.b') == BaseVariable('a.b', ('c', )))
    assert BaseVariable('a.b', 'c') == BaseVariable('a.b', 'c')


# Generated at 2022-06-12 20:01:10.520839
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_repr_as_str, get_shortish_repr
    class BaseVariableFake(BaseVariable):
        def _items(self, main_value):
            return [(self.source, main_value)]

    test_globals = {'x': BaseVariableFake('a'), 'z': 1, 'w': 'text'}

    # main_value = eval(self.code, frame.f_globals or {}, frame.f_locals),
    # here passing globals dictionary 
    # test_globals - {'x': BaseVariableFake('a'), 'z': 1, 'w': 'text'}
    # as frame.f_globals and {'y': 2} as frame.f_locals
    # calling items(main_value)
    # 
    # Items :

# Generated at 2022-06-12 20:01:15.470368
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    import inspect

    frame = inspect.currentframe()
    var = BaseVariable("frame")
    items = var.items(frame)
    assert "frame.f_code" in items


# Generated at 2022-06-12 20:01:35.565339
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from inspect import currentframe

    def func_to_test():
        return {"a": {"b": 1}}

    vars = {"a": 1, "b": 2}
    # get frame of caller
    frame = func_to_test.__code__.co_name
    frame = currentframe()
    v = BaseVariable("a")
    v.source = "a"
    assert v.items(frame) == [('a', '1')]



# Generated at 2022-06-12 20:01:42.190631
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    print("\n"*3)
    print("********* Unit Test For BaseVariable *********")
    v1 = BaseVariable("xyz",(1,2,3))
    v2 = BaseVariable("xyz",(1,2,3))
    v3 = BaseVariable("xyz",(4,5,6))
    assert v1 == v2
    assert v1 != v3
    print("BaseVariable Pass Unit Test")
    print("\n"*3)


# Generated at 2022-06-12 20:01:49.439348
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from .test_utils import FakeFrame
    import pytest
    
    frame = FakeFrame()
    
    def test(expected_result, x, y):
        assert (x == y) == expected_result
        assert (x != y) != expected_result
    
    test(True, Keys('foo'), Keys('foo'))
    test(True, Keys('foo'), Keys('foo', exclude=('bar',)))
    test(False, Keys('foo'), Keys('bar'))
    test(False, Keys('foo'), Keys('foo', exclude=('bar',)))
    test(False, Keys('foo'), Attrs('foo'))
    test(True, Attrs('foo'), Attrs('foo'))
    test(True, Attrs('foo'), Attrs('foo', exclude=('bar',)))

# Generated at 2022-06-12 20:01:58.947412
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class My_Variable(CommonVariable):
        def _keys(self, main_value):
            return itertools.chain(
                getattr(main_value, '__dict__', ()),
                getattr(main_value, '__slots__', ())
            )

        def _format_key(self, key):
            return '.' + key

        def _get_value(self, main_value, key):
            return getattr(main_value, key)
    class A:
        def __init__(self, x, y):
            self.x = x
            self._y = y

    class B(A):
        __slots__ = ['a', 'b']
        def __init__(self, b, a):
            A.__init__(self, 1, 2)
            self.a = a


# Generated at 2022-06-12 20:02:01.612981
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    bv1 = BaseVariable('x')
    bv2 = BaseVariable('x')
    assert bv1 == bv2
    bv3 = BaseVariable('y')
    assert bv1 != bv3


# Generated at 2022-06-12 20:02:05.318994
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    test_var = BaseVariable("test", ("x", ))
    test_var.items(frame)
    pass

# Generated at 2022-06-12 20:02:10.392177
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a=BaseVariable('abc')
    b=BaseVariable('abc')
    c=BaseVariable('def')
    d=BaseVariable('def', exclude='c')
    e=BaseVariable('def', exclude='c')
    assert a==b
    assert b==a
    assert c==d
    assert d==c
    assert d==e
    assert e==d
    assert e!=BaseVariable('def', exclude='c', f='90')


# Generated at 2022-06-12 20:02:15.887038
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Setup
    variable_1 = BaseVariable('x', ('a',))
    variable_2 = BaseVariable('x', ('a',))
    variable_3 = BaseVariable('y', ('a',))

    # Exercise
    actual = (
        variable_1 == variable_2,
        variable_1 == variable_3,
        variable_1 == 1,
    )

    # Verify
    expected = (True, False, False)
    assert actual == expected



# Generated at 2022-06-12 20:02:20.378596
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import types
    import glob 
    import os
    import ast
    import six

    conftest_filename = os.path.join(os.path.dirname(__file__),
                                    'conftest.py')
    with open(conftest_filename) as f:
        conftest_text = f.read()

    def normalize(source):
        tokens = list(tokenize.generate_tokens(StringIO(source).readline))
        normalized = cStringIO()
        for _, s, _, _, _ in tokens:
            normalized.write(s)
        normalized.seek(0)
        return normalized.read()

    def normalize_and_fix_encoding(source):
        if isinstance(source, six.binary_type):
            source = source.dec

# Generated at 2022-06-12 20:02:22.478509
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable_1 = BaseVariable(source='aaa', exclude=['e1', 'e2'])
    variable_2 = BaseVariable(source='aaa', exclude=['e1', 'e2'])

    assert variable_1 == variable_2


# Generated at 2022-06-12 20:02:53.808378
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # calling instance.__eq__(instance) should return True
    for var in (Attrs('x'), Keys('y'), Exploding('z')):
        assert var == var

# Generated at 2022-06-12 20:03:00.719163
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # 1. Arrange
    var1 = BaseVariable("var1", exclude="1")
    var2 = BaseVariable("var2", exclude="2")
    var3 = BaseVariable("var1", exclude="1")
    var4 = BaseVariable("var2", exclude="2")

    # 2. Act
    result1 = var1 == var2
    result2 = var3 == var4

    # 3. Assert
    assert isinstance(result1, bool)
    assert isinstance(result2, bool)
    assert result1 is False
    assert result2 is False


# Generated at 2022-06-12 20:03:08.329709
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    class A(object):
        a = 1
        b = 'abc'
        c = [1, 2, 3]
    attributes_source = 'inspect.getmembers(a, lambda x: not inspect.ismethod(x))'
    attributes_except_c_source = attributes_source + '[1:4]'
    attributes_except_b_source = attributes_source + '[1:3] + ' + attributes_source + '[4:6]'
    attributes_except_b_c_source = attributes_source + '[1:3] + ' + attributes_source + '[5:6]'
    a = A()
    attributes = inspect.getmembers(a, lambda x: not inspect.ismethod(x))

# Generated at 2022-06-12 20:03:18.427234
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import console
    from . import pycompat
    from . import utils
    from .pycompat import str_to_bytes
    from .compat import builtins

    _open = open

    # Ensure _open is available
    open = _open

    class Var(BaseVariable):

        def _items(self, main_value, normalize=False):
            return ('var', 'value')

    frame = pycompat.get_dummy_frame()
    var = Var('x')
    x = 1
    assert var.items(frame) == (('var', 'value'),)
    open = builtins.open = open

    frame = pycompat.get_dummy_frame()
    var = Var('x')
    x = 1
    assert var.items(frame) == (('var', 'value'),)



# Generated at 2022-06-12 20:03:25.351604
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from inspect import FrameInfo, Parameter
    from .traceback import Traceback

    def get_frame_info(frame):
        assert frame is not None
        return FrameInfo(frame, 0, '<file name>', '<file name>', '<code>', '<code>', '<code>', 1)

    def get_parameters(frame):
        assert frame is not None
        return []

    def get_traceback(tb, normalize=False):
        assert tb is not None
        return Traceback([get_frame_info(tb)], get_parameters, normalize)

    def get_exception(tb):
        assert tb is not None
        return str(tb)


# Generated at 2022-06-12 20:03:29.367328
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a')
    var2 = BaseVariable('a')
    var3 = BaseVariable('b')

    assert var1 ==  var2, "Two variables with same source should be equal"
    assert var2 != var3, "Two variables with different source shouldn't be equal"


# Generated at 2022-06-12 20:03:33.731800
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import exc
    import inspect
    import types
    import collections

    data = {'hello': 'world'}
    frame = inspect.currentframe()
    frame.f_locals['d'] = data

    # Testing common case
    var = Keys('d')
    assert var.items(frame, normalize=False) == [('d[hello]', "'world'")]

    # Test for error in ctor
    for source in [None, 'a[b']:
        try:
            var = Keys(source)
        except exc.VarTypeError:
            pass
        else:
            assert False, 'expected VarTypeError'

    # Testing use case of the method _items
    var = Keys('d', 'hello')
    assert var._items(data) == []

    # Testing use case of the method _format_

# Generated at 2022-06-12 20:03:37.187280
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert(BaseVariable('a') == BaseVariable('b'))
    assert(not BaseVariable('a') == BaseVariable('b', exclude='c'))
    assert(not BaseVariable('a', exclude='b') == BaseVariable('a', exclude='c'))


# Generated at 2022-06-12 20:03:44.579309
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame_variables = {
        "a": {"b" : {"c": 100}},
        "b": 'abc'
    }
    frame = utils.Frame(None, 'fake.py', None, None, frame_variables)
    b = BaseVariable('a')
    assert b.items(frame) == (('a', "{'b': {'c': 100}}"),)
    c = BaseVariable('b')
    assert c.items(frame) == (('b', "'abc'"),)


# Generated at 2022-06-12 20:03:46.511893
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
     var = BaseVariable("source", ['exclude'])
     assert var.items("frame") is None
# Unit tests for method _items of class CommonVariable

# Generated at 2022-06-12 20:04:33.147177
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
    Тестирует метод BaseVariable.items()
    """
    frame = frame_for_test()
    variable = BaseVariable("a")

    def get_a():
        a = "first"
        print("Печатаю a")
        return a

    def get_b():
        b = "second"
        print("Печатаю b")
        return b

    frame.f_locals['get_a'] = get_a
    frame.f_locals['get_b'] = get_b

    setattr(frame.f_locals['get_a'], 'c', 'third')

    main_value = get_a()
    items = variable.items(frame)

# Generated at 2022-06-12 20:04:43.870268
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import flask
    import sqlalchemy

    class TestClass(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    test_list = [1,2,3]
    test_dict = {'a': 1, 'b': 2}

    t = TestClass('a', 'b')

    # test for Attrs
    attrs_test_variable = Attrs('t', exclude='b')
    test_t_value = attrs_test_variable.items(sys._getframe(), normalize=True)

# Generated at 2022-06-12 20:04:45.450374
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('abc') == BaseVariable('abc')
    assert BaseVariable('abc') != BaseVariable('cde')
    assert BaseVariable('abc') != 5
    assert BaseVariable('abc') != BaseVariable('abc', ['def'])
    assert BaseVariable('abc', ['def']) != BaseVariable('abc')


# Generated at 2022-06-12 20:04:47.498543
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source_code = "3 + 4"
    variable = BaseVariable(source_code)
    assert variable.items({}) == ()


# Generated at 2022-06-12 20:04:51.235837
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestBaseVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, main_value)]
    return TestBaseVariable('main_value').items({'main_value': 'test'})[0][1] == 'test'

# Generated at 2022-06-12 20:04:56.284753
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class A(BaseVariable):
        def _items(self, main_value, normalize=False):
            return []

    a = A('x')
    b = A('y')
    assert a != b
    assert a == A('x')
    assert a == A('x', exclude='abc')
    assert a != A('x', exclude='abd')
    assert a != A('x', exclude='ab')
    assert a != A('')
    assert a != A('x', exclude='')
    assert a == A('x', exclude='ab', bla='bla')
    assert a != A('x', exclude='ab', bla='bli')
    assert a != A('x', exclude='ab', bli='bla')
    # Check that eq is symmetric
    c = A('x')

# Generated at 2022-06-12 20:05:05.849520
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Check equality of variables with same source, exclude but different type
    assert Keys('__a__') == Attrs('__a__')
    # Check equality of variables with different source
    assert Keys('__a__') != Keys('__b__')
    # Check equality of variables with different exclude
    assert Keys('__a__', '__b__') != Keys('__a__')
    # Check equality of variables with same source but one is exploded
    assert Keys('__a__') != Exploding('__a__')
    assert Keys('__a__') == Exploding('__a__')[:]
    # Check variables that needs parentheses
    assert Keys('a[1]') == Keys('(a)[1]')

# Generated at 2022-06-12 20:05:07.516922
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
  assert BaseVariable("a") == "a"
  assert not BaseVariable("a") == BaseVariable("b")


# Generated at 2022-06-12 20:05:13.183222
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    user_var = utils.UserVariable('x')
    dict_var = utils.Variable('x', 'map')
    func_var = utils.Variable('x', 'func')
    assert (user_var == user_var)
    assert (user_var == dict_var)
    assert (user_var == func_var)
    assert (not (user_var != func_var))

# Generated at 2022-06-12 20:05:18.087739
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('foo').__eq__(BaseVariable('foo')), "Variable object 'foo' should be equal to object 'foo'"
    assert BaseVariable('foo').__eq__(BaseVariable('bar')), "Variable object 'foo' should be equal to object 'bar'"
    assert BaseVariable('foo').__eq__(BaseVariable('zoo')), "Variable object 'foo' should be equal to object 'zoo'"


# Generated at 2022-06-12 20:06:43.959564
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test for method items of class BaseVariable in the case where the source
    # is the name of a variable
    def test_items_for_varible(source_variable, normalize, name_frame,
                               value_frame, expected_result):
        """Tests for method items of class BaseVariable"""
        base_variable = BaseVariable(source_variable, exclude=())
        assert base_variable.items(name_frame, normalize) == expected_result
        assert base_variable.items(value_frame, normalize) == expected_result

    name_frame = utils.get_frame(0)
    value_frame = utils.get_frame(5)
    source_variable = 'a'
    normalize = False
    expected_result = [('a', '1')]

# Generated at 2022-06-12 20:06:49.065582
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('x') == BaseVariable('x')
    assert BaseVariable('x', 'y') == BaseVariable('x', 'y')
    assert BaseVariable('x') != BaseVariable('y')
    assert BaseVariable('x', 'y') != BaseVariable('x', 'z')
    assert BaseVariable('x', 'y') != BaseVariable('x')



# Generated at 2022-06-12 20:06:53.748336
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = "hello source"
    exclude = {1,2,3}
    assert BaseVariable(source, exclude) == BaseVariable(source, exclude)
    assert BaseVariable(source, exclude) != BaseVariable(source)
    assert BaseVariable(source, exclude) != BaseVariable(source, {})
    assert BaseVariable(source, exclude) != BaseVariable(source, {1,2})
    assert BaseVariable(source, exclude) != BaseVariable('abc', exclude)


# Generated at 2022-06-12 20:06:55.843917
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a', exclude='a') == BaseVariable('a', exclude='a')
    assert BaseVariable('a') == BaseVariable('a', exclude='b')
    assert not BaseVariable('a') == BaseVariable('b')


# Generated at 2022-06-12 20:07:06.188561
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class DummyVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            BaseVariable.__init__(self, source, exclude)
        def _items(self, key):
            return ()

    dummy_variable1 = DummyVariable("a", (1, 2, 3))
    dummy_variable2 = DummyVariable("a", (1, 2, 3))
    dummy_variable3 = DummyVariable("b", (1, 2, 3))
    dummy_variable4 = DummyVariable("a", (1, 2))

    assert dummy_variable1 == dummy_variable1
    assert dummy_variable1 == dummy_variable2
    assert dummy_variable1 == dummy_variable3
    assert dummy_variable1 == dummy_variable4

    assert dummy_variable2 == dummy_variable1

# Generated at 2022-06-12 20:07:15.611632
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from copy import deepcopy
    from . import utils
    from . import pycompat
    from . import pwdb
    V = pwdb.Exploding
    v = V('foo.bar')
    foo = {}
    foo['bar'] = 'baz'
    frame = {}
    frame['foo'] = foo
    assert v.items(frame) == [('foo.bar', '"baz"')]
    assert V('bar', exclude=('bar',)).items(frame) == []
    foo = []
    foo.append(range(10))
    foo.append(range(10, 20))
    foo.append(range(20, 30))
    foo.append(range(30, 40))
    foo.append(range(40, 50))
    foo.append(range(50, 60))

# Generated at 2022-06-12 20:07:21.915333
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            yield 1, 2
            yield 3, 4

    test_variable = TestVariable('time.time()')
    assert list(test_variable.items(None)) == [(1, 2), (3, 4)]


# Generated at 2022-06-12 20:07:29.408484
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_global_variable
    import pandas as pd
    import numpy as np
    pd.__version__
    global_variables = get_global_variable()
    # Testing class Attrs
    # By default, the ancestor class CommonVariable calls _keys(main_value) 
    # to get keys of main_value before calling _items(main_value)
    # When main_value is a object of class Attrs, _keys(main_value) doesn't work.
    # So we should add the method _keys(main_value) to class Attrs
    # to make isinstance(main_value, Attrs) return True
    attrs_variable = Attrs("pd")
    assert attrs_variable._keys(pd) == ['__version__']

# Generated at 2022-06-12 20:07:39.242353
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:07:42.006622
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import collections
    d=collections.deque('abc')
    d.reverse()
    r=Indices('d').items(d)
    print(r)

if __name__ == '__main__':
    test_BaseVariable_items()