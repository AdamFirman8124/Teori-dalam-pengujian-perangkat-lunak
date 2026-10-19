

# Generated at 2022-06-12 19:58:51.438951
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .pycompat import builtins
    import types

    def make_frame():
        def test(): pass
        frame = types.FunctionType(test.__code__, builtins)
        frame.f_lineno = 0
        frame.f_globals = None
        frame.f_locals = None
        return frame

    frame = make_frame()
    frame.f_locals.x = 1
    frame.f_locals.y = 2
    frame.f_locals.z = 3
    frame.f_locals.w = (1, 2, 3)
    frame.f_locals.v = ((1, 2, 3), (4, 5, 6))
    frame.f_locals.t = [1, 2, 3]

# Generated at 2022-06-12 19:58:57.406559
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    frame, frame_globals, frame_locals = utils.build_frame({'a':42})
    
    k = Keys('a')
    items = k.items(frame)
    assert len(items) == 1
    assert items[0][0] == 'a[42]'

    k = Keys('a', exclude=42)
    items = k.items(frame)
    assert len(items) == 1
    assert items[0][0] == 'a'

    k = Attrs('a')
    items = k.items(frame)
    assert len(items) == 2
    assert items[0][0] == 'a.__dict__'

    k = Indices('a')
    items = k.items(frame)
    assert len(items) == 1

# Generated at 2022-06-12 19:59:06.240319
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    import operator
    from . import utils
    from . import pycompat
    from . import variables
    import pytest

    def f():
        a = {'b': 1, 'c': 2}
        d = 1
        d.asdasd = 2
        d.asdasdasd = 3
        d.glorp = lambda: a
        a['b'].asd = 'asd'
        sys.a = a
        sys.d = d

    g = utils.get_frame_variables(inspect.currentframe().f_back, common_only=False)

    def my_assert(g, bvar, expected):
        result = pycompat.iteritems(g)
        result = sorted(result, key=operator.itemgetter(0))


# Generated at 2022-06-12 19:59:13.290110
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    """
    测试类 Indices 的 __getitem__ 方法
    """
    i = Indices(1)
    # 在类Indices中，执行了 self._slice = item 可以看到，item其实就是真实的 slice 调用
    # print(i)
    # print(i._slice)
    # print(type(i))
    # 为什么这个地方需要deepcopy这个操作呢？？？因为Indices()类没有这个属性

# Generated at 2022-06-12 19:59:16.637179
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    v = Indices('a')[2:4]
    frame = {'a': [0, 1, 2, 3, 4]}
    print(v.items(frame))



# Generated at 2022-06-12 19:59:18.957214
# Unit test for constructor of class BaseVariable
def test_BaseVariable():
    assert BaseVariable("a", "b")


# Generated at 2022-06-12 19:59:28.433367
# Unit test for constructor of class Indices
def test_Indices():
    assert Indices('f') == Indices('f')
    assert Indices('f') != Indices('g')
    assert set([Indices('f'), Indices('g')]) == set([Indices('f'), Indices('g')])
    assert Indices('f')[2:4] != Indices('f')
    assert Indices('f')[1:3] != Indices('f')[2:4]
    assert set([Indices('f')[1:3], Indices('f')[2:4]]) == set([Indices('f')[1:3], Indices('f')[2:4]])
    assert Indices('f')[1:3] in [Indices('f')[1:3], Indices('f')[2:4]]

# Generated at 2022-06-12 19:59:32.816148
# Unit test for constructor of class Attrs
def test_Attrs():
    attrs = Attrs('foobar')
    assert attrs.source == 'foobar'
    assert attrs.exclude == tuple()
    assert attrs.code.co_names == ('foobar',)
    assert attrs.unambiguous_source == '(foobar)'


# Generated at 2022-06-12 19:59:38.942962
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame_1 = __builtins__.__dict__
    frame_2 = frame_1['__builtins__'].__dict__
    frame_3 = frame_2['__builtins__'].__dict__

# Generated at 2022-06-12 19:59:44.998269
# Unit test for constructor of class Attrs
def test_Attrs():
    class A(object):
        pass
    a = A()
    a.b = 12
    a.c = 'aaa'
    attrs = Attrs('a.')
    assert attrs.source == 'a.'
    assert attrs.unambiguous_source == 'a.'
    assert attrs._keys(a) == ['b', 'c']
    assert attrs._format_key('b') == '.b'
    assert attrs._get_value(a, 'b') == 12
    attrs.exclude = ('b',)
    assert list(attrs._items(a)) == ['a.', '(a.).c']

