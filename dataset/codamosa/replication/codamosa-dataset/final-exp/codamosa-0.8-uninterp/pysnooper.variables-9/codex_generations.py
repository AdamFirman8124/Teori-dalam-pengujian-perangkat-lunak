

# Generated at 2022-06-12 19:58:47.112091
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    x = {'a': 1}
    frame = {'x': x}
    v = BaseVariable('x')
    print(v.items(frame, normalize=False))
    # print(v.items(frame, normalize=True))



# Generated at 2022-06-12 19:58:50.029768
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable("test", "exclude")
    var2 = BaseVariable("test", "exclude")
    assert var1 == var2

# Generated at 2022-06-12 19:58:54.300019
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Test 1
    class A(BaseVariable):
        def _items(self, main_value, normalize=False):
            return ()
    v1 = A('a')
    v2 = A('a')
    assert v1 == v2

    # Test 2
    v3 = A('a', 'b')
    v4 = A('a', 'b')
    assert v3 != v1
    assert v3 != v2



# Generated at 2022-06-12 19:59:03.314275
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from ..tracer import Tracer
    from ..api import return_value, function_call
    from .frame import Frame
    import sys

    def num_to_value(name):
        try:
            return sys.modules[name]
        except KeyError:
            return sys.version_info

    def setup_trace(fun):
        tracer = Tracer()
        tracer.trace_method(return_value(tracer), 'items')
        tracer.trace_method(function_call(tracer), 'items')

        @tracer
        def trace():
            fun()

        return trace, tracer

    def setup_frame():
        frame = utils.Frame(utils.Function(test_BaseVariable_items))
        frame.f_globals = dict(num_to_value=num_to_value)
       

# Generated at 2022-06-12 19:59:10.217162
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    if not hasattr(pycompat.ABC, "__eq__"):
        print("SKIP")
        return
    bv = BaseVariable("a")
    bv2 = BaseVariable("a")
    # For Python 2 we need to supply a valid __hash__
    if not hasattr(bv, "__hash__"):
        bv.__hash__ = object.__hash__
    if not hasattr(bv2, "__hash__"):
        bv2.__hash__ = object.__hash__

    assert bv == bv2



# Generated at 2022-06-12 19:59:12.428705
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a')
    v2 = BaseVariable('a')
    v3 = BaseVariable('b')

    assert (v1 == v2) == True
    assert (v1 == v3) == False


# Generated at 2022-06-12 19:59:24.433407
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def _get_variable_for_source(source):
        if source == 'attrs':
            return Attrs('a')
        if source == 'keys':
            return Keys('a')
        if source == 'indices':
            return Indices('a')
        if source == 'exploding':
            return Exploding('a')

    # Test for class Attrs
    assert _get_variable_for_source('attrs') == _get_variable_for_source('attrs')  # Source is a.
    assert _get_variable_for_source('attrs') == _get_variable_for_source('attrs')  # Source is b.
    assert _get_variable_for_source('attrs') != _get_variable_for_source('exploding')   # Source is c.

    # Test for class Keys

# Generated at 2022-06-12 19:59:25.447136
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass
# examples of method items of class BaseVariable

# Generated at 2022-06-12 19:59:27.808961
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # TODO: 添加测试用例
    pass


# Generated at 2022-06-12 19:59:36.123551
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    assert Indices(None)._keys(None) == []
    assert Indices(None)._keys('hello') == range(len('hello'))
    assert Indices(None)[1:3]._keys('hello') == [1, 2]
    assert Indices(None)[1:1]._keys('hello') == []
    assert Indices(None)[::2]._keys('hello') == [0, 2, 4]
    assert Indices(None)[::-1]._keys('hello') == [4, 3, 2, 1, 0]
    assert Indices(None)[-1:2:-1]._keys('hello') == [4, 3]

# Generated at 2022-06-12 19:59:42.526462
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    indices = Indices('', ())
    indices[slice(0, None)]
    indices[1:10:2]
    indices[:]
    indices[::-1]

# Generated at 2022-06-12 19:59:45.879108
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Foo(BaseVariable):
        def __init__(self, source, exclude=()):
            BaseVariable.__init__(self, source, exclude)
    assert (Foo('test', 'exclude') == Foo('test', 'exclude') == True)
    assert Foo('test', 'exclude') != Foo('test', 'exclude2') != True


