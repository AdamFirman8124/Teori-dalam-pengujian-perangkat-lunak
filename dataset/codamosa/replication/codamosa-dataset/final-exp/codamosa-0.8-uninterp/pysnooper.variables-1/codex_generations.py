

# Generated at 2022-06-12 19:58:45.972136
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    a = Indices('a')
    assert a['b':] == Indices('a', slice(None, 'b', None))
    assert a[:'b':2] == Indices('a', slice(':b:2', None, None))

# Generated at 2022-06-12 19:58:47.560199
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = "@test.py:143:test_simple"
    exclude = ()
    var = BaseVariable(source, exclude)
    assert var.items(frame) == ()


# Generated at 2022-06-12 19:58:50.068094
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    a = Indices("a")[1:3]
    assert a._slice == slice(1,3,None)

# Generated at 2022-06-12 19:58:54.331076
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a')
    var2 = BaseVariable('a')
    var3 = BaseVariable('a', exclude=('b', ))
    var4 = BaseVariable('a')
    var5 = BaseVariable('a', exclude=('b', 'c', ))

    assert(var1 == var2)
    assert(var1 != var3)
    assert(var1 == var4)
    assert(var1 != var5)

# Generated at 2022-06-12 19:58:57.077537
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    b1 = BaseVariable('b1')
    assert b1 == BaseVariable('b1')
    assert b1 != Attrs('b2')



# Generated at 2022-06-12 19:59:05.804145
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # '<' (less than)
    assert BaseVariable('<', '<') == BaseVariable('<', '<')

    # '<=' (less than or equal to)
    assert BaseVariable('<', '<=') == BaseVariable('<', '<=')

    # '==' (equal to)
    assert NotImplemented == BaseVariable('==', '==')

    # '!=' (not equal to)
    assert BaseVariable('!=', '!=') == NotImplemented

    # '>=' (greater than or equal to)
    assert BaseVariable('>', '>=') == BaseVariable('>', '>=')

    # '>' (greater than)
    assert BaseVariable('>', '>') == BaseVariable('>', '>')


# Generated at 2022-06-12 19:59:07.378981
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    test_frame = inspect.stack()[1][0]
    test_var = 'list(range(5))'
    test_variable = Indices(test_var)
    test_variable.items(test_frame)


# Generated at 2022-06-12 19:59:09.791402
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    r = Indices('foo', exclude=['_blah'])({})
    assert isinstance(r, Indices)
    assert r._slice == slice(None)
    r = r[::-1]
    assert r._slice == slice(None, None, -1)


# Generated at 2022-06-12 19:59:12.493707
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class LocalVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return [(self.source, utils.get_shortish_repr(key))]

    import inspect
    frame = inspect.currentframe()
    variable = LocalVariable('abc')
    print(variable.items(frame))


# Generated at 2022-06-12 19:59:24.516424
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class BaseVariableSub(BaseVariable):
        pass

    BaseVariableSub1 = BaseVariableSub('BaseVariableSub1')
    BaseVariableSub2 = BaseVariableSub('BaseVariableSub2')
    BaseVariableSub3 = BaseVariableSub('BaseVariableSub1')
    BaseVariableSub4 = BaseVariableSub('BaseVariableSub1', exclude='a')
    BaseVariableSub5 = BaseVariableSub('BaseVariableSub1', exclude='a,b')
    x = 5

    assert BaseVariableSub1 == BaseVariableSub1
    assert BaseVariableSub1 == BaseVariableSub3
    assert BaseVariableSub1 == BaseVariableSub4
    assert BaseVariableSub1 != BaseVariableSub2
    assert BaseVariableSub1 == BaseVariableSub5

    def f():
        pass

    assert BaseVariableSub(f) == BaseVariableSub(f)



# Generated at 2022-06-12 19:59:40.957027
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v_dict = {'x': 1, 'y': 2}
    v_list = [1, 2, 3]
    v_tuple = (1, 2)
    v_obj = object()
    d_frame = {'v_dict': v_dict, 'v_list': v_list,
           'v_tuple': v_tuple, 'v_obj': v_obj}
    frame = lambda: 0
    frame.f_locals = d_frame
    
    assert Attrs('v_dict').items(frame) == [
        ('v_dict', '{' + repr(v_dict) + '}'),
        ('v_dict.x', repr(v_dict['x'])),
        ('v_dict.y', repr(v_dict['y']))
    ]
    