# Generated at 2022-06-12 19:59:56.432669
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    Main = BaseVariable('main')
    Attrs = BaseVariable('attrs')
    Derived = BaseVariable('derived')

    assert (Main != Attrs)
    assert (Main != Derived)

    assert (Main == Main)
    assert (Attrs == Attrs)
    assert (Derived == Derived)




# Generated at 2022-06-12 20:00:00.142729
# Unit test for constructor of class Indices
def test_Indices():
    assert Indices.__init__(source='aa',exclude=('ss'))

if __name__ == '__main__':
    test_Indices()

# Generated at 2022-06-12 20:00:10.030053
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    global BaseVariable

    from pympler import asizeof
    from . import utils
    from . import pycompat


    class BaseVariable(pycompat.ABC):
        def __init__(self, source):
            self.source = source
            self.code = compile(source, '<variable>', 'eval')

        def __eq__(self, other):
            return (isinstance(other, BaseVariable) and
                    self.source == other.source)


    class CommonVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            super(CommonVariable, self).__init__(source)
            self.exclude = utils.ensure_tuple(exclude)


    common_variable1 = CommonVariable("__main__")

# Generated at 2022-06-12 20:00:13.161378
# Unit test for constructor of class Indices
def test_Indices():
    i = Indices('attrs')
    assert i._keys('string') == range(6)
    assert i._keys(range(10)) == range(10)
    assert i._keys((1,2,3)) == range(3)


# Generated at 2022-06-12 20:00:21.434032
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    class A(object):
        i=1
        j=2
    class B(object):
        i=1
        j=2
        jj=4
    #a = {'x':'1', 'y':'2', 'z':'3'}
    #b = ['1', '2', '3']
    a = A()
    b = B()
    #c = a
    c = a


    x = utils.get_shortish_repr(c, normalize=False)
    print(x)
    x = utils.get_shortish_repr(c, normalize=True)
    print(x)

    x = Keys('a').items(sys._getframe(), normalize=False)
    print(x)

# Generated at 2022-06-12 20:00:32.188692
# Unit test for constructor of class Exploding

# Generated at 2022-06-12 20:00:35.034891
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    b = BaseVariable('a')
    c = BaseVariable('a')
    d = BaseVariable('b')
    result = b == c
    assert result == True
    result = b == d
    assert result == False

# Generated at 2022-06-12 20:00:46.923135
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    assert CommonVariable("a", exclude=["b"]).source == "a"
    assert CommonVariable("a", exclude=("b",)).source == "a"
    assert CommonVariable("a", exclude=("b",)).exclude == ("b",)
    assert CommonVariable("a").source == "a"
    assert CommonVariable("a").exclude == tuple()
    assert CommonVariable("a").code == compile("a", '<variable>', 'eval')
    assert CommonVariable("a").unambiguous_source == "a"
    assert CommonVariable("a.b").unambiguous_source == "(a.b)"
    # Test hash and compare for the object
    v1 = CommonVariable("a")
    v2 = CommonVariable("a")
    v3 = BaseVariable("a")

# Generated at 2022-06-12 20:00:53.085737
# Unit test for constructor of class Keys
def test_Keys():
    k = Keys("var")
    assert k.source == "var"
    assert k.exclude == ()

    k = Keys("var", exclude=("x", "y"))
    assert k.source == "var"
    assert k.exclude == ("x", "y")

    k = Keys("var", "x")
    assert k.source == "var"
    assert k.exclude == ("x",)

# Generated at 2022-06-12 20:00:59.985891
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class SomethingVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return ()

    print('test_BaseVariable___eq__')
    a = BaseVariable('a')
    a_clone = BaseVariable('a')
    b = BaseVariable('b')

    assert hash(a) == hash(a_clone)
    assert a == a_clone

    assert a != b

    assert a != 123
    assert a != 'hello'

# Generated at 2022-06-12 20:01:07.808965
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs('a', 'b') == Attrs('a', 'b')
    assert Attrs('a', 'b') != Attrs('a', 'c')
    assert Attrs('a') != Keys('a')
    assert Attrs('a') != Indices('a')
    assert Keys('a') != Indices('a')