# Generated at 2022-06-12 19:59:53.020418
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def check(**kwargs):
        frame = kwargs.pop('frame')
        variables = kwargs.pop('vars')
        result = kwargs.pop('result')
        normalize = kwargs.pop('normalize', False)
        assert not kwargs

        loader = pkgutil.find_loader('debug_toolbar_line_profiler')
        module_path = loader.get_filename('debug_toolbar_line_profiler')
        module_directory = os.path.dirname(module_path)

        real_source = '{}/../../{}'.format(module_directory, 'fake_app/app.py')
        fake_source = 'fake_app/app.py'

        source = ''

# Generated at 2022-06-12 19:59:55.214719
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    v = Indices('v')
    v1 = v[::2]
    v2 = Indices('v')[::2]




# Generated at 2022-06-12 19:59:58.350779
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():

    # Imports
    from inspect import ismethod

    # Create a instance
    indices_instance = Indices('a')

    # Check whether __getitem__ method is implemented in class Indices
    assert ismethod(indices_instance.__getitem__)


# Generated at 2022-06-12 20:00:05.280967
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    x = Indices('a')
    x_slice = x[2:5]
    assert isinstance(x_slice, Indices)
    assert x_slice._slice == slice(2, 5)
    assert x_slice.source == 'a'
    assert x_slice.exclude == ()
    assert x_slice.code == x.code
    assert x_slice.unambiguous_source == x.unambiguous_source
    assert x_slice._fingerprint == x._fingerprint
    assert x_slice != x

# Generated at 2022-06-12 20:00:12.160074
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variables = (Attrs, Keys, Indices, Exploding)
    sources = (
        'a', 'a.b', 'a.b[1]', 'a.b[1].c'
    )
    for variable in variables:
        for source in sources:
            for exclude in ((), 'a', 'b', 'c'):
                var = variable(source, exclude)
                print('var.items({})'.format(var.source))
                for frame in utils.FrameIter():
                    for key, value in var.items(frame):
                        print('    ' + repr(key) + ': ' + repr(value))

# Generated at 2022-06-12 20:00:20.855933
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys

    def func():
        a = 1
        l = [1, 2]
        d = {'k': 'v'}

    frame = inspect.currentframe().f_back
    frame.f_globals['a'] = 1
    frame.f_globals['l'] = [1, 2]
    frame.f_globals['d'] = {'k': 'v'}


    vars = {'a', 'l', 'd'}
    normalize = False
    for var in vars:
        for exclude in ([], ['a'], ['k']):
            base_var = BaseVariable(var, exclude)
            items = base_var.items(frame, normalize)
            print(items)
            print(dict(items))


# Generated at 2022-06-12 20:00:31.161459
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # equal
    assert Attrs('a') == Attrs('a')
    assert Keys('a') == Keys('a')
    assert Indices('a') == Indices('a')
    assert Indices('a')[:] == Indices('a')[:]
    assert Exploding('a') == Exploding('a')
    assert Attrs('a', exclude=('b')) == Attrs('a', exclude=('b'))
    assert Keys('a', exclude=('b')) == Keys('a', exclude=('b'))
    assert Indices('a', exclude=('b')) == Indices('a', exclude=('b'))
    assert Indices('a', exclude=('b'))[:] == Indices('a', exclude=('b'))[:]

# Generated at 2022-06-12 20:00:33.601485
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    test_i = Indices('test_map')
    assert test_i[1:3]._slice == slice(1, 3)


# Generated at 2022-06-12 20:00:49.716400
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types
    import collections.abc as abc

    # test frame
    frame = sys._getframe()
    f_globals = frame.f_globals
    f_locals = frame.f_locals

    # test data

# Generated at 2022-06-12 20:00:55.761524
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = "request"
    variable_1 = BaseVariable(source)
    variable_2 = BaseVariable(source)
    variable_3 = BaseVariable(source, exclude=["POST"])
    variable_4 = BaseVariable(source, exclude="POST")

    assert variable_1 == variable_2
    assert variable_1 != variable_3
    assert variable_3 == variable_4
    assert variable_4 != variable_1