# Generated at 2022-06-12 19:59:50.837520
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    results = []

    class A(BaseVariable):
        def _items(self, key, normalize=False):
            pass


    class B(BaseVariable):
        def _items(self, key, normalize=False):
            pass


    x = A('test1')
    results.append(x == x)
    
    x = A('test2')
    y = A('test2')
    results.append(x == y)

    x = A('test2', ('abc', 'def'))
    y = A('test2', ('abc', 'def'))
    results.append(x == y)

    x = A('test3', ('abc', 'def'))
    y = A('test3', ('def', 'abc'))
    results.append(x == y)


# Generated at 2022-06-12 19:59:56.855551
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('x', 'y') == BaseVariable('x', 'y')
    assert BaseVariable('x') == BaseVariable('x')
    assert BaseVariable('x') != BaseVariable('y')
    assert BaseVariable('x', 'y') != BaseVariable('x')
    assert BaseVariable('x', 'y') != BaseVariable('y', 'z')


# Generated at 2022-06-12 20:00:01.155244
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable = BaseVariable('a', exclude=1)
    variable1 = BaseVariable('a', exclude=())
    variable2 = BaseVariable('b', exclude=1)

    assert variable == variable1
    assert variable != variable2



# Generated at 2022-06-12 20:00:10.637183
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('i', 'j')
    v2 = BaseVariable('i', 'j')
    v3 = BaseVariable('i', 'j')
    v4 = BaseVariable('i', ('j',))
    v5 = BaseVariable('i', ('j',))
    v6 = BaseVariable('k', 'j')
    v7 = BaseVariable('k', 'j')
    v8 = BaseVariable('k', ('j',))
    v9 = BaseVariable('k', ('j',))
    v10 = Attrs('i', 'j')
    v11 = Attrs('i', 'j')
    v12 = Attrs('i', 'j')
    v13 = Attrs('i', ('j',))
    v14 = Attrs('i', ('j',))
    v15 = Keys('i', 'j')

# Generated at 2022-06-12 20:00:19.959408
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # class Attrs(CommonVariable)
    # class Keys(CommonVariable)
    # class Indices(Keys)
    # class Exploding(BaseVariable)
    A1=Attrs("A",("B",))
    A2=Attrs("A",("B",))
    assert ( A1 == A2 ) is True
    K1=Keys("K",("B",))
    K2=Keys("K",("B",))
    assert ( K1 == K2 ) is True
    I1=Indices("I",("B",))
    I2=Indices("I",("B",))
    assert ( I1 == I2 ) is True
    E1=Exploding("E",("B",))
    E2=Exploding("E",("B",))
    assert ( E1 == E2 ) is True

# Generated at 2022-06-12 20:00:22.528727
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('')
    v2 = BaseVariable('')
    assert v1.__eq__(v2)


# Generated at 2022-06-12 20:00:24.149116
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    # Create a dummy instance
    var = Indices('var')
    
    # Run method
    result = var.__getitem__(slice(1, 2))
    
    # Should be an instance of Indices
    assert isinstance(result, Indices)

# Generated at 2022-06-12 20:00:33.882862
# Unit test for method __eq__ of class BaseVariable

# Generated at 2022-06-12 20:00:38.228520
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    l = [1, 2, 3, 4, 5]
    var = Indices('l')[1:3]
    items = var.items(None)
    assert items == [('l[1]', '2'), ('l[2]', '3')]

# Generated at 2022-06-12 20:00:51.931573
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class BaseVariableSubclass(BaseVariable):
        def __init__(self, source, exclude=()):
            super().__init__(source, exclude)
            self.variable_test = 1


# Generated at 2022-06-12 20:00:52.737299
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:00:57.965482
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from .common import BaseVariable

    class MockVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return ()

    v1 = MockVariable(source='foo')
    v2 = MockVariable(source='foo')

    assert v1 == v2
    assert v2 == v1


# Generated at 2022-06-12 20:00:59.000063
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass


# Generated at 2022-06-12 20:01:03.229102
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Variable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [('', '0')]

    assert Variable('foo.bar', ('baz', )) == Variable('foo.bar', ('baz', ))
    assert Variable('foo.bar', ('baz',)) != Variable('foo.bar', ('foobar',))