# Generated at 2022-06-12 20:01:14.100624
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test(a, b, c, v):
        s = BaseVariable(a, b)
        r = s.items(c)
        print(r)
        assert r == v

    lglobals = {'__name__': '__main__',
                '__doc__': None,
                '__package__': None,
                '__loader__': None,
                '__spec__': None,
                '__annotations__': {},
                '__builtins__': {},
                '__file__': '/Users/lianghe/Desktop/charles/python/visual-stack/tests/test_variable.py',
                '__cached__': None}
    lname = 'test_BaseVariable_items'

# Generated at 2022-06-12 20:01:16.040909
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    i = Indices("mydict")
    a_slice = slice(0,2)
    i = i[a_slice]
    assert (i._slice == a_slice)



# Generated at 2022-06-12 20:01:22.133612
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = inspect.currentframe()
    from pprint import pprint
    pprint(Attrs('inspect').items(frame))
    pprint(Keys('inspect').items(frame))
    pprint(Indices('inspect').items(frame))
    pprint(Exploding('inspect').items(frame))
    pprint(Exploding('inspect').items(frame))
    pprint(Exploding('inspect').items(frame))
    pprint(Exploding('inspect').items(frame))
if __name__=="__main__":
    test_BaseVariable_items()

# Generated at 2022-06-12 20:01:25.937506
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    x = 4
    frame = pycompat.fake_frame([], [], {"x": x})
    vars_ = BaseVariable("x")
    assert vars_.items(frame)[0][1] == utils.get_shortish_repr(x)


# Generated at 2022-06-12 20:01:28.485329
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    fake_indices = Indices('items.params')
    sliced_indices = fake_indices[:]
    assert(sliced_indices._slice == slice(None))



# Generated at 2022-06-12 20:01:32.544461
# Unit test for constructor of class BaseVariable
def test_BaseVariable():
    source = 'a'
    exclude = ()
    b = BaseVariable(source, exclude)
    assert b.source == 'a'
    assert b.exclude == ()
    assert b.code == compile('a', '<variable>', 'eval')
    assert not needs_parentheses(source)
    assert b.unambiguous_source == 'a'


# Generated at 2022-06-12 20:01:34.526948
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('data') == BaseVariable('data')
    assert BaseVariable('data') != BaseVariable('data2')

# Generated at 2022-06-12 20:01:37.035258
# Unit test for constructor of class CommonVariable
def test_CommonVariable():
    variable = CommonVariable("var")
    try:
        variable._get_value("var")
    except:
        pass


# Generated at 2022-06-12 20:01:46.213733
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import types

    class Test:
        pass
    local_names = {'source': 'xyz', 'frame': [object(), object()], 'Test': Test}
    local_names['frame'][0].f_locals = deepcopy(local_names)
    local_names['frame'][0].f_globals = types.ModuleType('__main__')
    local_names['frame'][1].f_locals = {'frame': local_names['frame'][0]}


# Generated at 2022-06-12 20:02:03.477644
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def get_items(variables, frame):
        """
        Get items for related class of BaseVariable
        """
        assert isinstance(variables, BaseVariable)
        return variables.items(frame, normalize=False)

    def assert_items_equal(items1, items2):
        assert items1 == items2
        for i in items1:
            assert isinstance(i, tuple)
            assert len(i) == 2
            assert isinstance(i[0], str)
            assert isinstance(i[1], str)

    class MyDict(Mapping):
        def __init__(self, keys):
            self.keys = keys
        def __iter__(self):
            return iter(self.keys)
        def __len__(self):
            return len(self.keys)

# Generated at 2022-06-12 20:02:11.796629
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    import types

    def foo():
        print("hi")

    test_locals = {}

    test_locals["bar"] = "bar"
    test_locals["globals"] = "globals"
    test_locals["foo"] = foo
    test_locals["baz"] = {1:2, 3:4, 5:6}
    test_locals["baz"][1] = "one"
    test_locals["baz"][3] = "three"
    test_locals["baz"][5] = "five"
    test_locals["sys"] = sys
    test_locals["types"] = types
    frame = inspect.currentframe()
    test_locals["frame"] = frame
    test_locals["frame"].f