# Generated at 2022-06-12 20:00:58.365072
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert list(BaseVariable('expr').items({'expr': 3})) == [('expr', '3')]


# Generated at 2022-06-12 20:01:06.460038
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Test case 1
    var_test_case_1_1 = BaseVariable(source = "test1")
    var_test_case_1_2 = BaseVariable(source = "test1")
    assert var_test_case_1_1 == var_test_case_1_2

    # Test case 2
    var_test_case_2_1 = BaseVariable(source = "test1")
    var_test_case_2_2 = BaseVariable(source = "test2")
    assert var_test_case_2_1 != var_test_case_2_2

    # Test case 3
    var_test_case_3_1 = BaseVariable(source = "test1")
    var_test_case_3_2 = BaseVariable(source = "test1", exclude = "test2")
    assert var_test

# Generated at 2022-06-12 20:01:12.882804
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test standard case
    frame = DummyFrame(f_locals={'a': {'b': 'c'}})
    result = Keys('a').items(frame)
    assert result == [('a', "{'b': 'c'}"), ('a[b]', "'c'")]
    # test needs_parentheses
    frame = DummyFrame(f_locals={'a': {'b': 'c'}})
    result = Keys('a().to_frame()').items(frame)
    assert result == [('a().to_frame()', "dict")]
    # test when _keys raise an exception
    frame = DummyFrame(f_locals={'a': {'b': 'c'}})
    result = Indices('a').items(frame)

# Generated at 2022-06-12 20:01:19.110838
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from collections import namedtuple
    from . import utils

    _BaseVariable = namedtuple('BaseVariable', ['source', 'exclude'])

    # The same object
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')

    # The same value but different types
    assert BaseVariable('a') != _BaseVariable('a')

    # Different value
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', 'b') != BaseVariable('a')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')

    # Test with exclude == (item,)
    # The same object
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')

    # The same value but different types

# Generated at 2022-06-12 20:01:23.022407
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TempVariable(BaseVariable):
        pass

    frame = frame = inspect.currentframe()
    variable = TempVariable(source = 'frame')
    variable.items(frame)

# Generated at 2022-06-12 20:01:32.221633
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(frame, expected_result):
        dut = BaseVariable('a')
        result = dut.items(frame)
        assert result == expected_result, '%s != %s' % (result, expected_result)

    frame = utils.DummyFrame({'a': {'a': 1, 'b': 2, 'c': 3}})
    expected_result = (('a', "{'a': 1, 'b': 2, 'c': 3}"),
                       ('a.a', '1'),
                       ('a.b', '2'),
                       ('a.c', '3'))
    test(frame, expected_result)

    frame = utils.DummyFrame({'a': (1, 2, 3)})

# Generated at 2022-06-12 20:01:41.796781
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Arrange
    class BaseVariable(BaseVariable):
        def __init__(self, source):
            self.source = source
            self.code = compile(source, '<variable>', 'eval')

        def _items(self, key, normalize=False):
            return [(self.source, utils.get_shortish_repr(key, normalize=normalize))]
    class DemoClass(object):
        def __init__(self):
            self.name = 'test'
    instance = DemoClass()
    # Act
    items = BaseVariable('instance').items(sys._getframe())
    # Assert
    assert (("instance", "DemoClass()") == items[0])


# Generated at 2022-06-12 20:01:43.677991
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'locals()'
    variable = BaseVariable(source, exclude=())
    print(variable.items(variable))
    assert variable.items(variable) == [(source, '{}')]


if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:02:01.794721
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    import pprint
    def f1(x, y):
        z = x + y
        z1 = z + z
        z2 = z1 + z1
        z3 = z2 + z2
        z4 = z3 + z3
        z5 = z4 + z4
        z6 = z5 + z5
        z7 = z6 + z6
        z8 = z7 + z7
        z9 = z8 + z8
        z10 = z9 + z9
        return z10
    frame = utils.get_frame(f1)
    v = list(BaseVariable('z1').items(frame))
    pprint.pprint(v)

    a = [1, 2, 3, 4, 5]

# Generated at 2022-06-12 20:02:03.409624
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('_[0]')
    b = BaseVariable('_[0]')
    assert a == b