# Generated at 2022-06-12 20:01:10.270443
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global_vars = {'a':[1,2,3,4,5], 'b':{'a': 1, 'b': 2, 'c': 3, 'd': 4}}
    local_vars = {}
    # Frame is not used here
    frame = None
    # Test case 1: Attrs
    # test case 1.1: evaluate local variable
    source = 'a'
    variable = Attrs(source)
    result = variable.items(frame, normalize=False)
    assert result == [(source, '[1, 2, 3, 4, 5]')]
    # test case 1.2: evaluate global variable
    source = 'b'
    variable = Attrs(source)
    result = variable.items(frame, normalize=False)

# Generated at 2022-06-12 20:01:15.770520
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    mv = BaseVariable("a")
    mv_return_true = BaseVariable("a")
    mv_return_false = BaseVariable("b")
    assert mv == mv_return_true
    assert not (mv == mv_return_false)



# Generated at 2022-06-12 20:01:23.333286
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types
    import pdb_clone.utils
    import pdb_clone.variable
    reload(pdb_clone.utils)
    reload(pdb_clone.variable)
    main_value = 'asdf'
    exclude = ('z',)
    func = types.FunctionType(pdb_clone.utils.get_code(), {}, 'func')
    var = pdb_clone.variable.Attrs('main_value', exclude)
    result = var.items(func.__code__.co_varnames, {'main_value': main_value})

# Generated at 2022-06-12 20:01:27.798601
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a')
    v2 = BaseVariable('b')
    v3 = BaseVariable('a', exclude=('b','c'))
    v4 = BaseVariable('a')

    assert v1 != v2
    assert v1 != v3
    assert v1 == v4
    assert hash(v1) == hash(v4)

# Generated at 2022-06-12 20:01:34.440957
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class object_1(BaseVariable):
        pass
    class object_2(BaseVariable):
        pass
    base_variable_1 = BaseVariable("test_1")
    base_variable_2 = Attrs("test_2")
    base_variable_3 = Attrs("test_2")
    base_variable_4 = object_1()
    base_variable_5 = BaseVariable()
    print(base_variable_1 == base_variable_2)
    print(base_variable_2 == base_variable_3)
    print(base_variable_2 == base_variable_4)
    print(base_variable_1 == base_variable_5)


# Generated at 2022-06-12 20:01:48.261339
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from . import utils
    from .context import Context, ContextSet, Variable
    from .environment import Environment
    from .config import Config
    import inspect
    import types
    import datetime

    # Python3-specific classes
    if sys.version_info[:2] >= (3, 3):
        class test_ABCSet(BaseVariable):
            def _items(self, key, normalize=False):
                return
        class test_CodeType(BaseVariable):
            def _items(self, key, normalize=False):
                return
        class test_CoroutineType(BaseVariable):
            def _items(self, key, normalize=False):
                return
        class test_DynamicClassAttribute(BaseVariable):
            def _items(self, key, normalize=False):
                return

# Generated at 2022-06-12 20:01:54.584067
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    cls = BaseVariable
    v1 = cls("a.b.c")
    v2 = cls("a.b.c")
    v3 = cls("d.b.c")

    assert (v1 == v2)
    assert (v1 != v2)
    assert (v1 == v3)
    assert (v1 != v3)

test_BaseVariable___eq__()

# Generated at 2022-06-12 20:01:58.910614
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a', ('b', 'c'))
    assert v1 == BaseVariable('a', ('b', 'c'))
    assert v1 != BaseVariable('a', ('b', 'd'))
    assert v1 != BaseVariable('b', ('b', 'c'))
    assert v1 != BaseVariable('a', ('b', 'c', 'd'))


# Generated at 2022-06-12 20:02:04.064035
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a')
    v2 = BaseVariable('a')
    v3 = BaseVariable('a', ['b'])
    v4 = BaseVariable('a', ['c'])
    v5 = BaseVariable('a', 'b')
    v6 = BaseVariable('b', 'a')
    if v1 == v2 == v5 == v6 and v1 != v3 != v4:
        print('test_BaseVariable___eq__ passed')
        return

    print('test_BaseVariable___eq__ failed')


# Generated at 2022-06-12 20:02:12.122144
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert(Indices('a[1:2]') == Indices('a[0:10]') == Indices('a[:]'))
    assert(Indices('a') == Attrs('a'))
    assert(Indices('a') == Indices('a'))
    assert(Indices('a') == Keys('a'))
    assert(Indices('a') != Exploding('a'))
    assert(Indices('a') != Attrs('a'))
    assert(Indices('a') != Keys('a'))
    assert(Indices('a') != BaseVariable('a'))
    assert(Indices('a') != BaseVariable('a', exclude=None))
    assert(Indices('a') != BaseVariable('a', exclude=(1, )))
    assert(Attrs('a') == Attrs('a'))