# Generated at 2022-06-12 20:02:15.372647
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    main_value = [{'a': 1}, 2, '3']
    test_cls = BaseVariable("mainvalue")
    result = test_cls.items(main_value)
    assert result == [("mainvalue", "[{'a': 1}, 2, '3']")]



# Generated at 2022-06-12 20:02:26.033847
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def test(func, instance, expected):
        assert func(instance, expected) == True, "expected is {}".format(expected)

    test(lambda instance, expected: instance == expected, BaseVariable("x"), BaseVariable("x"))
    test(lambda instance, expected: instance == expected, BaseVariable("x"), BaseVariable("x", ("y", "z")))
    test(lambda instance, expected: instance == expected, BaseVariable("x", ("y", "z")), BaseVariable("x"))
    test(lambda instance, expected: instance == expected, BaseVariable("x", ("y", "z")), BaseVariable("x", ("y", "z")))
    test(lambda instance, expected: instance == expected, BaseVariable("X", ("y", "z")), BaseVariable("x", ("a", "b")))

# Generated at 2022-06-12 20:02:34.568688
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import frame

    vars = Attrs('a').items(frame((("a", 1))))
    assert len(vars) == 1 and vars[0] == ('a', '1')
    vars = Attrs('a').items(frame((("a", (1, 2, 3)))))
    assert len(vars) == 4 and ('a', '1') in vars and ('a[1]', '2') in vars
    vars = Attrs('a').items(frame((("a", {1: 2, 3: 4}))), normalize=True)
    assert len(vars) == 4 and ('a', '{...}') in vars and ('a[1]', '2') in vars
    vars = Indices('a').items(frame((("a", [1, 2, 3]))))

# Generated at 2022-06-12 20:02:36.699365
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('bbb', exclude=('c',))
    variable2 = BaseVariable('bbb', exclude=('c',))

    assert variable1 == variable2 == variable1

# Generated at 2022-06-12 20:02:41.905255
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Initialization
    source = 'b'
    exclude = []
    evalCode = compile(source, '<variable>', 'eval')
    evalParentheses = compile('({})'.format(source), '<variable>', 'eval')
    baseVariable = BaseVariable(source, exclude)
    # Test baseVariable.code
    expected_result = evalCode
    actual_result = baseVariable.code
    assert actual_result == expected_result
    # Test baseVariable.unambiguous_source
    expected_result = '({})'.format(source)
    actual_result = baseVariable.unambiguous_source
    assert actual_result == expected_result


# Generated at 2022-06-12 20:02:43.858038
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('b')
    assert (a == b) == False


# Generated at 2022-06-12 20:02:45.950508
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Variable(BaseVariable):
        def _items(self, key, normalize=False):
            return []

    v = Variable('x', 'A')
    v.items()
    v.items(normalize=True)

# Generated at 2022-06-12 20:02:52.428040
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Case 1: Case 1: Attrs
    class C1():
        def __init__(self, a, b, c):
            self.a=a
            self.b=b
            self.c=c
    c1 = C1(1,2,3)
    v1 = Attrs('c', exclude=('a',))
    assert v1.items(None)==[('c', 'C1(a=1, b=2, c=3)'),
                            ('(c).b', '2'),
                            ('(c).c', '3')]
    # Case 2: Case 2: Keys
    d2 = {'a':1, 'b':2}
    v2 = Keys('d', exclude=('a',))

# Generated at 2022-06-12 20:03:02.734579
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """Unit test for method __eq__ of class BaseVariable"""
    var1 = BaseVariable('var1')
    var2 = BaseVariable('var1')
    var3 = BaseVariable('var1', exclude='exclude')
    var4 = BaseVariable('var2')
    var5 = BaseVariable('var2', exclude='exclude')
    assert var1 == var2
    assert var1 != var3
    assert var1 != var4
    assert var4 != var5

# Generated at 2022-06-12 20:03:04.786835
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    attrs = Attrs('x')
    attrs2 = Attrs('x')
    assert attrs.__eq__(attrs2)



# Generated at 2022-06-12 20:03:10.027143
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('x').items({'x': 1}) == [('x', '1')]
    assert BaseVariable('x', 'y').items({'x': 1, 'y': 2}) == [('x', '1')]
    assert BaseVariable('x', 'z').items({'x': 1, 'y': 2}) == [('x', '1'), ('x.y', '2')]
    assert BaseVariable('x').items({'x': lambda: 1}) == [('x', '<function BaseVariable.test_BaseVariable_items.<locals>.<lambda> at 0x106711598>')]