# Generated at 2022-06-12 20:02:11.497006
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys, inspect
    frame = inspect.currentframe()
    f = frame.f_locals
    f['f'] = f
    assert BaseVariable('f').items(frame) == [('f', '{...}')]
    assert BaseVariable('f[0]').items(frame) == [('f[0]', '{...}')]
    assert BaseVariable('f[1]').items(frame) == []
    assert BaseVariable('f.x').items(frame) == [('f.x', '{...}')]
    assert BaseVariable('f.y').items(frame) == []
    assert BaseVariable('f.f').items(frame) == [('f.f', '{...}')]
    assert BaseVariable('f.z').items(frame) == []

# Generated at 2022-06-12 20:02:12.371066
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variable = BaseVariable()
    variable.items()

# Generated at 2022-06-12 20:02:15.923577
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs('test') == Attrs('test')
    assert Attrs('test') != Attrs('test2')
    assert Attrs('test') != Keys('test')
    assert Attrs('test') != Indices('test')
    assert Attrs('test') != Exploding('test')



# Generated at 2022-06-12 20:02:19.133329
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    class A(object):
        a = 1
    a = A()
    var = BaseVariable('a')
    assert var.items(sys._getframe()) == [('a', 'A object')]

# Generated at 2022-06-12 20:02:23.842367
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a.b')
    v2 = BaseVariable('a.b')
    assert v1 == v2, '__eq__ compare BaseVariable failed.'
    v3 = BaseVariable('a.c')
    assert v1 != v3, '__eq__ compare BaseVariable failed.'


# Generated at 2022-06-12 20:02:32.013614
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable_1 = BaseVariable('a')
    variable_2 = BaseVariable('a')
    variable_3 = BaseVariable('b')
    variable_4 = BaseVariable('a', exclude='_')
    variable_5 = BaseVariable('a')
    variable_5.source = 'b'
    variable_6 = BaseVariable('a')
    variable_6.exclude = '_'
    variable_7 = BaseVariable('a')
    variable_7.code = compile('a', '<variable>', 'eval')
    variable_8 = BaseVariable('a')
    variable_8.unambiguous_source = 'a'
    variable_9 = BaseVariable('a')
    variable_10 = BaseVariable('a')

    assert variable_1 == variable_2
    assert variable_1 == variable_10
    assert variable_1 != variable

# Generated at 2022-06-12 20:02:40.072044
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    x = BaseVariable('1')
    assert x.items(1) == [('1', '1')]
    x = BaseVariable('1+1')
    assert x.items(1) == [('1+1', '2')]
    x = BaseVariable('frame.f_globals')
    assert x.items({'frame':{'f_globals':1}}) == [('frame.f_globals', '1')]
    x = BaseVariable('frame.f_locals')
    assert x.items({'frame':{'f_locals':1}}) == [('frame.f_locals', '1')]
    x = BaseVariable('1+1', exclude='2')
    assert x.items(1) == [('1+1', '2')]

# Generated at 2022-06-12 20:02:49.682203
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_helpful_exception():
        # Unit test for method items of class BaseVariable
        # Test for Exception raised when calling `items` method
        # of class `BaseVariable`
        # Test for custom Exception message
        class MockFrame(object):
            f_globals = {'a': 3}
            f_locals = {}

        class MockVariable(BaseVariable):
            def _items(self, main_value, normalize=False):
                return ('', '')

        mockFrame = MockFrame()
        mock_variable = MockVariable('a')
        with pytest.raises(Exception) as excinfo:
            mock_variable.items(mockFrame)

        assert 'has an empty source' in str(excinfo.value)


# Generated at 2022-06-12 20:03:10.005513
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    pass


# Generated at 2022-06-12 20:03:11.768495
# Unit test for method __eq__ of class BaseVariable