# Generated at 2022-06-12 20:02:16.592378
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    # Create a new BaseVariable object
    var1 = BaseVariable("var1", [])
    var2 = BaseVariable("var2", [])
    var3 = BaseVariable("var1", [])
    if (var1 == var2 and var1 == var3 and var2 == var3):
        print("BaseVariable object created successfully")
    else:
        print("Something wrong with creating BaseVariable object")


# Generated at 2022-06-12 20:02:18.802041
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable("x")
    var2 = BaseVariable("x")
    var3 = BaseVariable("y")

    assert var == var2
    assert var != var3


# Generated at 2022-06-12 20:02:21.251736
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1=BaseVariable('a')
    v2=BaseVariable('b')
    print(v1==v2)
    
    

# Generated at 2022-06-12 20:02:27.831489
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable = BaseVariable('a')
    variable2 = BaseVariable('a')
    variable2 = BaseVariable('b')
    assert variable == variable2, 'Expected variable == variable2'
    variable3 = BaseVariable('a', 'b')
    assert variable == variable3, 'Expected variable == variable3'
    variable4 = BaseVariable('a', 'c')
    assert variable.__eq__(variable4) is False, 'Expected variable.__eq__(variable4) to be false'


# Generated at 2022-06-12 20:02:35.844553
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v_0 = BaseVariable(source='source',exclude=(None, ))
    v_1 = BaseVariable(source='source',exclude=(None, ))
    v_2 = BaseVariable(source='source',exclude=(1, ))
    v_3 = Keys(source='source',exclude=(None, ))
    assert v_0 == v_1
    assert v_0 != v_2
    assert v_0 != v_3
    assert v_1 != v_2
    assert v_1 != v_3
    assert v_2 != v_3


# Generated at 2022-06-12 20:02:53.000145
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import builtins
    frame = inspect.currentframe()
    print(frame.f_globals)
    #getattr(builtins, __name__)
    var = BaseVariable("a")
    var_items = var.items(frame)
    print(var_items)

test_BaseVariable_items()

# Generated at 2022-06-12 20:03:02.357191
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    frame = sys._getframe()
    local_variable = BaseVariable('local_variable', exclude = ('a', 'b'))
    print(local_variable.items(frame))
    assert local_variable.items(frame) == [('local_variable', '"Pretty"')]
    local_list = BaseVariable('local_list', exclude = ('a', 'b'))
    print(local_list.items(frame))
    assert local_list.items(frame) == [('local_list', '[0, 1, 2, 3]')]
    local_dict = BaseVariable('local_dict', exclude = ('a', 'b'))
    print(local_dict.items(frame))

# Generated at 2022-06-12 20:03:04.154539
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a')
    var2 = BaseVariable('a')
    assert var1 == var2


# Generated at 2022-06-12 20:03:05.833831
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a', exclude='b')
    var2 = BaseVariable('a', exclude='b')

    assert var1 == var2
    assert var2 == var1


# Generated at 2022-06-12 20:03:09.204395
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('x', 'y')
    variable2 = BaseVariable('x', 'y')
    variable3 = BaseVariable('x', 'z')
    variable4 = Attrs('x', 'z')
    variable5 = Attrs('y', 'z')

    assert variable1 == variable2
    assert variable1 == variable1
    assert variable2 == variable2
    assert variable1 != variable3
    assert variable1 != variable4
    assert variable1 != variable5

# Generated at 2022-06-12 20:03:12.661496
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # new a object of class BaseVariable
    v = BaseVariable("{}")
    # raise NotImplementedError
    try:
        v.items(frame=None, normalize=True)
    except NotImplementedError as e:
        print("type(e): ", type(e))
        print("e: ", e)
    except Exception as e:
        print("type(e): ", type(e))
        print("e: ", e)
    # call _items to see if exception will be raised
    try:
        v._items("exception")
    except Exception as e:
        print("type(e): ", type(e))
        print("e: ", e)


# Generated at 2022-06-12 20:03:15.298241
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert not (BaseVariable('a') == BaseVariable('b'))
    assert not (BaseVariable('a') == 'a')