# Generated at 2022-06-12 20:03:15.501293
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = Attrs('var1', exclude=['exclude1', 'exclude2'])
    var2 = Attrs('var2', exclude=['exclude2', 'exclude3'])
    var3 = Attrs('var1', exclude=['exclude1', 'exclude2'])
    assert var1.__eq__(var3)
    assert not var1.__eq__(var2)

# Generated at 2022-06-12 20:03:19.238299
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("abc")
    v2 = BaseVariable("abc")
    v3 = BaseVariable("def")
    v4 = BaseVariable("abc", "def")
    v5 = BaseVariable("abc", "ghi")
    assert v1 == v2
    assert hash(v1) == hash(v2)
    assert v1 != v3
    assert v1 != v4
    assert v1 != v5
    print("PASS")


# Generated at 2022-06-12 20:03:24.562456
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect 
    def test_func():
        d = {'k1':'v1'}
        return d['k1']
    frame = inspect.currentframe()
    variable = BaseVariable('d', exclude=('items',))
    variable.items(frame)

test_BaseVariable_items()

# Generated at 2022-06-12 20:03:31.513883
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class FakeFrame(object):
        f_globals = {'a': 1}
        f_locals = {'b':2}
    fake_frame = FakeFrame()
    print(BaseVariable('a').items(fake_frame))
    print(BaseVariable('b').items(fake_frame))
    print(BaseVariable('c').items(fake_frame))
    print(BaseVariable('a+b').items(fake_frame))

    print(Exploding('a').items(fake_frame))

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:03:34.850491
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('b')
    a1 = BaseVariable('a')

    # True if same object
    assert(a == a)

    # False if different object
    assert(not (a == b))

    # True if equal object
    assert(a == a1)

"""
Tests for method items of class BaseVariable
"""

# Generated at 2022-06-12 20:03:45.572329
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import inspect
    _test_BaseVariable___eq___code = inspect.getsource(test_BaseVariable___eq__)
    _test_BaseVariable___eq___bytecode = compile(_test_BaseVariable___eq___code, '<string>', 'exec')

    import sys
    _test_BaseVariable___eq___frame = sys._getframe(0)
    test_BaseVariable___eq___code = BaseVariable('test_BaseVariable___eq___code', '(_test_BaseVariable___eq___frame, _test_BaseVariable___eq___bytecode)')
    test_BaseVariable___eq___bytecode = BaseVariable('test_BaseVariable___eq___bytecode', '(_test_BaseVariable___eq___frame, test_BaseVariable___eq___code)')

# Generated at 2022-06-12 20:03:54.540152
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    base_var1 = BaseVariable('test')
    base_var2 = BaseVariable('test')
    base_var3 = BaseVariable('test', exclude=('test_exclude_1', 'test_exclude_2'))
    base_var4 = BaseVariable('test', exclude=('test_exclude_1'))
    base_var5 = BaseVariable('test_2')

    assert base_var1 == base_var2
    assert base_var1 != base_var3
    assert base_var3 != base_var4
    assert base_var1 != base_var5
    assert base_var2 != base_var5
    assert base_var3 != base_var5
    assert base_var4 != base_var5

# Generated at 2022-06-12 20:04:07.940849
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class BaseVariableSub(BaseVariable):
        def _format_key(self, key):
            return '[{}]'.format(key)
        def _get_value(self, main_value, key):
            return main_value[key]
        def _keys(self, main_value):
            return main_value.keys()

    class VariableSub(BaseVariableSub):
        pass

    class VariableSubSub(VariableSub):
        pass

    class VariableSubSubSub(VariableSubSub):
        pass

    locals_ = {'str':str}

    print(BaseVariable('str').items(locals_))

    print(BaseVariableSub('str').items(locals_))

    print(VariableSub('str').items(locals_))

    print(VariableSubSub('str').items(locals_))