# Generated at 2022-06-12 20:03:21.738526
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
    unit test for method items of class BaseVariable
    """
    # normalize = False
    # test for class Attrs
    Attrs_1 = Attrs('a')
    Attrs_2 = Attrs('b')
    Attrs_3 = Attrs('c')
    Attrs_4 = Attrs('d')
    a = 3
    b = '2'
    c = {3:3, 4:4}
    d = [1,2,3,4]
    e = {3:3, 4:4}
    f = [1,2,3,4]
    frame = locals()
    assert Attrs_1.items(frame) == [('a', '3')]
    assert Attrs_2.items(frame) == [('b', "'2'")]
    assert Attrs_3

# Generated at 2022-06-12 20:03:31.394639
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = Attrs('a')
    a2 = Attrs('a')
    a3 = Attrs('a', exclude=['b', 'c'])
    a4 = Attrs('b', exclude=['b', 'c'])
    a5 = Attrs('a', exclude=['b', 'd'])
    a6 = Attrs('a', exclude=['d', 'c'])
    a7 = Attrs('a', exclude=('b', 'c'))
    assert a1 == a2
    assert a1 != a3
    assert a3 != a4
    assert a3 != a5
    assert a3 != a6
    assert a3 == a7
    del a1, a2, a3, a4, a5, a6, a7

    k1 = Keys('k')

# Generated at 2022-06-12 20:03:35.791760
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils

    class A:
        def __init__(self):
            self.a = 123
            self.b = 'a'
            self.c = [1, 2, 3, 4, 5]

    variable = BaseVariable('a', exclude=['a'])
    frame = utils.get_frame_of_function(test_BaseVariable_items)
    assert variable.items(frame) == [('a.a', '123'), ('a.b', "'a'"), ('a.c', '[1, 2, 3,...]')]

# Generated at 2022-06-12 20:03:41.669348
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:03:48.749622
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """
    Test __eq__ method of BaseVariable
    """
    a = BaseVariable('a')
    aa = BaseVariable('a')
    aaa = BaseVariable('aa')
    aaaa = BaseVariable('aa')
    b = BaseVariable('b')

    assert a == aa
    assert a != b
    assert a != aaa
    assert a != 123
    assert aa == aaaa
    assert aa != b
    assert aaa != a
    assert aaa == aaaa
    assert b != aaa
    assert b != aa
    assert 123 != aa
    assert 123 != aaaa
    assert a != 123
    assert b != 123

# Generated at 2022-06-12 20:03:57.313086
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types

    class TestClass(object):
        def __init__(self):
            self.a = 1
            self.b = [1, 2, 3]
            self.c = {'key': 'value'}
            self.d = 3

    test_class = TestClass()

    for source in ["test_class.a", "test_class.b", "test_class.c", "test_class.d"]:
        frame = types.SimpleNamespace()
        frame.f_locals = {'test_class': test_class}
        frame.f_globals = {}
        base_variable = BaseVariable(source)
        print(base_variable.items(frame))
        print()


# Generated at 2022-06-12 20:04:01.064996
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("v1", exclude="a")
    v2 = BaseVariable("v1", exclude="a")
    assert v1 == v2
    v3 = BaseVariable("v3", exclude="a")
    assert v3 != v1
    v4 = BaseVariable("v1", exclude="b")
    assert v1 != v4


# Generated at 2022-06-12 20:04:09.651415
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Create a BaseVariable instance
    base_variable = BaseVariable(source='a')

    # Test that the created instance is equal to itself
    assert base_variable == base_variable

    # Test that the created instance is equal to a copy of itself
    copy_of_base_variable = deepcopy(base_variable)
    assert base_variable == copy_of_base_variable

    # Test that the created instance is equal to an equivalent BaseVariable instance
    other_base_variable = BaseVariable(source='a')
    assert base_variable == other_base_variable

    # Test that the created instance is not equal to a BaseVariable instance with a different source
    other_base_variable = BaseVariable(source='b')
    assert base_variable != other_base_variable

    # Test that the created instance is not equal to a BaseVariable instance with a different exclude


# Generated at 2022-06-12 20:04:51.719274
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    def foo():
        x = 1
        if True:
            x = 2
        y = x
        return y

    frame = sys._getframe()
    var = BaseVariable('x')
    assert var.items(frame) == (('x', '2'),)


# Generated at 2022-06-12 20:04:54.800675
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("x") == BaseVariable("x", "y")
    assert BaseVariable("x", "y") == BaseVariable("x", "y")
    assert BaseVariable("x") != BaseVariable("y")
    assert BaseVariable("x", "y") != BaseVariable("x", "z")

# Generated at 2022-06-12 20:05:05.889106
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import debug
    from .threads import get_thread_by_id
    from .frames import Frame
    from .events import FrameEvent
    from .objects import Thread
    from .app import run_trio_app

    def thread_func1():
        x = 5
        debug.run('')
        x = 6
        debug.run('')

    async def thread_func2():
        x = 7
        debug.run('')
        x = 8
        debug.run('')

    a = 5
    b = 6
    c = 7
    d = 8
    e = 9
    f = 10
    g = 11
    h = 12
    i = 13
    j = 14
    k = 15

    a_ = 5
    b_ = 6
    c_ = 7
    d_

# Generated at 2022-06-12 20:05:13.845143
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    if sys.version_info >= (3, 0):
        import builtins
        eval('builtins.x = 1')
        print(base_variable_items())
        assert eval(base_variable_items()) == [('builtins', '<module \'builtins\' (built-in)>')]
    else:
        import __builtin__
        eval('__builtin__.x = 1')
        print(base_variable_items())
        assert eval(base_variable_items()) == [('__builtin__', '<module \'__builtin__\' (built-in)>')]



# Generated at 2022-06-12 20:05:21.406238
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import BaseVariable
    print(BaseVariable('a.b') == BaseVariable('a.b'))
    print(BaseVariable('a.b') == BaseVariable('a.c'))
    print(BaseVariable('a.b', exclude=('b',)) == BaseVariable('a.b', exclude=('b',)))
    print(BaseVariable('a.b', exclude=('b',)) == BaseVariable('a.b', exclude=('c',)))
    print(BaseVariable('a.b') == Attrs('a.b'))
    print(Keys('a.b') == Keys('a.b'))
    print(Exploding('a.b') == Attrs('a.b'))
    print(Exploding('a.b') == Keys('a.b'))

# Generated at 2022-06-12 20:05:25.572986
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('a', ['b'])
    c = BaseVariable('a', 'b')
    d = BaseVariable('b', 'a')
    e = Keys('a', 'b')
    assert a == a
    assert b == b
    assert c == c
    assert d == d
    assert e == e
    assert a != b
    assert a != c
    assert a != d
    assert a != e
    assert b != c
    assert b != d
    assert b != e
    assert c != d
    assert c != e
    assert d != e


# Generated at 2022-06-12 20:05:31.998762
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def test_equal():
        assert Attrs('x') == Attrs('x')
        assert Attrs('x', exclude='y') == Attrs('x', exclude='y')
        assert not (Attrs('x') == Attrs('y'))
        assert not (Attrs('x', exclude='y') == Attrs('x', exclude='z'))
        assert not (Attrs('x') == Keys('x'))
        assert not (Attrs('x') == Attrs('x', exclude='y'))
        assert not (Attrs('x', exclude='y') == Attrs('x'))

    test_equal()

# Generated at 2022-06-12 20:05:35.577847
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    b = BaseVariable("a")
    assert b.items(None) == ()



# Generated at 2022-06-12 20:05:41.196834
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = object()
    frame.f_locals = {'my_dict': {'a': 'b'}}
    frame.f_globals = {}

    v = Exploding('my_dict')
    res = v.items(frame)
    assert res[0] == ('my_dict', '{...}')

    v = Keys('my_dict')
    res = v.items(frame)
    assert res[0] == ('my_dict', '{...}')

# Generated at 2022-06-12 20:05:51.669012
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Variable(BaseVariable):
        def _items(self, key):
            return (key,)

    a = Variable('a', exclude=['b'])
    b = Variable('b', exclude=['c'])
    c = Variable('c', exclude=['a'])

    # Item lists of test variables
    items_a = a.items({"a":"hello"})
    items_b = b.items({"b":"world"})
    items_c = c.items({"c":"!"})
    items_d = {"a":"hello", "b":"world", "c":"!"}

    # Test for the existence of a and b in the items of d
    assert any(a.items({"a":"hello"}) == item for item in items_d)

# Generated at 2022-06-12 20:07:16.623896
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import cached_property
    class LazyDict(object):
        """
        定义一个惰性加载字典类, 用来模拟懒加载的自定义字典
        """
        def __init__(self, d):
            self.d = d

        def __getattr__(self, attr):
            return self.d[attr]

        @cached_property
        def __dict__(self):
            return self.d

        @cached_property
        def __slots__(self):
            """
            interesting __slots__ was called recursivelly
            """
            return self.d.keys()


# Generated at 2022-06-12 20:07:28.065478
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f(x):
        return x
    # f.func_code == f.__code__
    assert f.__code__ == f.func_code
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    A1 = A(1, 2)
    A2 = A('abc', 'def')
    variable1 = BaseVariable('f')
    variable2 = BaseVariable('A1')
    variable3 = BaseVariable('A2')
    test_frame = inspect.currentframe()
    A1_items = variable2.items(test_frame)
    assert A1_items[0][0] == 'A1'
    assert len(A1_items) == 3

# Generated at 2022-06-12 20:07:34.765846
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable("a[1]")
    assert var.__eq__(var)
    assert not var.__ne__(var)
    var2 = BaseVariable("a[1]")
    assert var.__eq__(var2)
    assert not var.__ne__(var2)
    var3 = BaseVariable("a[2]")
    assert not var.__eq__(var3)
    assert var.__ne__(var3)

# Generated at 2022-06-12 20:07:43.057653
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test instance of class Attrs
    attr = Attrs('a')
    frame = {}
    frame['a'] = 1
    assert attr.items(frame) == [('a', '1')]

    frame['b'] = 9
    frame['a'] = {0: frame['b']}
    assert attr.items(frame) == [('a', '{0: 9}')]

    frame['c'] = 'sdfsdfs'
    frame['b'] = {1: frame['c']}
    frame['a'] = {0: frame['b']}
    assert attr.items(frame) == [('a', '{0: {1: sdfsdfs}}')]

    frame['a'] = {0: {1: frame['c']}}

# Generated at 2022-06-12 20:07:46.860350
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # given any object, the returned result is always a tuple
    assert isinstance(BaseVariable('_').items(None), tuple)

    # TODO the following test case triggered a bug, however the bug was fixed
    # in the original code.  So it is a TO BE INVESTIGATED case!
    # Code should raise a NameError
    # assert BaseVariable('a').items(None) == ()



# Generated at 2022-06-12 20:07:47.896914
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = BaseVariable('a')
    # a.items() raise NotImplementedError


# Generated at 2022-06-12 20:07:48.823987
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('x')
    #assert v.items() == ()


# Generated at 2022-06-12 20:07:53.090424
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test method of class BaseVariable
    source = '1 + 2'
    base = BaseVariable(source)
    print(base.source)
    print(base.exclude)
    print(base.unambiguous_source)
    print([x for x in base.items(None)])
    print('--------------------------------------------------------------------------')

    # Test method of class CommonVariable
    source = 'l[:2]'
    common = CommonVariable(source)
    print(common.source)
    print(common.exclude)
    print(common.unambiguous_source)
    print([x for x in common.items(None)])
    print('--------------------------------------------------------------------------')

    # Test method of class Attrs
    source = 'l[:2]'
    attrs = Attrs(source)
    print(attrs.source)

# Generated at 2022-06-12 20:08:03.104086
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Modify the source code of function BaseVariable.items
    # to run this code unit, or
    # If you don't want to modify it,
    # you can add a new script and import it
    # after this script.
    # __file__ : absolute path of this script
    import sys
    import os.path
    sys.path.append(os.path.dirname(__file__))
    import utils

    # Variable v will be used in the following unit test
    # Below is the declaration of variable v
    v = utils.Variable(source='_v', exclude=('_v', 'v'))

    frame = sys.getframe()
    frame.f_locals = {'_v': '_v'}
    frame.f_globals = {'_v': '_v'}

    # unit

# Generated at 2022-06-12 20:08:11.237507
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_shortish_repr
    test_data = [
        ['a', 'b', 'c'],
        {'apple': 'red', 'banana': 'yellow'},
        {'a': 'b', 'c': {'1': '2'}}
    ]
    for x in test_data:
        expected_result = [('a', get_shortish_repr(x))]
        for key in x:
            expected_result.append('({}){}'.format(key, x[key]))
        # Test Attrs
        attrs = Attrs('a')
        result = attrs._items(x, False)
        if isinstance(x, Mapping) or isinstance(x, Sequence):
            assert(2 == len(result))