# Test passed


# Generated at 2022-06-12 20:03:25.218185
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert (BaseVariable('a') == BaseVariable('a'))
    assert (BaseVariable('a') == BaseVariable('a', ('b', 'c')))
    assert (BaseVariable('a', ('b', 'c')) == BaseVariable('a'))
    assert (BaseVariable('a', ('b', 'c')) == BaseVariable('a', ('b', 'c')))
    assert (BaseVariable('a', ('b', 'c')) == BaseVariable('a', ('c', 'b')))
    assert (BaseVariable('a') != BaseVariable('b'))
    assert (BaseVariable('a') != BaseVariable('a', ()))
    assert (BaseVariable('a') != BaseVariable('a', ('b')))
    assert (BaseVariable('a') != BaseVariable('a', ('c')))

# Generated at 2022-06-12 20:03:31.400375
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    result = BaseVariable('a') == BaseVariable('a')
    assert result == True

    result = BaseVariable('a') == BaseVariable('b')
    assert result == False

    result = BaseVariable('a') == BaseVariable('a', 1)
    assert result == False

    result = BaseVariable('a') == BaseVariable('a', ())
    assert result == True
    # Test by pylint
    if result == True:
        result = True
    else:
        result = True


# Generated at 2022-06-12 20:03:34.532787
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """
    Test for BaseVariable.__eq__()
   """
    # Test state of the object
    variable_ = BaseVar()
    variable_.__eq__(BaseVar())
    variable_.__eq__('1')
    variable_.__eq__(None)



# Generated at 2022-06-12 20:04:09.583264
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    with pytest.raises(NotImplementedError):
        BaseVariable('a').items('a')

# Generated at 2022-06-12 20:04:20.410679
# Unit test for method __eq__ of class BaseVariable

# Generated at 2022-06-12 20:04:28.871032
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test when method eval throws exception
    def test_exception():
        frame = SimpleNamespace(f_locals={})
        variable = BaseVariable('a')
        assert variable.items(frame, normalize=True) == ()

    test_exception()

    # Test normal cases
    frame = SimpleNamespace(f_locals={'a': 'a'})
    variable = BaseVariable('a')
    assert variable.items(frame, normalize=True) == [('a', '"a"')]

    frame = SimpleNamespace(f_locals={'a': {'a': 'a'}})
    variable = BaseVariable('a')
    assert variable.items(frame, normalize=True) == [('a', "{'a': 'a'}")]


# Generated at 2022-06-12 20:04:33.671972
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_normalize():
        assert [('self.a', '1'), ('self.b', '2')] == self.BaseVariable.items(self, normalize=True)

    frame = None
    class self(object):
        a = 1
        b = 2

    self.BaseVariable = BaseVariable('self', exclude=('a'))
    assert [('self', 'self'), ('self.b', '2')] == self.BaseVariable.items(frame)
    test_normalize()

    self.BaseVariable = Keys('self')
    assert [('self[1]', '2'), ('self[2]', 'a')] == self.BaseVariable.items(frame)
    test_normalize()

    self.BaseVariable = Keys('self.args')
    assert [('self.args[1]', '2')]

# Generated at 2022-06-12 20:04:42.772721
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a')
    assert var1.__eq__(var1) is True
    assert var1.__eq__(BaseVariable('a')) is True
    assert var1.__eq__(BaseVariable('b')) is False
    assert var1.__eq__(BaseVariable('a', exclude=['a'])) is False
    assert var1.__eq__(BaseVariable('a', exclude='a')) is False
    assert var1.__eq__('a') is False
    var1_1 = BaseVariable('a')
    assert var1.__eq__(var1_1) is True
    assert var1_1.__eq__(var1) is True

# Generated at 2022-06-12 20:04:46.481181
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    test_list = ['value1', 'value2']
    test_obj = BaseVariable(self.source)
    test_obj.items(self, test_dict)



# Generated at 2022-06-12 20:04:54.324077
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BaseVariable(source='var', exclude=())
    BaseVariable(source='var', exclude=())
    BaseVariable(source='var1', exclude=('a','b','c'))
    BaseVariable(source='var1', exclude=('a','b','c'))
    BaseVariable(source='var1', exclude=('c','b','a'))
    BaseVariable(source='var1', exclude=('b','c','a'))
    BaseVariable(source='var1', exclude=('a','b','c','d'))
    BaseVariable(source='var2', exclude=('a','b','c'))
    BaseVariable(source='var1', exclude=('e',))



