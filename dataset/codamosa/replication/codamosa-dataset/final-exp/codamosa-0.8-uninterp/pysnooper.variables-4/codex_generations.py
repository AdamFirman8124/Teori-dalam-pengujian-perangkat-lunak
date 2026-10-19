

# Generated at 2022-06-12 19:58:53.057685
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # setup
    from .var import BaseVariable, _BaseVariable_items
    from .builtin import all_variables
    from .pycompat import IS_PY2
    
    class DummyVariable(BaseVariable):
        def _items(self, key, normalize=False):
            raise NotImplementedError

    dummy_frame = utils.DummyFrame()
    dummy_frame.f_locals = {'x': 1, 'y': 2}
    dummy_variable = DummyVariable('x')
    dummy_variable_with_normalization = DummyVariable('y')

    # test that BaseVariable.items is an alias to _BaseVariable_items
    assert BaseVariable.items is _BaseVariable_items

    # normalize=True, an item of returned tuple is a tuple of two strings and BaseVariable.items does not raise


# Generated at 2022-06-12 19:58:59.669094
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    from . import utils
    local_frame = inspect.currentframe().f_back
    global_frame = inspect.currentframe().f_back.f_back

    frame = local_frame
    print(local_frame)
    print(global_frame)
    for var in utils.DEFAULT_VARIABLES:
        items = var.items(frame)
        print(items)


if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 19:59:04.063464
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    _slice = slice(None, None, None)
    assert Indices('a', exclude=())._slice == _slice
    assert Indices('a', exclude=())[7:2:-2]._slice == slice(7, 2, -2)
    assert Indices('a', exclude=())[3:7]._slice == slice(3, 7, None)

test_Indices___getitem__()

# Generated at 2022-06-12 19:59:12.151399
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():  # pragma: no cover
    from .frame import Frame
    from . import formatters
    import ast
    import os

    def assert_repr(source, expected, enable_formatters=True):
        frame = Frame.get_current(1)
        if enable_formatters:
            formatter = formatters.Formatter()
        else:
            formatter = None
        variable = BaseVariable(source)
        result = variable.items(frame, formatter)
        assert result == expected

    assert_repr('1+2', [('1+2', '3')])
    assert_repr('1/0', [('1/0', 'ZeroDivisionError')])

# Generated at 2022-06-12 19:59:13.108322
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Todo
    pass



# Generated at 2022-06-12 19:59:15.689671
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .test.test_variables import test_BaseVariable_items
    test_BaseVariable_items()

# Generated at 2022-06-12 19:59:21.065544
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('a').items(None) == ()
    assert BaseVariable('a').items(None, normalize="abc") == ()
    assert BaseVariable('a', exclude=("a",)).items(None) == ()
    assert BaseVariable('a', exclude=("b",)).items(None) == ()


# Generated at 2022-06-12 19:59:29.995328
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys
    import math

    frame = sys._getframe()
    source = 'math.pi'
    baseVar = BaseVariable(source)
    print('source = {}'.format(baseVar.source))
    print('exclude = {}'.format(baseVar.exclude))
    items = baseVar.items(frame)
    print('items = {}'.format(items))
    items = sorted(items, key=lambda x: str(x[0]))
    print('items = {}'.format(items))
    if len(items) > 0:
        print('items[0][0] = {}, items[0][0] = {}'.format(items[0][0], items[-1][1]))
    else:
        print('items is empty')


# Generated at 2022-06-12 19:59:37.014211
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types
    import pympler.tracker
    pycompat.check_long()
    l = [1,2,3,4]
    t = (1,2,3,4)
    d = {'key': 'value'}
    s = 'str'
    b = b'bytes'
    m = memoryview(b'bytes')
    v = pycompat.MAXSIZE - 1
    cl = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', b'', 0, b'')
    f = types.FrameType(None, {}, {}, '?', cl)
    mtr = pympler.tracker.SummaryTracker()