# Generated at 2022-06-12 20:04:17.393299
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import requests
    
    res = requests.get("http://127.0.0.1:8000/get_user_info/")
    response_json = eval(res.text)
    print(response_json)
    
    res = requests.get("http://127.0.0.1:8000/get_last_trade_price/")
    response_json = eval(res.text)
    print(response_json)
    
    res = requests.get("http://127.0.0.1:8000/get_withdrawal_list/")
    response_json = eval(res.text)
    print(response_json)

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:04:26.856784
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    context = {'a': 1, 'b': [2, 3], 'c': {'k': 'v'}}

    assert Keys('b').items(context) == [
        ('b', '[2, 3]'),
        ('b[0]', '2'),
        ('b[1]', '3')
    ]

    assert Keys('c').items(context) == [
        ('c', "{'k': 'v'}"),
        ("c['k']", "'v'")
    ]
    assert Attrs('c').items(context) == [
        ('c', "{'k': 'v'}"),
    ]


# Generated at 2022-06-12 20:04:28.350240
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pdb; pdb.set_trace()
    variable = BaseVariable('x')
    variable.items()

# Generated at 2022-06-12 20:04:35.158999
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import config
    from . import debugger
    from . import utils
    from . import test_utils
    from . import pycompat

    if not pycompat.PY3:
        return

    config.default._hide_frames = ()
    config.default._include_frames = ()
    config.default._variable = ('a', 'b', 'c')
    config.default._on_fault = True
    config.default._watch_variables = ()
    config.default._disable_stdin = False
    config.default._show_hidden_frames = False
    config.default._watch_expression = ()

    def foo(x):
        y = bar(x)
        return y

    def bar(x):
        z = baz(x)
        return z

    def baz(x):
        return x

# Generated at 2022-06-12 20:04:45.757232
# Unit test for method items of class BaseVariable
def test_BaseVariable_items(): 
    import inspect
    import math
    import os
    import sys
    import random
    import math
    import sys
    from collections import deque
    from collections import defaultdict
    from collections import OrderedDict
    from collections import Counter
    from enum import Enum
    from types import ModuleType
    #@Dict
    class People(object):
        def __init__(self):
            self.dict_name = {'Tom':1,'Jim':1,'Jack':1}
        def keys(self):
            return list(self.dict_name.keys())
        def __getitem__(self,key):
            return self.dict_name[key]
        @staticmethod
        def __new__(cls):
            return super(People,cls).__new__(cls)
    people = People()
    #

# Generated at 2022-06-12 20:04:54.873326
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    local_var = 'local'
    inspect.currentframe().f_locals['local_var'] = local_var
    global_var = 'global'
    inspect.currentframe().f_globals['global_var'] = global_var
    assert BaseVariable('local_var').items(inspect.currentframe()) == (
        ('local_var', '\'local\''),
    )
    assert BaseVariable('global_var').items(inspect.currentframe()) == (
        ('global_var', '\'global\''),
    )
    assert BaseVariable('self').items(inspect.currentframe()) == ()

# Generated at 2022-06-12 20:05:05.888014
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Create a dummy class
    class DummyObject(object):
        def __init__(self):
            self.a = 1

    # Create a dummy function
    def dummy_func(x):
        return x

    # Create a dummy frame
    dummy_frame = lambda: None
    dummy_frame.f_globals = {'DummyObject': DummyObject, 'dummy_func': dummy_func}
    dummy_frame.f_locals = {'foo': DummyObject(), 'bar': dummy_func}

    # Test for Attrs
    attrs = Attrs('foo')
    assert attrs.items(dummy_frame) == [('foo', 'DummyObject()'), ('foo.a', '1')]

    # Test for Keys
    keys = Keys('foo')

# Generated at 2022-06-12 20:05:16.199523
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys
    from collections import OrderedDict
    from . import get_frame_locals

    frame = inspect.currentframe()
    assert frame is not None, 'This unit test must be run from inside a function'
    # get the frame of the calling function
    frame = frame.f_back
    frame_locals = get_frame_locals(frame)
    # get the frame locals
    frame_locals['main_value'] = frame
    # assign the frame to the variable main_value
    # test code
    assert frame_locals == frame
    # the above line is true, because both variables represent the same dictionary
    var = BaseVariable('main_value')
    # get the variable from the user input
    assert var
    # a variable has been created, thus it does not evaluate to False
    assert isinstance