# Generated at 2022-06-12 20:05:00.100756
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def get_methods(cls, name):
        methods = []
        for cls in cls.__mro__:
            if name in cls.__dict__:
                methods.append(cls.__dict__[name])
        return methods

    def check_eq(cls, cls2, name='__eq__'):
        m1 = get_methods(cls, name)
        m2 = get_methods(cls2, name)
        if m1 == m2:
            print('PASS')
        else:
            print('FAIL:', m1, m2)
    check_eq(BaseVariable, BaseVariable)
    check_eq(CommonVariable, CommonVariable)
    check_eq(CommonVariable, Attrs)
    check_eq(Attrs, Attrs)
    check_

# Generated at 2022-06-12 20:05:08.554291
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import MockFrame, MockSymbolTable
    import pudb

    # Define a very simple function for testing
    def test_function():
        my_variable = 1
        nested_variable = {
            'thing1': 'value1',
            'thing2': 'value2',
        }
        # Create a mock frame for testing
        frame = MockFrame()
        frame.f_globals = MockSymbolTable({'test_function': test_function})
        frame.f_locals = MockSymbolTable({
            'my_variable': my_variable,
            'nested_variable': nested_variable,
            'excluded_variable': {},
            'excluded_thing': 'value'
        })

        # Test with the variable 'my_variable'
        variable = BaseVariable('my_variable')
       

# Generated at 2022-06-12 20:05:13.622975
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', exclude=['b']) != BaseVariable('a', exclude=['c'])
    assert BaseVariable('a', exclude=['b', 'c']) == BaseVariable('a', exclude=['c', 'b'])



# Generated at 2022-06-12 20:05:57.605115
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    print('test_BaseVariable___eq__')

    source = 'frame.f_locals'

    A = Keys(source)
    B = Keys(source)
    C = Keys('frame.f_globals')
    D = Keys('frame.f_locals', exclude=('frame',))
    E = Attrs(source)

    assert A == B
    assert A != C
    assert A != D
    assert A != E

# Generated at 2022-06-12 20:06:01.606229
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = BaseVariable(source='foo', exclude='bar')
    a2 = BaseVariable(source='foo', exclude='baz')
    a3 = BaseVariable(source='moo', exclude='bar')
    a4 = BaseVariable(source='moo', exclude='baz')
    a5 = BaseVariable(source='foo', exclude='bar')
    assert a1 == a1
    assert a1 == a5
    assert a2 == a2
    assert a3 == a3
    assert a4 == a4

    assert a1 != a2
    assert a1 != a3
    assert a1 != a4
    assert a2 != a3
    assert a2 != a4
    assert a3 != a4

test_BaseVariable___eq__()

# Generated at 2022-06-12 20:06:07.998956
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_frame
    from .valuetrace import ValueTrace
    my_frame_joe = get_frame('my_frame_joe')
    my_frame_joe_locals = my_frame_joe.f_locals
    # -------------------------Test for variable "var_dict"
    variable = BaseVariable("var_dict")
    variable_items = variable.items(my_frame_joe)
    variable_items_correct = [('var_dict', "{'s': 'Hello, world!'}")]
    assert variable_items == variable_items_correct
    # -------------------------Test for variable "var_dict_key_s"
    variable = BaseVariable("var_dict['s']")
    variable_items = variable.items(my_frame_joe)
    variable_items_correct

# Generated at 2022-06-12 20:06:10.880801
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable(source = 'a1')
    b = BaseVariable(source = 'a2')

    assert(a == BaseVariable(source = 'a1'))
    assert(a != b)
    assert(b == BaseVariable(source = 'a2'))


# Generated at 2022-06-12 20:06:14.780745
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = 0
    class a(BaseVariable):
        def items(self, frame, normalize=False):
            return self._items(main_value, normalize)
    a = a(source='', exclude=())
    a.code = 0
    main_value = 0
    a._items(main_value, normalize)
    return True


# Generated at 2022-06-12 20:06:16.014391
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass



# Generated at 2022-06-12 20:06:24.416006
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable('source', exclude='exclude')
    def __eq__(other):
        return var.__eq__(other)

    # Equals to itself
    assert __eq__(var)

    # Equals to an object which has exactly the same values of its members
    assert __eq__(BaseVariable('source', exclude='exclude'))

    # Not equals to a variable which has different values of its members
    assert not __eq__(BaseVariable('different_source', 'different_exclude'))
    assert not __eq__(BaseVariable('source', 'different_exclude'))
    assert not __eq__(BaseVariable('different_source', exclude='exclude'))

    # Not equals to a variable which has more members
    assert not __eq__(BaseVariable('source', exclude='exclude', more_member='more'))

# Generated at 2022-06-12 20:06:34.196512
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import debugger

    def func():
        args = (1, 2)
        a = 1
        b = 2
        _test_variable_source = {'args[0]': args[0],
                                 'args[1]': args[1],
                                 'a': a,
                                 'b': b}
        # print(args, type(args), range(len(args)))

        with debugger.Tracer() as db:
            db.set_trace()

    # Set variables that are used in method items of class BaseVariable
    variable_source = 'args'
    variable_exclude = ()
    variable = Keys(variable_source, variable_exclude)

    # Call method items of class BaseVariable
    frame, frame_args = debugger.get_frame_args(func, frame_index=1)

# Generated at 2022-06-12 20:06:40.679159
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def check(v):
        assert v == v
        assert v == deepcopy(v)
        assert not(v != v)
        assert not(v != deepcopy(v))
    for cls in BaseVariable.__subclasses__():
        check(cls('x'))
        check(cls('x', 'y'))
        check(cls('x', 'y'))
        check(cls('x', ['y', 'z']))

# Generated at 2022-06-12 20:06:50.105808
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import numpy as np
    image = np.zeros(shape=(3, 100, 100, 3))
    image[:] = 123
    item = BaseVariable(source="image").items(frame=None, normalize=False)
    print(item)
    # [('image', 'array([[[[123., 123., 123.],\n        '
    #          '[123., 123., 123.],\n        '
    #          '[123., 123., 123.], ...,\n        '
    #          '[123., 123., 123.],\n        '
    #          '[123., 123., 123.],\n        '
    #          '[123., 123., 123.]],\n\n       ...,\n\n       [[123., '
    #          '123., 123.],\n        [123., 123., 123.],\

# Generated at 2022-06-12 20:08:17.674909
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .base import BaseVariable
    import inspect
    import re
    '''
    test_res = []
    frame = inspect.stack()[1]
    var = BaseVariable('str')
    var_items = var.items(frame)
    res = re.compile(r'str')
    for g in var_items:
        if res.match(g[0]):
            test_res.append(g[0])
    assert test_res == ['str'], test_res
    '''

# Generated at 2022-06-12 20:08:24.704987
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    # Get the function 'test_BaseVariable_items'
    test_func = frame.f_back
    assert(test_func.f_code.co_name == 'test_BaseVariable_items')
    # Get the global variables of the function
    global_vars = test_func.f_globals
    # Get the local variables of the function
    local_vars = test_func.f_locals
    local_vars = {'__builtins__': None, 'inspect': inspect, 'frame': frame, 'test_func': test_func, 'global_vars': global_vars, 'local_vars': local_vars}
    # Create an object 'exploding'
    exploding = Exploding('exploding')
    # Create an object 'keys'

# Generated at 2022-06-12 20:08:31.623747
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    # An exception is expected at items of the object which is not a Mapping nor Sequence and AttributeError
    class A:
        def __init__(self):
            self.a = 1
            self.b = 2

    class B:
        def __init__(self):
            self.a = 1
            self.key = '2'

    class C:
        pass

    a = A()
    b = B()
    c = C()

    print(Keys('a').items(a))
    print(Indices('a').items(a))
    print(Attrs('a').items(a))
    print(Exploding('a').items(a))

    print(Keys('b').items(b))
    print(Indices('b').items(b))
    print(Attrs('b').items(b))
    print

# Generated at 2022-06-12 20:08:41.792354
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import pytest
    from . import pycompat
    from .compat import PY2

    class A(BaseVariable):
        def _items(self, key, normalize=False):
            raise NotImplementedError

    class B(object):
        pass

    a = A('A')
    a2 = A('A')
    b = A('B')
    aa = A('A', ('a', 'b'))
    aa2 = A('A', ('b', 'a'))
    aa3 = A('A', ('a', 'b', 1))
    aaa = A('A', ('a', 'b', 1))
    bb = A('B', ('a', 'b'))
    aa_exclude = aa.exclude
    aa.exclude = ('a', 'b')