# Generated at 2022-06-12 19:59:44.732239
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frames
    from collections import deque
    from .utils import getting_deprecation_warning_with

    class Number(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self.d = 4

    def test_func(frame, exc_type, exc_value, exc_traceback):
        frame.f_locals['foo'] = 123
        frame.f_locals['bar'] = deque([1, 2, 3])
        frame.f_locals['baz'] = Number()

    frame = frames.get_fake_frame_with_locals(test_func)

    # test class BaseVariable
    # test case 1: has no attribute 'items'
    # BaseVariable is an abstract class, it has no attribute 'items

# Generated at 2022-06-12 19:59:49.958598
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:00:00.256965
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class FakeFrame:
        def __init__(self, variables):
            self.f_globals = variables

    frame = FakeFrame({'foo': 'bar', 'baz': {'qux': 'quux'}, 'quuz': ['corge', 'grault']})
    assert BaseVariable('foo').items(frame) == [('foo', 'bar')]
    assert BaseVariable('baz.qux').items(frame) == [('baz', repr({'qux': 'quux'})), ('baz.qux', 'quux')]
    assert BaseVariable('baz').items(frame, True) == [('baz', repr({'qux': 'quux'}))]

# Generated at 2022-06-12 20:00:07.344194
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    d = {'key1':10, 'key2':20}
    import sys
    frame = sys._getframe()
    frame.f_locals['d'] = d
    def fun(x):
        return d
    frame.f_locals['fun'] = fun
    variable = BaseVariable('d', exclude=['key1'])
    result = variable.items(frame)
    assert result == [('d', '{\'key1\': 10, \'key2\': 20}'),('d.key2', '20')]

# Generated at 2022-06-12 20:00:08.884418
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # 1
    result = BaseVariable('a').items(None)
    print('result=',result)
    



# Generated at 2022-06-12 20:00:10.382412
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    var = Indices('whatever')
    assert var[:2] == Indices('whatever')[:2]

# Generated at 2022-06-12 20:00:12.554846
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    arg = inspect.getcallargs(BaseVariable(source="args").items)
    assert arg


# Generated at 2022-06-12 20:00:17.153658
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    v = Indices('a', exclude=(1, 2))
    assert v == v[:]
    v2 = v[:2]
    assert v2 != v
    assert isinstance(v2, Indices)
    assert v2._slice == slice(None, 2)

test_Indices___getitem__()



# Generated at 2022-06-12 20:00:18.918578
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    main_value = 'abc'
    assert BaseVariable(main_value).items(main_value) == [('abc', 'abc')]


# Generated at 2022-06-12 20:00:30.309305
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Variable(BaseVariable):
        def _items(self, key, normalize=False):
            return (self.source, repr(utils.get_shortish_repr(key, normalize=normalize)))

    frame = dict(a=1, b=2, c=3)
    var_a = Variable('a')
    var_a_items = var_a.items(frame)
    assert var_a_items == [('a', "'1'")]

    var_a_b_items = var_a.items(frame, normalize=True)
    assert var_a_b_items == [('a', "'1'")]

    var_a_b_items = Variable('[a, b]').items(frame, normalize=True)

# Generated at 2022-06-12 20:00:34.076549
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class SampleVariable(BaseVariable):
        pass

    variable = SampleVariable('source', 'exclude')
    frame, frame_locals = inspect.currentframe(), {}
    result = variable.items(frame, normalize=True)
    assert result == ()


# Generated at 2022-06-12 20:00:39.985488
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    _add_a_test_method(BaseVariable, 'items')

# Generated at 2022-06-12 20:00:47.739516
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # define the method items for class BaseVariable
    def items_BaseVariable(self, frame, normalize=False):
        try:
            main_value = eval(self.code, frame.f_globals or {}, frame.f_locals)
        except Exception:
            return ()
        return self._items(main_value, normalize)

    # create a test object
    test_obj = BaseVariable('')
    # test the method items for class BaseVariable
    # assert items == ()
    assert items_BaseVariable(test_obj, None) == ()


# Generated at 2022-06-12 20:00:59.331525
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types
    # exclude = ['obj']
    exclude = ('obj',)
    # exclude = ['obj', 'id', 'value']
    # exclude = utils.ensure_tuple(exclude)
    # print(exclude)
    # None = None
    # print(self.exclude)
    def fun(a, b):
        d = {'a':1}
        obj = types.SimpleNamespace(x=2, y=3, a=4, b=5)
        return (a+b, d, obj)

    # source = 'a+b'
    # source = ''
    source = 'obj'
    # source = 'd'
    # source = 'obj.x'
    print(source)
    frame = sys._getframe(0)
    print(frame)

# Generated at 2022-06-12 20:01:04.969465
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Check a normal case
    test_frame = inspect.currentframe()
    test_variable = BaseVariable('test_frame.f_lineno')
    assert len(test_variable.items(test_frame)) == 1
    assert  test_variable.items(test_frame)[0] == ('test_frame.f_lineno', '45')

    # Check a case of exception
    test_variable = BaseVariable('')
    with pytest.raises(Exception):
        test_variable.items(test_frame)



# Generated at 2022-06-12 20:01:15.580925
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_exploding(source, normalize, expected):
        result = Exploding(source).items({}, normalize=normalize)
        assert len(result) == len(expected), 'Expected result and actual one have different lengths'
        assert all(pair1 == pair2 for pair1, pair2 in zip(result, expected)), 'Expected results are not equal to the actual one'

    test_exploding(
        source='(1, 2, 3)',
        normalize=False,
        expected=[
            ('(1, 2, 3)', '(1, 2, 3)'),
            ('(1, 2, 3)[0]', '1'),
            ('(1, 2, 3)[1]', '2'),
            ('(1, 2, 3)[2]', '3')
        ]
    )

    test_exploding

# Generated at 2022-06-12 20:01:22.078750
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    bv = BaseVariable('sys')
    print(bv.items(inspect.currentframe()))

# Append classes in BaseVariable to the current module
sys.modules[__name__].__setattr__(__name__, BaseVariable)
sys.modules[__name__].__setattr__('Attrs', Attrs)
sys.modules[__name__].__setattr__('Keys', Keys)
sys.modules[__name__].__setattr__('Indices', Indices)
sys.modules[__name__].__setattr__('Exploding', Exploding)

# Generated at 2022-06-12 20:01:28.987458
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    '''
    Unit test for method items of class BaseVariable

    >>> my_list = [1, 2, 3]
    >>> class FakeFrame():
    ...     f_globals = {'my_list': my_list}
    >>> Exploding('my_list').items(FakeFrame())
    [('my_list', '[1, 2, 3]'), ('my_list[0]', '1'), ('my_list[1]', '2'), ('my_list[2]', '3')]
    '''
    pass


# Generated at 2022-06-12 20:01:39.720066
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import types
    import inspect
    frame = inspect.getouterframes(inspect.currentframe())[1][0]
    values = dict(
        foo= 'x',
        bar= [1, 2, 3],
        baz='baz',
        qux=1,
        quux=object(),
        corge=types.SimpleNamespace(a=1, b=2, c=3),
        grault=[],
        garply=None,
        waldo={},
        fred={'a': 1, 'b': 2, 'c': 3},
        plugh={4, 5, 6},
        xyz=object()
    )
    def locs(**kwargs):
        return {var: values[var] for var in kwargs}

# Generated at 2022-06-12 20:01:42.331181
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = BaseVariable()
    try:
        var.items()
        return False
    except NotImplementedError as e:
        assert e
        return True


# Generated at 2022-06-12 20:01:47.910562
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import types
    import sys

    class BaseVariable_test(BaseVariable):
        def __init__(self, source, *args, **kwargs):
            BaseVariable.__init__(self, source, *args, **kwargs)

        def _items(self, main_value, normalize=False):
            return [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]

    def get_frame():
        frame = sys._getframe(1)
        while frame.f_globals.get('__name__') not in ('__main__', 'builtins', '__builtin__'):
            frame = frame.f_back
        return frame
            
    var = BaseVariable_test('x', exclude=['y'])
    frame = get_frame

# Generated at 2022-06-12 20:02:04.838489
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = Attrs('a')

    class A:
        a = 123
        def b(self):
            pass

    assert v.items(A.__dict__['a'].__globals__['__dict__']) == [
        ('a', '123'), ('a.a', '123'), ('a.b', '<function>')
    ]

    assert v.exclude.__add__(('a',)) != v.exclude
    v = v.exclude.__add__(('a',))
    print(v.items(A.__dict__['a'].__globals__['__dict__']))
    assert v.items(A.__dict__['a'].__globals__['__dict__']) == [('a.b', '<function>')]
    a = A()



# Generated at 2022-06-12 20:02:14.044928
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import protocol
    from . import protocol_ext

    # test_BaseVariable_items1
    my_var = protocol.DefaultVariable('a')
    frame = protocol_ext.FrameExt('', '', {})
    assert my_var.items(frame) == [('a', '')]
    
    # test_BaseVariable_items2
    my_var = protocol.DefaultVariable('a[1]')
    frame = protocol_ext.FrameExt('', '', {})
    assert my_var.items(frame) == [('a[1]', '')]
    
    # test_BaseVariable_items3
    my_var = protocol.DefaultVariable('a.b')
    frame = protocol_ext.FrameExt('', '', {})
    assert my_var.items(frame) == [('a.b', '')]



# Generated at 2022-06-12 20:02:21.556002
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var1 = BaseVariable('x')
    # emulate frame with 3 variables
    frame = {'x': 1, 'y': 2, 'z': 3}
    frame_items = frame.items()

    # emulate frame with 3 attributes
    frame1 = {}
    frame1.a = 1
    frame1.b = 2
    frame1.c = 3
    frame_items1 = frame1.items()

    # emulate frame with 3 elements
    frame2 = [1, 2, 3]
    frame_items2 = frame2.items()

    print('BaseVariable items test')

    # test for the common case
    if var1.items(frame) == frame_items:
        print('passed')
    else:
        print('failed')

    # test for the case of BaseVariableAttributes
    var2 = Attrs('x')

# Generated at 2022-06-12 20:02:25.766892
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Create a fake frame
    frame = types.FrameType(None, None, None, 'test', {}, None)

    # Create a variable that refers to x
    variable = Attrs('foo')

    # Evaluate x in the frame
    variable.items(frame)


# Generated at 2022-06-12 20:02:34.352009
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # create a test file for test_BaseVariable_items
    with open('BaseVariable_items_test.py', 'w') as f:
        f.write("""
d = {'a': 1, 'b': 2, 'c': 3}
e = (1, 2, 3, 4)
f = [1, 2, 3, 4, 5]
x = 1
""")

    # import the test file BaseVariable_items_test as a module
    import BaseVariable_items_test

    # create a dictionary to store the expected result
    key_vals = dict()
    # loop through the module's global namespace, and copy it to key_vals
    for key,val in vars(BaseVariable_items_test).items():
        key_vals[key] = val
    # create a local namespace for the base variable class

# Generated at 2022-06-12 20:02:37.594142
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class AttrsTest(BaseVariable):
        def _items(self, main_value, normalize=False):
            return {'key':'value'}

    basevariable = AttrsTest('source', exclude='exclude')
    

# Generated at 2022-06-12 20:02:41.857188
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = BaseVariable(source = 'a')
    a.source = 'b'
    a.code = 'code'
    a.unambiguous_source = 'c'
    a.exclude = ('a',)
    print(a.items(frame=None))
# test_BaseVariable_items()


# Generated at 2022-06-12 20:02:46.085786
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
	import inspect
	try:
		src = inspect.getsource(BaseVariable)
		lines = src.split("\n")
		lines = [line.strip() for line in lines]
		for line in lines:
			print(line)
	except IOError:
		pass #probably running in Python 3.x
		

# Generated at 2022-06-12 20:02:56.307920
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Child(BaseVariable):
        def _items(self, key, normalize=False):
            pass

    variable_base_source = Child("source")
    variable_base_exclude = Child("source")
    variable_base = Child("source", exclude=("exclude",))
    variable_different_source = Child("different_source")
    variable_different_exclude = Child("source", exclude=("different_exclude",))
    variable_different_class = Attrs("source", exclude=("different_class",))

    # same source, different excludes
    assert variable_base == variable_base_exclude
    assert variable_base != variable_different_exclude

    # same source, same excludes
    assert variable_base == variable_base

    # different source, same excludes
    assert variable_base != variable_different_source

    #

# Generated at 2022-06-12 20:03:05.445586
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    with open('/tmp/test_pycallgraph.txt', 'w') as f:
        utils.msg('[test_BaseVariable_items]')
        for source in ['a', '(a)', 'a.x', 'a.x.y', 'a["x"].y']:
            v = BaseVariable(source)
            assert v.items({'a': 1}) == [(source, '1')]
            assert v.items({'a': {'x': {'y': 2}}}) == [(source, '{')]
            assert v.items({'a': {'x': None}}) == [(source, 'None')]
            utils.msg(v.items({'a': {'x': None}}))

# Generated at 2022-06-12 20:03:23.715573
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class F(BaseVariable):
        def __init__(self, source, exclude=(), result=()):
            super(F, self).__init__(source, exclude)
            self.result = result
        def _items(self, key, normalize=False):
            return self.result

    # test items
    assert F('x').items({}) == ()
    assert F('x').items({'x': 1}) == (('x', '1'),) 
    assert F('x', []).items({'x': 1}) == (('x', '1'),) 
    assert F('x', ['x']).items({'x': 1}) == () 
    assert F('x', ['y']).items({'x': 1}) == (('x', '1'),) 

# Generated at 2022-06-12 20:03:32.817983
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def display_var(obj, name_of_var):
        print('%s.items() : %s' % (name_of_var, obj.items))

    class BTreeNode(object):
        __slots__ = ['left', 'right']

        def __init__(self):
            self.left = None
            self.right = None

    T = BTreeNode()
    T.left = BTreeNode()
    T.right = BTreeNode()

    # Attrs
    name_of_var = 'Attrs'
    obj = Attrs(name_of_var)
    display_var(obj, name_of_var)

    # Keys
    name_of_var = 'Keys'
    obj = Keys(name_of_var)
    display_var(obj, name_of_var)

   

# Generated at 2022-06-12 20:03:43.553180
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert Attrs('abc').items(dummy_frame({'abc': object()})) == [
        ('abc', '<object>'),
    ]
    assert Attrs('abc').items(dummy_frame({'abc': object()}), normalize=True) == [
        ('abc', '<object>'),
    ]
    assert Attrs('abc').items(dummy_frame({'abc': object()})) == [
        ('abc', '<object>'),
    ]
    assert Attrs('abc').items(dummy_frame({'abc': object()}), normalize=True) == [
        ('abc', '<object>'),
    ]
    assert Attrs('abc', 'm').items(
        dummy_frame({'abc': type('MyClass', (object,), {'m': 42})()})
    )

# Generated at 2022-06-12 20:03:50.328394
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('b')
    c = BaseVariable('c')
    d = BaseVariable('c')
    e = BaseVariable('c')
    f = BaseVariable('a')
    g = BaseVariable('a')
    h = BaseVariable('a')
    i = BaseVariable('a')
    j = BaseVariable('a')
    k = BaseVariable('a')
    l = BaseVariable('a')
    m = BaseVariable('a')
    n = BaseVariable('a')
    o = BaseVariable('a')
    p = BaseVariable('a')
    q = BaseVariable('a')
    r = BaseVariable('a')
    s = BaseVariable('a')
    t = BaseVariable('a')
    
    assert a != b
    assert a != c
    assert a != d

# Generated at 2022-06-12 20:03:56.926098
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestedClass(BaseVariable):
        def _items(self, main_value, normalize=False):
            return main_value
    global_dict = dict(a=1, b=2)
    local_dict = dict(x=11, y=22)
    frame_obj = types.FrameType(f_code=None, f_globals=global_dict, f_locals=local_dict)
    result_tested_class = TestedClass('a').items(frame_obj)
    assert result_tested_class == (1, )

# Generated at 2022-06-12 20:03:59.953999
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable(source="x", exclude=["a"])
    b = BaseVariable(source="x", exclude=["a"])

    assert(a.__eq__(b) == True)
    assert(b.__eq__(a) == True)



# Generated at 2022-06-12 20:04:05.814986
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global my_dict
    # d = {'a': 1, 'b': 2, 'c': 3}
    assert BaseVariable('d').items(d) == [('d', '{...}')]
    assert BaseVariable('d').items(d, True) == [('d', "{'a': 1, 'b': 2, 'c': 3}")]
    # d['a']
    assert BaseVariable('d[a]').items(d) == [('d[a]', '1')]
    # d['x']
    assert BaseVariable('d[x]').items(d) == [('d[x]', '{...}')]
    # d.items()
    assert BaseVariable('d.items()').items(d) == [('d.items()', '{...}')]
    # d.keys()

# Generated at 2022-06-12 20:04:06.644796
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variable = Keys("key")
    variable.items("key")

# Generated at 2022-06-12 20:04:17.698676
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import custom_itertools as it
    x_source = "i"
    x_exclude = ["i"]
    x_eval = "i"
    x_frame = None
    x_normalize = False
    # x_compile_code will be called later
    x_compile_code = compile(x_source, '<variable>', 'eval')
    x_results = [("i", "1"), ("j", "2")]
    class BogusBaseVariable(BaseVariable):
        def __init__(self):
            pass
        def items(self, frame=None, normalize=x_normalize):
            assert frame == x_frame
            assert normalize == x_normalize
            return x_results
    bbv = BogusBaseVariable()

# Generated at 2022-06-12 20:04:23.204728
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    # Simulate subclass
    class DummyVariable(BaseVariable):
        pass

    # Normal comparison
    assert BaseVariable('a') == BaseVariable('a')

    # Different class
    assert BaseVariable('a') != DummyVariable('a')

    # Different source
    assert BaseVariable('a') != BaseVariable('b')

    # Different exclude
    assert BaseVariable('a') != BaseVariable('a', exclude='b')

# Generated at 2022-06-12 20:04:42.310101
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    # Unit test for method items of class CommonVariable
    def test_CommonVariable_items():
        class DummyVariable(CommonVariable):
            def _keys(self, main_value):
                return main_value

            def _format_key(self, key):
                return key

            def _get_value(self, main_value, key):
                return key

        source = 'a'
        exclude = 'b'
        callable = lambda x: x  # noqa
        main_value = {'a', 'b', callable}

        variable = DummyVariable(source, exclude)
        result = variable.items(main_value)


# Generated at 2022-06-12 20:04:49.895809
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    class _(BaseVariable):
        def _items(self, key, normalize=False):
            return ("foo", "bar")
    def f():
        pass
    frame = inspect.currentframe()
    assert _("foo").items(frame) == [("foo", "bar")]
    assert _("foo", "bar").items(frame) == [("foo", "bar")]
    assert _("foo", "bar", "foo").items(frame) == [("foo", "bar")]
    assert _("foo", ("bar", "foo")).items(frame) == [("foo", "bar")]

# Generated at 2022-06-12 20:04:55.028203
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # check whether Attrs.items() works correctly
    # test case 1: check the shortcut of eval
    source = 'obj'
    bv1 = Attrs(source)
    assert source == bv1.source
    assert source == bv1.unambiguous_source
    assert source == bv1.items({'obj': {'a': 1, 'b': 'hello'}})[0][0]
    assert 'hello' == bv1.items({'obj': {'a': 1, 'b': 'hello'}})[0][1]
    # test case 2: check the shortcut of eval
    source = 'obj'
    bv2 = Attrs(source)
    assert source == bv2.source
    assert source == bv2.unambiguous_source

# Generated at 2022-06-12 20:05:06.002359
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
    Test the items method of class BaseVariable
    """
    # Define a dict
    _context = {
        'x': 1,
        'y': 2,
        'somelist': [1, 2, 3, 4],
        'somestring': 'aaaaaaaaaa',
        'somestring_short': 'aaa',
        'someclass': SomeClass(),
        'somedict': {'a': 1, 'b': 2},
    }
    # Add a variable to _context
    _context['x_plus_y'] = _context['x'] + _context['y']
    # Define a variable to be traced
    variable = BaseVariable('x_plus_y')
    # Test the method items
    # Define a dict whose keys are the variables to trace and whose values are the values of the


# Generated at 2022-06-12 20:05:09.081890
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')

    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', exclude='_') != BaseVariable('a', exclude='__')

# Generated at 2022-06-12 20:05:11.979287
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    target=BaseVariable("a")
    assert target.source=="a"
    assert target.exclude==()
    assert target.code==compile("a", "<variable>", "eval")
    assert target.unambiguous_source=="a"
    assert target.items(frame)==(("a", "2"),)
    exclude=("b", "c")
    assert target.exclude==exclude


# Generated at 2022-06-12 20:05:18.853891
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variable_source = 'frame.f_locals'
    variable_source2 = 'frame.f_globals'
    variable_exclude = 'sys'
    variable_exclude2 = tuple('sys')
    variable = BaseVariable(variable_source, variable_exclude)
    variable2 = BaseVariable(variable_source, variable_exclude2)
    variable3 = BaseVariable(variable_source2, variable_exclude2)
    assert variable.items('') == ()
    assert variable2.items('') == ()
    assert variable3.items('') == ()



# Generated at 2022-06-12 20:05:30.708095
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    # frame schema: (frame, globals, line no.)
    frames = [
        (sys._getframe(), {}, 'sys._getframe()'),
    ]
    line_no = inspect.currentframe().f_lineno
    frame = sys._getframe()
    while frame.f_back:
        frame = frame.f_back
        frames.append((frame, frame.f_globals, 'line {}'.format(line_no)))
        line_no = frame.f_lineno

    import re
    import traceback
    from . import utils
    from .pycompat import builtins

    def get_shortish_repr(value, normalize=False):
        """Get shortish version of the variable value"""
        value_repr = utils.repr(value)


# Generated at 2022-06-12 20:05:34.291842
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .context import screen
    screen.BaseVariable.items(main_value, frame)


# Generated at 2022-06-12 20:05:34.820527
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
  return


# Generated at 2022-06-12 20:05:59.383572
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from types import FrameType
    frame = FrameType(None, None, None, None, None, None)
    frame.f_locals = {
        'a': 1,
        'b': [1, 2, 3],
        'c': {'x': 1},
        'd': None
    }

    def test_case(source, expected):
        actual = [x[0] + ': ' + x[1] for x in BaseVariable(source).items(frame)]
        assert actual == expected, '{} -> {} != {}'.format(
            source, actual, expected)

    test_case('a', ['a: 1'])
    test_case('b', ['b: [1, 2, 3]', 'b[0]: 1', 'b[1]: 2', 'b[2]: 3'])
    test_

# Generated at 2022-06-12 20:06:09.026190
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import run
    import collections

    def assert_result(result, expected):
        try:
            assert result == expected
        except:
            raise AssertionError(
                'Variable "[{}]"'.format(','.join(
                    ':'.join(item)
                    for item
                    in result)),
                ' != ',
                'Variable "[{}]"'.format(','.join(
                    ':'.join(item)
                    for item
                    in expected)))

    with run.ignore_exceptions():
        with run.formatter(run.plain_formatter) as f:
            a = []
            a.append(1)

            assert_result(BaseVariable('a').items(f.tb.frame), (('a', '[]'),))

# Generated at 2022-06-12 20:06:17.068237
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = inspect.currentframe()
    assert frame.f_locals['frame'] is frame
    assert frame.f_locals['inspect'] is inspect
    assert frame.f_locals['BaseVariable'] is BaseVariable
    assert frame.f_locals['test_BaseVariable_items'] is test_BaseVariable_items
    assert frame.f_locals['Abc'] is abc.ABC  # Not registered as virtual subclass of BaseVariable for some reason
    assert frame.f_locals['x'] == 5
    assert frame.f_locals['y'] == [6]
    assert frame.f_locals['z'] == {'a': 7}
    assert frame.f_locals['w'] == (8,)
    assert frame.f_locals['v'] == {'a': 9, 'b': 10}
   

# Generated at 2022-06-12 20:06:24.754717
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("abc") == BaseVariable("abc")
    assert not (BaseVariable("abc") == BaseVariable("def"))

    assert Attrs("abc") == Attrs("abc")
    assert not (Attrs("abc") == Attrs("def"))
    assert not (Attrs("abc") == BaseVariable("abc"))

    assert Indices("abc") == Indices("abc")
    assert not (Indices("abc") == Indices("def"))
    assert not (Indices("abc")[2:5] == Indices("abc")[3:8])
    assert not (Indices("abc") == BaseVariable("abc"))

    assert Keys("abc") == Keys("abc")
    assert not (Keys("abc") == Keys("def"))
    assert not (Keys("abc") == BaseVariable("abc"))

    assert Exploding("abc") == Exploding

# Generated at 2022-06-12 20:06:34.689603
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import os
    import threading

    frame = sys._getframe()
    frame._dummy = 1
    frame.f_locals = {'__builtins__': __builtins__}
    frame.f_globals = {'threading': threading, 'os': os}

    # Test for method _items of class CommonVariable
    CommonVariable('frame').items(frame)
    CommonVariable('frame').items(frame, normalize=True)
    Attrs('frame').items(frame)
    Attrs('frame').items(frame, normalize=True)
    Keys('globals()').items(frame)
    Indices('globals().keys()').items(frame)
    Indices('globals().keys()')[:].items(frame)

# Generated at 2022-06-12 20:06:44.406320
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    d = {'a': 1, 'b': 2}
    import logging
    logging.basicConfig(level=logging.DEBUG)
    code = compile('d', '<variable>', 'eval')
    vars = {'d': d}
    frame = {}
    frame.update(vars)
    logging.debug(eval(code, frame.f_globals or {}, frame.f_locals))
    main_value = eval(code, frame.f_globals or {}, frame.f_locals)
    for key in vars.keys():
        try:
            if key in ('a',):
                continue
            value = vars[key]
        except Exception:
            continue

# Generated at 2022-06-12 20:06:46.312712
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('abc')
    v.items('abc')


# Generated at 2022-06-12 20:06:54.314506
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Unit test for method items of class Keys
    frame, frame1 = utils.build_mock_frames(2)
    assert Keys("self.hello['world']").items(frame1) == [("self.hello['world']", '"hello"')]
    # Unit test for method items of class Indices
    assert Indices("self.hello").items(frame1) == [("self.hello[0]",'"hello[0]"')]
    # Unit test for method items of class Attrs
    assert Attrs("self.hello").items(frame1) == [("self.hello.<locals>.world",'"hello"')]
    # Unit test for method items of class Exploding
    assert Exploding('self.hello').items(frame1) == [("self.hello.<locals>.world",'"hello"')]   

# Generated at 2022-06-12 20:06:56.753300
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v = BaseVariable("self.arguments", exclude=())
    assert v == v
    assert v == BaseVariable("self.arguments", exclude=())
    assert not (v == "self.arguments")



# Generated at 2022-06-12 20:07:07.321148
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
    Test the method items of class BaseVariable
    """
    def source_to_item(source):
        """
        Return the items of a source
        """
        item = BaseVariable(source)
        return item.items(frame)

    def source_to_items_list(source):
        """
        Return a list which contains the items of a source
        """
        items = source_to_item(source)
        return list(items)

    frame = frame_locals = {'__name__': 'example', '__doc__': None}
    d = dict(enumerate(range(10)))
    frame_locals['d'] = d
    items = source_to_items_list('d')

# Generated at 2022-06-12 20:07:41.603233
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    dic = {}
    dic['a'] = 1
    import sys
    fr = sys._getframe()
    print(BaseVariable('dic', exclude=('a',)).items(fr))


__all__ = ['BaseVariable', 'Attrs', 'Keys', 'Indices', 'Exploding']

# Generated at 2022-06-12 20:07:52.438780
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import math
    import sympy
    import numpy as np
    # input
    value = np.array([0.1, 0.2, 0.3, 0.2])
    value = sympy.Matrix([[1, 2], [3, 4], [5, 6]])
    value = sympy.Identity(3)
    value = math.pi

    var = BaseVariable('value')
    print(var.items(value))

    #TODO: list comprehension should be used instead of loop
    #to keep variable information
    print([(var.source, var.items(value)) for var in [Keys(), Indices(), Attrs()]])
    print([(var.source, var.items(value)) for var in [Keys(), Indices(), Attrs()]])

# Generated at 2022-06-12 20:07:56.629444
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable("a")
    b = BaseVariable("b")
    assert a != b
    c = BaseVariable("a")
    assert a == c

test_BaseVariable___eq__()

# Generated at 2022-06-12 20:08:01.195240
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    c = BaseVariable('c')
    b = BaseVariable('a', ('x',))
    d = BaseVariable('a')
    e = BaseVariable('a')

    assert a == d
    assert a != c
    assert d == e
    assert b != d
    print('BaseVariable: __eq__ method is ok')


# Generated at 2022-06-12 20:08:03.917862
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')
    assert BaseVariable('a', 'b') == BaseVariable('a', 'c')
    assert BaseVariable('a', 'b') == BaseVariable('a')

# Generated at 2022-06-12 20:08:11.917828
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import pycompat

    class Variable(BaseVariable):
        def _items(self, key, normalize=False):
            return []

    class CommonVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return []

    class Exploding(BaseVariable):
        def _items(self, key, normalize=False):
            return []

    class Attrs(CommonVariable):
        def _items(self, key, normalize=False):
            return []

    class Keys(CommonVariable):
        def _items(self, key, normalize=False):
            return []

    class Indices(Keys):
        _slice = slice(None)

        def _items(self, key, normalize=False):
            return []

    baseVariable = Variable('key')

# Generated at 2022-06-12 20:08:18.075323
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class C(BaseVariable):
        def __init__(self, source='__mocker__.mocker_value', exclude=()):
            BaseVariable.__init__(self, source, exclude)

        def _items(self, key, normalize=False):
            return [('__mocker__', 'mocker_value')]

    res = C()
    assert res.items({'__mocker__': 'mocker_value'}) == [('__mocker__', 'mocker_value')]

# Generated at 2022-06-12 20:08:24.759291
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    d = {'1': 1, '2': 2, '3': 3}
    a = Attrs('a', ['string'])
    b = Attrs('b', ['string'])
    k = Keys('k', ['string'])
    i = Indices('i')
    assert a == a
    assert a != b
    assert a != k
    assert a != i

    assert a._items(d) == Keys('a', ['string']).items(d)
    assert a._items(d) != Keys('b', ['string']).items(d)
    assert a._items(d) != Indices('a', ['string']).items(d)
    assert a._items(d) != Indices('b', ['string']).items(d)



# Generated at 2022-06-12 20:08:29.563942
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import random
    random.seed(4682)

    class Test(object):
        def __init__(self):
            import random
            self.rand = random.random()

    test = Test()
    test.a = 1
    test.b = 2
    test.c = [3, 4]
    test.d = test.c
    frame = sys._getframe()
    frame.f_locals['test'] = test
    frame.f_locals['test_e'] = [test]
    frame.f_locals['test_f'] = [5,6]
    frame.f_locals['test_g'] = {'a': 7, 'b': 8}

    def test_variable(variable):
        print(variable.source)
        print(variable.items(frame))


# Generated at 2022-06-12 20:08:31.497732
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BaseVariable1 = BaseVariable(source="__getitem__")
    BaseVariable2 = BaseVariable(source="__getitem__")
    BaseVariable3 = BaseVariable(source="__str__")
    assert BaseVariable1 == BaseVariable2
    assert BaseVariable1 != BaseVariable3