# Generated at 2022-06-12 20:05:22.718140
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
	assert BaseVariable('f').items('f') == ('f', 'f')
	assert BaseVariable('f').items(1) == ('f', '1')
	assert BaseVariable('f').items(None) == ('f', 'None')
	# 只要f不是一个变量，就都是合法的
	assert BaseVariable('f').items("f") == ('f', "'f'")
	assert BaseVariable('f', ['a']).items("f") == ('f', "'f'")
	assert BaseVariable('f', ['a']).items("g") == ('f', "'g'")
	assert BaseVariable('f', ['a']).items("a") == ('f', "'a'")

# Generated at 2022-06-12 20:05:42.645730
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    y = 12
    def foo():
        return 10

    class Bar(object):
        a = 10
        b = 20

        @classmethod
        def c(cls):
            return 30

        @staticmethod
        def d():
            return 30

    result = (('foo', '10'), ('Bar.a', '10'), ('Bar.b', '20'), ('Bar.c', '30'), ('Bar.d', '30'), ('y', '12'))
    frame = foo.__code__.co_firstlineno + 2


# Generated at 2022-06-12 20:05:47.147051
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = Keys('a')
    frame = inspect.currentframe()
    assert var.items(frame) == [('a', '{}')]
    assert var.items(frame, normalize=True) == [('a', '{}')]

# Generated at 2022-06-12 20:05:52.199931
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Var(BaseVariable):

        def _items(self, key, normalize=False):
            return [(key, key)]

    # Ensure that items of BaseVariable raise error when _items is not implemented
    try:
        Var('').items(None)
        assert False
    except NotImplementedError:
        pass
    assert Var('').items(None) == [('', '')]


# Generated at 2022-06-12 20:05:56.248459
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_basevariable_items(source, exclude, frame):
        var = BaseVariable(source, exclude)
        return var.items(frame)

    exclude = 'exclude'
    frame = _debug_frame()
    source = 'source'

    result = test_basevariable_items(source, exclude, frame)
    assert result == ()



# Generated at 2022-06-12 20:05:59.080679
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('1')
    v._get_value
    v._items
    v._safe_keys
    v._keys
    v.items()
    v._format_key



# Generated at 2022-06-12 20:06:04.950568
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:06:07.222727
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = BaseVariable('value')
    assert bv.items(dict(value=1)) == (('value', 1), )


# Generated at 2022-06-12 20:06:12.231711
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('a').items({'a': 1}) == (('a', '1'),)
    assert BaseVariable('x', exclude=['a']).items({'x': {'a': 1}}) == (('x', "{'a': 1}"),)
    assert BaseVariable('x').items({'x': {'a': 1}}) == (('x', "{'a': 1}"), ('x.a', '1'))


# Generated at 2022-06-12 20:06:18.277957
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import json
    import sys
    from pymongo import MongoClient
    from . import pycompat
    from . import utils

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": pycompat.datetime.datetime.utcnow()
    }


# Generated at 2022-06-12 20:06:26.066784
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def f(x):
        a = {'a': 12}  # noqa
        b = [1, 2, 3]  # noqa
        c = (1, 2, 3)  # noqa
        d = 12  # noqa
        e = object()  # noqa
        f = object()  # noqa
        e.x = f  # noqa
        f.x = e  # noqa
        return x

    import sys
    import types
    frame = sys._getframe().f_back
    frame.f_globals.update(globals())
    variables = [Keys('x'), Indices('x'), Attrs('x'), Exploding('x')]
    for variable in variables:
        items = variable.items(frame)
        assert len(items) > 0

# Generated at 2022-06-12 20:06:52.636465
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from pprint import pprint

    frame = sys._getframe()

    dummy_dict = {
        'a': 1,
        'b': {
            'x': 2,
            'y': 3
        },
        'c': [1, 2, 3]
    }

    dummy_dict_keys = ['a', 'b', 'c']

    dummy_dict_nested_keys = ['a', 'b.x', 'b.y', 'c.0', 'c.1', 'c.2', ]

    dummy_list = [1, 2, 3]

    dummy_list_keys = ['[0]', '[1]', '[2]']

    dummy_class = type('dummy', (object,), {'x': 1, 'y': 2})


# Generated at 2022-06-12 20:06:58.222322
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test exception
    test_source = 'abc'
    test_variable = BaseVariable(test_source)
    frame = {}
    result = test_variable.items(frame)
    assert result == ()

    # Test source
    test_source = 'a'
    test_variable = BaseVariable(test_source)
    frame = {'a': 1}
    result = test_variable.items(frame)
    assert result == [('a', '1')]


# Generated at 2022-06-12 20:07:03.721133
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_Attrs():
        class Test(object):
            def __init__(self):
                self.a = 1
                self.b = 2

        t = Test()
        v = Attrs('t', exclude='b')
        assert v.items(None) == [('t', '<__main__.Test object at 0x7f88eac48320>'), ('t.a', '1')]

    def test_Keys():
        v = Keys('t', exclude=0)
        t = {2: 3, 1: 4}
        assert v.items(None, normalize=True) == [('t', "{1: 4, 2: 3}"), ('t[1]', '4'), ('t[2]', '3')]


# Generated at 2022-06-12 20:07:07.151831
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'a.b.c'
    exclude = ('d', )
    frame = None
    normalize = True

    variable = BaseVariable(source, exclude)
    assert variable.items(frame, normalize) == []



# Generated at 2022-06-12 20:07:16.219785
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import frameinfo
    frame, frameinfo = frameinfo()
    globals, locals = frame.f_globals, frame.f_locals
    # Testing Attrs
    # for class
    source = 'Attrs'
    a = Attrs(source)
    result = a.items(frame)
    print(result)
    # for instance
    source = 'frameinfo'
    a = Attrs(source)
    result = a.items(frame)
    print(result)
    # Testing Keys
    # for dict
    source = 'globals'
    k = Keys(source)
    result = k.items(frame)
    print(result)
    # for OrderedDict
    source = 'locals'
    k = Keys(source)
    result = k.items(frame)
   

# Generated at 2022-06-12 20:07:27.668398
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    x = 'foo'
    z = 'baz'
    mydict = {'foo': 42, 'bar': 43, 'baz': 44}
    mylist = [1, 2, 3]
    mytuple = (1, 2, 3)
    myset = set([1, 2, 3])
    myfrozenset = frozenset([1, 2, 3])
    myobj = type('MyObject', (object,), {})()
    myint = 12345

    def myfunc():
        """Docstring."""
        pass

    def mygenerator():
        """Docstring."""
        yield 1
        yield 2

    myclass = type('MyClass', (object,), {})
    myclass2 = type('MyClass2', (object,), {})
    myinstance = myclass()
    my

# Generated at 2022-06-12 20:07:37.931535
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .pycompat import StringIO
    import sys
    int_type = 1
    float_type = 1.0
    str_type = 'str'
    bool_type = True
    list_type = [int_type, float_type, str_type, bool_type]
    dict_type = {"a": int_type, "b": float_type, "c": str_type, "d": bool_type}
    set_type = set(list_type)
    tuple_type = tuple(list_type)
    # test for class BaseVariable
    if sys.version_info >= (3, 3):
        from .pycompat import OrderedDict
        OrderedDict_type = OrderedDict()
        OrderedDict_type["a"] = int_type

# Generated at 2022-06-12 20:07:44.336795
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]

    d = {'foo': {'bar': 'baz'}}
    d_shortish_repr = utils.get_shortish_repr(d)

    variable = TestVariable('d', exclude=['foo'])
    assert variable.items(frame={'d': d}).pop() == ('d', '{' + d_shortish_repr + '}')


# Generated at 2022-06-12 20:07:54.666338
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import os
    import io
    class DummyFileIO(io.FileIO):
        def __init__(self):
            pass
    dummy_file = DummyFileIO()
    dummy_file.name = "[Errno 5]: Input/Output Error: '/dev/mapper/vg_sairam-LogVol00'"
    dummy_file.closed = False
    dummy_file.mode = 'r+b'
    dummy_file.fileno = lambda: 5
    dummy_file.isatty = lambda: True
    dummy_file.tell = lambda: 0
    dummy_file.write = lambda s: 0
    dummy_file.flush = lambda: None
    dummy_file.close = lambda: None
    dummy_file.read = lambda n: None
    dummy_file.readinto = lambda b: None

# Generated at 2022-06-12 20:08:01.356439
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def myfunc(x, y=1, *z, **zkw):
        print('Hello, world!')
    myfunc(0)
    frame = sys._getframe()
    print(frame.f_locals)
    base = BaseVariable('myfunc', 'z')
    print(base.items(frame))
    print('==========')
    print(Keys('myfunc').items(frame, True))
    print(Indices('z').items(frame))


if __name__ == '__main__':
    test_BaseVariable_items()