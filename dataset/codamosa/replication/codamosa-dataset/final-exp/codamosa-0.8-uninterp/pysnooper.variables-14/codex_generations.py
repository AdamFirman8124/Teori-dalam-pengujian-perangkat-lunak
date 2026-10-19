

# Generated at 2022-06-12 19:58:52.997838
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    #t = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14}
    #a = {'x': 5, 'y': 11}
    #b = [1, 3, 5, 7, 9, 11]
    #c = (1, 2, 3, 4, 5, 6)
    #d = 'abcdef'
    #e = {'v': {'abc': 'def'}}
    #f = [{'v': {'abc': 'def'}}]
    #g = {'x': 5, 'y': 11, 'z': [{'v': {'abc': 'def'}}]}
    print(Indices('').items('abcdef'))
    print(Indices('')[::-1].items('abcdef'))

# Generated at 2022-06-12 19:58:58.073132
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('x').items(frame) == []
    assert BaseVariable('x', exclude=('a', 'f')).items(frame) == [('x', '42'), ('x.b', '42.b'), ('x.c', '42.c'), ('x.d', '42.d'), ('x.e', '42.e')]


# Generated at 2022-06-12 19:59:00.343143
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    indices = Indices('xx', exclude=['xxx'])
    print(indices._slice)
    indices2 = indices[1:]
    print(indices2._slice)
    assert indices._slice == slice(None)
    assert indices2._slice == slice(1,None)


# Generated at 2022-06-12 19:59:10.652907
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # validate the truth of the following
    assert BaseVariable('x') == BaseVariable('x')
    # validate the truth of the following
    assert BaseVariable('x', 'y') == BaseVariable('x', 'y')
    # validate the truth of the following
    assert BaseVariable('x', ['y']) == BaseVariable('x', 'y')
    # validate the falsity of the following
    assert BaseVariable('x') != BaseVariable('y')
    # validate the falsity of the following
    assert BaseVariable('x') != BaseVariable('x', ['y'])
    # validate the falsity of the following
    assert BaseVariable('x', 'y') != BaseVariable('x', 'z')
    # validate the falsity of the following
    assert BaseVariable('x', 'y') != BaseVariable('x', ['y', 'z'])
   

# Generated at 2022-06-12 19:59:22.305076
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from . import pycompat
    from . import utils

    class MockVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [(self.source, None)]
    assert len(Indices(MockVariable('source_name')[4:])._items({0: '', 1: '', 2: '', 3: ''})) == 1
    assert len(Indices(MockVariable('source_name')[:])._items({0: '', 1: '', 2: '', 3: ''})) == 5
    assert len(Indices(MockVariable('source_name')[:6])._items({0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: ''})) == 7

# Generated at 2022-06-12 19:59:26.832762
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    obj1 = Indices('argv')
    assert obj1._slice == slice(None)

    obj2 = obj1[:]
    assert obj2._slice == slice(None)

    obj3 = obj1[1:2]
    assert obj3._slice == slice(1,2)

    obj4 = obj1[1::-1]
    assert obj4._slice == slice(1,None,-1)



# Generated at 2022-06-12 19:59:35.956203
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    # Method __eq__ should return a boolean.
    # It should return True if and only if
    # the other variable is of the same class
    # and has the same source and exclude attributes.
    
    variable1 = Attrs('a')
    variable2 = Attrs('b')
    variable3 = Attrs('a')
    variable4 = Attrs('a', exclude='b')
    variable5 = Keys('a')

    assert variable1 == variable3
    assert variable3 == variable1
    assert variable1 != variable2
    assert variable2 != variable1
    assert variable1 != variable4
    assert variable4 != variable1
    assert variable1 != variable5
    assert variable5 != variable1



# Generated at 2022-06-12 19:59:42.595783
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BV_list = []
    BV_list.append(BaseVariable("a"))
    BV_list.append(BaseVariable("b"))
    BV_list.append(BaseVariable("a"))
    BV_list.append(BaseVariable("c"))
    BV_list.append(BaseVariable("a"))

    for i in range(len(BV_list)-1):
        assert not BV_list[i].__eq__(BV_list[i+1]), "It is wrong !!"

if __name__ == "__main__":
    test_BaseVariable___eq__()

# Generated at 2022-06-12 19:59:47.304191
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable('a')
    assert v.items({'a':1}) == (('a', '1'),)
    assert v.items({'a':1, 'b':2}) == (('a', '1'),)


# Generated at 2022-06-12 19:59:51.351773
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    test_input = range(10)
    test_case = Indices('x')
    test_case[2:5]
    expect_result = [(u'x[2]', u'2'),(u'x[3]', u'3'),(u'x[4]', u'4')]
    assert test_case._items(test_input) == expect_result


# Generated at 2022-06-12 20:00:01.975718
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var = BaseVariable('source', exclude=('foo', 'bar'))
    var_eq = BaseVariable('source', exclude=('foo', 'bar'))
    var_diff = BaseVariable('source', exclude=('other', 'bar'))

    assert var == var_eq
    assert var != var_diff


# Generated at 2022-06-12 20:00:10.382301
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('a', ['b'])
    variable2 = BaseVariable('a', ['b'])
    variable3 = BaseVariable('a', ['c'])
    variable4 = BaseVariable('b', ['c'])
    variable5 = BaseVariable('<built-in function id>', ['c'])
    variable6 = BaseVariable('<built-in function id>', ['c'])
    variable7 = BaseVariable('<built-in function id>', ['d'])
    assert variable1 == variable2
    assert variable1 != variable3
    assert variable1 != variable4
    assert variable1 != variable5
    assert variable5 == variable6
    assert variable5 != variable7


# Generated at 2022-06-12 20:00:19.721675
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source1 = '10'
    source2 = 'x'
    source3 = 'x * y'
    source4 = 'x * y * z'
    source5 = 'x * z'

    exclude1 = ('a', 'b')
    exclude2 = ('a', 'c')
    exclude3 = ('x',)
    exclude4 = ('a')

    variables = [
        Keys(source1, exclude1),
        Keys(source1, exclude1),
        Keys(source2, exclude1),
        Keys(source2, exclude2),
        Keys(source3, exclude3),
        Keys(source3, exclude3),
        Keys(source4, exclude3),
        Keys(source4, exclude4),
        Keys(source5, exclude4),
        Keys(source5, exclude4),
    ]

    assert_vari

# Generated at 2022-06-12 20:00:28.957700
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = Exploding('')
    b = Attrs('')
    c = Attrs('', '')
    d = Attrs('b')
    e = Attrs('b', '')
    f = Attrs('b', 'a')
    g = Attrs('b', 'b')

    assert a != b, 'a != b'  # type(a)!=type(b)
    assert b == c, 'b == c'
    assert b != d, 'b != d'  # source不同
    assert d == e, 'd == e'
    assert d != f, 'd != f'  # exclude不同
    assert f == g, 'f == g'

# Generated at 2022-06-12 20:00:37.567805
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('var', ('a', 'b'))
    variable2 = BaseVariable('var', ('a', 'b'))
    variable3 = BaseVariable('var', ('a', 'b', 'c'))
    variable4 = BaseVariable('var', 'a')
    variable5 = BaseVariable('var', 'b')

    # Reflexivity property
    assert variable1 == variable1

    # Symmetric property
    assert variable1 == variable2
    assert variable2 == variable1

    # Transitive property
    assert variable1 == variable2
    assert variable2 == variable4
    assert variable4 == variable1

    # Consistency property
    assert variable1 == variable2
    assert variable2 == variable2

    assert variable1 == variable2
    assert variable2 != variable3
    assert variable3 != variable4
    assert variable4

# Generated at 2022-06-12 20:00:45.003634
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Test 1 of 2
    a = BaseVariable('a.b')
    assert a == a
    a2 = BaseVariable('a.b')
    assert a == a2
    b = BaseVariable('a.c')
    assert a != b

    # Test 2 of 2
    a = BaseVariable('a.b')
    assert a == a
    a3 = BaseVariable('a.b')
    assert a == a3
    b = BaseVariable('a.c')
    assert a != b

# Generated at 2022-06-12 20:00:48.858950
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Assert that two BaseVariables with the same source are equal
    source = "1 + 1"
    a = BaseVariable(source)
    b = BaseVariable(source)
    assert(a == b)
    assert(not (a != b))



# Generated at 2022-06-12 20:01:00.134900
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
	v1 = Indices('foo')
	v2 = Keys('foo')
	v3 = Attrs('foo')
	d1 = {}
	d2 = {'foo': 123, 'bar': 456}
	d3 = {'foo': 123, 'bar': 456, 'baz': 789}
	d4 = {'bar': 456}
	#test case1
	print('Test case:', inspect.stack()[0][3])
	print('v1:', v1)
	print('v2:', v2)
	print('Return:', v1 == v2)
	print()
	#test case2
	print('Test case:', inspect.stack()[0][3])
	print('v1:', v1)
	print('v3:', v3)

# Generated at 2022-06-12 20:01:07.540511
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    input_parameter1=[{'source': 'var', 'exclude': (), 'code': 'var', 'unambiguous_source': 'var'},{'source': 'var', 'exclude': (), 'code': None, 'unambiguous_source': 'var'}]
    output_parameter1=[True, False]

    input_parameter2=[{'source': 'var', 'exclude': (), 'code': 'var', 'unambiguous_source': 'var'},{'source': 'var', 'exclude': (), 'code': 'var', 'unambiguous_source': 'var'}]
    output_parameter2=[True, True]


# Generated at 2022-06-12 20:01:09.194372
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variable = BaseVariable('a')
    variable.items()
    variable._items()

# Generated at 2022-06-12 20:01:17.972368
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = Attrs('1')
    v2 = Attrs('2')
    assert v1 != v2
    v3 = Attrs('1', ('a',))
    v4 = Attrs('1', ('b',))
    assert v3 != v4
    v5 = Attrs('1', ('a',))
    v6 = Attrs('1', ('a',))
    assert v5 == v6
    v7 = Attrs('1', ('a',))
    v8 = Attrs('1', ('a'))
    assert v7 == v8

# Generated at 2022-06-12 20:01:22.440781
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BaseVariable(source="dict", exclude=[]) == BaseVariable(source="dict", exclude=[])
    # verification of not equal class
    BaseVariable(source="dict", exclude=[]) != 1


# Generated at 2022-06-12 20:01:28.118040
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    v1 = BaseVariable(source = 'a', exclude = ())
    v2 = BaseVariable(source = 'a', exclude = ())
    v3 = BaseVariable(source = 'b', exclude = ())
    v4 = CommonVariable(source = 'a', exclude = ())

    assert v1.__eq__(v2)
    assert not v1.__eq__(v3)
    assert not v1.__eq__(v4)

# Generated at 2022-06-12 20:01:33.090098
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Test positive case
    assert BaseVariable('x.y') == BaseVariable('x.y')
    # Test negative case
    assert BaseVariable('x.y') != BaseVariable('x.z')
    assert BaseVariable('x.y') != BaseVariable('x["y"]')
    assert BaseVariable('x.y') != BaseVariable('x[y]')
    assert BaseVariable('x.y') != BaseVariable('x.y', exclude=('x',))


# Generated at 2022-06-12 20:01:43.618117
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class a(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass
    class b(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass
    class c(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass
    class d(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass

    # each class
    assert a('x') == a('x')
    assert b('x') == b('x')
    assert c('x') == c('x')
    assert d('x') == d('x')
    assert a('x') != b('x')
    assert b('x') != c('x')

# Generated at 2022-06-12 20:01:45.850845
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('a')
    c = BaseVariable('b')
    assert a == b
    assert a == a
    assert b == a
    assert b == b
    assert a != c
    assert a != object()


# Generated at 2022-06-12 20:01:55.919014
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Module:
        x = 3

    def test(source, expected):
        variable = BaseVariable(source)
        frame = inspect.currentframe()
        assert variable.items(frame) == expected
        frame = inspect.stack()[1][0]
        assert variable.items(frame) == expected

    def test_error(source, expected_type):
        variable = BaseVariable(source)
        frame = inspect.currentframe()
        try:
            variable.items(frame)
        except Exception as e:
            assert type(e) is expected_type
        else:
            assert False

    test('3', [('3', '3')])
    test('Module', [(
        'Module',
        '<module \'honeydew.variables\' from \'{}\'>'.format(__file__)
    )])
    test

# Generated at 2022-06-12 20:01:58.758701
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = Keys('a', ['b', 'c'])
    v2 = Keys('a', ('b', 'c'))
    assert v1 == v2



# Generated at 2022-06-12 20:02:01.687145
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # assert 1 == '1'
    # assert 1 == str(1)
    assert '1' == '1'
    assert 1 != str(1)
    # assert str(1) == str(1)
    assert '1' != 1
    assert str(1) != 1

# Generated at 2022-06-12 20:02:09.034668
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', exclude=['b']) == BaseVariable('a', exclude=['b'])
    assert BaseVariable('a', exclude=['b']) != BaseVariable('a', exclude=['c'])
    assert BaseVariable('a') != Attrs('a')
    assert BaseVariable('a') != Keys('a')
    assert BaseVariable('a') != Indices('a')
    assert BaseVariable('a') != Exploding('a')

# Generated at 2022-06-12 20:02:21.467049
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')
    assert BaseVariable('a', 'b') != BaseVariable('a')
    assert BaseVariable('a') != Attrs('a')
    assert Attrs('a') == Attrs('a')
    assert Attrs('a') != Attrs('b')
    assert Attrs('a', 'b') == Attrs('a', 'b')
    assert Attrs('a', 'b') != Attrs('a', 'c')
    assert Attrs('a', 'b') != Attrs('a')
    assert Attrs('a') != Indices('a')
   

# Generated at 2022-06-12 20:02:26.076311
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('x',exclude=())
    var2 = BaseVariable('x',exclude=())
    var3 = BaseVariable('y',exclude=())
    assert var1 == var2
    assert not var1 == var3
    assert var1 != var3


# Generated at 2022-06-12 20:02:34.602419
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import pytest
    import pdb_clone.variable as variable
    import pdb_clone.utils as utils

    class FakeFrame:
        def __init__(self, f_globals, f_locals):
            self.f_globals = f_globals
            self.f_locals = f_locals

    # Mock object returned by get_shortish_repr(...)
    class FakeShortishRepr:
        def __init__(self, repr_value, limit_length_value):
            self._repr = repr_value
            self._limit_length_value = limit_length_value

        def repr(self, repr_value, limit_length_value):
            return self._repr

        def limit_length_value(self, limit_length_value):
            return self

# Generated at 2022-06-12 20:02:39.736047
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = Attrs('hello', 'world')
    var2 = Attrs('hello', 'world')
    var3 = Attrs('hello')
    var4 = Keys('hello')
    assert var1 == var2
    assert var1 != var3
    assert var1 != var4
    assert var1 != 'hello'

# Generated at 2022-06-12 20:02:47.795132
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Create an instance of Keys variable with source 'm'
    v = Keys('m')
    # Create a fake frame with the variable m
    frame = type('frame', (object,), {'f_locals': {'m': {'a': 1}}})()
    # Check if we get a tuple with one pair
    assert v.items(frame) == (('m[a]', '1'),)
    # Update the frame to have one more key-value pair in the dict
    frame.f_locals['m'].update({'b': 2.0})
    # Check if we get a tuple with two pairs
    assert v.items(frame) == (('m[a]', '1'), ('m[b]', '2.0'))



# Generated at 2022-06-12 20:02:55.752224
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def generate_function(function_name, source, exclude, local_var_name, local_var_value, expected):
        locals_code = """
        {} = {}
        """.format(local_var_name, local_var_value)
        variable_code = """
        from __main__ import BaseVariable

        class {function_name}(BaseVariable):
            def _items(self, key, normalize=False):
                pass
        """.format(function_name=function_name)
        test_code = """
        from __main__ import {}
        assert {}.items(frame) == {}
        """.format(function_name, function_name, expected)
        code_to_run = locals_code + variable_code + test_code

        print(code_to_run)

# Generated at 2022-06-12 20:03:04.972620
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = {'a': 1, 'b':2, 'c':{'c1':3, 'c2':4}}
    assert Attrs('a').items(frame) == [('a', '1')]
    assert Attrs('c.c1').items(frame) == [('c.c1', '3')]
    assert Attrs('c.c1.c2').items(frame) == [('c.c1.c2', '<attribute not found>')]
    assert Keys('c').items(frame) == [('c', "<class 'dict'>"), ('c[c1]', '3'), ('c[c2]', '4')]

# Generated at 2022-06-12 20:03:09.285487
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def test_ok():
        assert a == b
        assert not(a != b)
        assert not(a == c)
        assert a != c

    a = BaseVariable('a')
    b = BaseVariable('a')
    c = BaseVariable('c')

    test_ok()
    a.source = 'b'
    b.source = 'b'
    test_ok()
    a.exclude = c.exclude = ['d']
    test_ok()
    c.exclude = ['e']
    test_ok()
    c.source = 'd'
    test_ok()

# Generated at 2022-06-12 20:03:18.818628
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import Frame
    from . import FrameSummary
    from . import ThreadSummary

    f1 = Frame(None, None, None, None)
    f2 = Frame(None, None, None, None)
    thread_summary = ThreadSummary(None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    fs = FrameSummary(f1, f2, thread_summary)
    class test_class(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __str__(self):
            return "test_class"
        __repr__ = __str__
    test_class1 = test_class(1, 2)
    test_class2 = test_class(3, 4)
    test

# Generated at 2022-06-12 20:03:19.452539
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass


# Generated at 2022-06-12 20:03:33.128493
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame=FakeFrame()
    frame.f_locals["a"] = {'a':1, 'b':2 }
    frame.f_locals["a"]["c"] = frame.f_locals["a"]
    import sys
    frame.f_globals = sys._getframe(0).f_globals
    print(frame.f_locals["a"])
    print('---')
    BaseVariable('a').items(frame)
    print('---')
    BaseVariable('a.b').items(frame)
    print('---')
    BaseVariable('a.c').items(frame)
    print('---')
    BaseVariable('a', 'b').items(frame)
    print('---')
    BaseVariable('a.c', 'b').items(frame)
    print('---')
   

# Generated at 2022-06-12 20:03:35.826415
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs('a') != Attrs('b')
    assert Attrs('a') == Attrs('a')
    assert Attrs('a') != Keys('a')
    assert Attrs('a') != Indices('a')

# Generated at 2022-06-12 20:03:46.433707
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    print(BaseVariable('a', None) == BaseVariable('a', None))
    print(BaseVariable('a', None) == BaseVariable('b', None))
    print(BaseVariable('a', None) == BaseVariable('a', 'b'))
    print(BaseVariable('a', None) == BaseVariable('a', 'c'))
    print(BaseVariable('a', None) == BaseVariable('a', 'b', 'c'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'c'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b', 'c'))

# Generated at 2022-06-12 20:03:56.701902
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    import types
    from . import utils

    def get_globals(func):
        assert inspect.isfunction(func)
        return func.__globals__

    def get_locals(frame):
        assert isinstance(frame, types.FrameType)
        return frame.f_locals

    class Test:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __repr__(self):
            return 'Test({}, {})'.format(self.a, self.b)

    frame = sys._getframe()
    test = Test('a', 'b')

    print(get_globals(test_BaseVariable_items))
    print(get_locals(frame))

    # Common test case
   

# Generated at 2022-06-12 20:03:59.431115
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('var')
    var2 = BaseVariable('var')
    var3 = BaseVariable('var', exclude='self')

    assert var1 == var2
    assert var1 != var3
    assert var2 != var3


# Generated at 2022-06-12 20:04:08.281526
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def _test_BaseVariable___eq__(expected, a, b):
        assert expected == (a == b)

    _test_BaseVariable___eq__(True,
                              BaseVariable('a'), BaseVariable('a'))
    _test_BaseVariable___eq__(False,
                              BaseVariable('a'), BaseVariable('b'))
    _test_BaseVariable___eq__(False,
                              Attrs('a'), BaseVariable('a'))
    _test_BaseVariable___eq__(True,
                              Attrs('a'), Attrs('a'))
    _test_BaseVariable___eq__(False,
                              Attrs('a'), Attrs('b'))
    _test_BaseVariable___eq__(False,
                              Attrs('a'), Keys('a'))

# Generated at 2022-06-12 20:04:18.606944
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # imports
    from _pytest.monkeypatch import MonkeyPatch

    # mocks
    class BaseVariableMock(BaseVariable):
        def __init__(self, m1, m2):
            self.m1, self.m2 = m1, m2

        def _items(self, key, normalize=False):
            raise NotImplementedError

        @property
        def _fingerprint(self):
            return (type(self), self.m1, self.m2)

    b1 = BaseVariableMock('1','1')
    b2 = BaseVariableMock('1','1')
    b3 = BaseVariableMock('2','1')

    # monkeypatching
    monkeypatch = MonkeyPatch()

    # tests
    assert b1 == b2
    assert b1 != b3

# Generated at 2022-06-12 20:04:22.683445
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('b')
    c = BaseVariable('a')
    assert a.__eq__(b) == False
    assert a.__eq__(c) == True
    assert b.__eq__(c) == False



# Generated at 2022-06-12 20:04:27.945697
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():

    from datetime import date

    v = BaseVariable('x')
    assert v == BaseVariable('x')

    assert not (v == BaseVariable('y'))
    assert not (v == BaseVariable('x', ('y',)))
    assert not (v == BaseVariable('x', ('y', 'z')))

    assert not (v == type(v)())
    assert not (v == date.today())
    assert not (v == object())

# Generated at 2022-06-12 20:04:34.698652
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def _make_var(source, exclude=()):
        var = BaseVariable(source, exclude)
        var.code = compile(source, '<variable>', 'eval')
        return var

    var = _make_var('x')
    result = var.items(utils.make_frame({'x': (1, 2, 3)}))
    assert result == {'x': (1, 2, 3)}

    # Test that exclude works for BaseVariable
    with pytest.raises(AttributeError):
        var = _make_var('x', ('foo', 'bar'))
        result = var.items(utils.make_frame({'x': {
            'foo': 0,
            'bar': 1,
            'baz': 2
        }}))



# Generated at 2022-06-12 20:04:56.691773
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    BLAH = object()
    R = object()
    T = object()
    items = lambda cls, obj, **kwargs: list(cls(**kwargs).items(get_frame(obj)))
    assert items(Attrs, BLAH, source='BLAH', exclude=['some_field']) == \
        [('BLAH', '<BLAH>'), ('BLAH.foo', '2'), ('BLAH.bar', '3'), ('BLAH.baz', "'hello'")]
    assert items(Keys, {'a': 1, 'b': 2}, source='D') == \
        [('D', '{...}'), ('D[b]', '2'), ('D[a]', '1')]

# Generated at 2022-06-12 20:05:07.276909
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .fake import Frame
    frame = Frame()
    frame.f_locals['x'] = 'x'
    assert list(BaseVariable('x').items(frame)) == [('x', '\'x\'')]
    frame.f_locals['dict_'] = dict(a=1)
    assert list(Keys('dict_').items(frame)) == [('dict_', '{...}'), ('dict_[a]', '1')]
    frame.f_locals['list_'] = [1, 2, 3]
    assert list(Indices('list_').items(frame)) == [('list_', '[...]'), ('list_[0]', '1'), ('list_[1]', '2'), ('list_[2]', '3')]

# Generated at 2022-06-12 20:05:17.464095
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:05:29.843153
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # First one
    var1 = BaseVariable('frame')
    frame = inspect.currentframe()
    assert var1.items(frame) == []
    assert var1.items(frame, normalize=True) == []

    # Second
    var2 = BaseVariable('frame', exclude=('f_locals', 'f_globals', 'f_back'))

# Generated at 2022-06-12 20:05:41.407561
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class A(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def __repr__(self):
            return "<a's repr>"

        def method(self):
            return "<a's method>"

    a = A(1, 2, 3)
    b = A(4, 5, 6)

    variables = {
        'exploding': Exploding,
        'attrs': Attrs,
        'keys': Keys,
        'indices': Indices,
    }

    def assert_items(args, expect):
        actual = []
        for name, cls in variables.items():
            v = cls(*args)
            actual.append((name, sorted(v.items(sys._getframe()))))


# Generated at 2022-06-12 20:05:44.345868
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v = BaseVariable('x')
    assert v == v
    assert v == BaseVariable('x')
    assert v == BaseVariable('y')



# Generated at 2022-06-12 20:05:54.663275
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def assert_items(expected, variable, frame, normalize=False):
        assert list(variable.items(frame, normalize)) == expected

    def test_main():
        frame = utils.create_frame('main_value', {'main_value': 123})
        assert_items([('main_value', '123')],
            BaseVariable('main_value'),
            frame
        )

    def test_exclude():
        frame = utils.create_frame('main_value', {'main_value': 123})
        assert_items([('main_value', '123')],
            BaseVariable('main_value', 'exclude'),
            frame
        )
        assert_items([],
            BaseVariable('main_value', 'main_value'),
            frame
        )

    def test_main_error():
        frame = ut

# Generated at 2022-06-12 20:05:59.035935
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # init
    source = 'a'
    exclude = ('b',)
    var1 = BaseVariable(source, exclude)
    var2 = BaseVariable(source, exclude)
    assert var1 == var2
    assert not var1.__eq__(None)
    assert not (var1 == 'source')
    assert not var1.__eq__(BaseVariable('a1', exclude))

# Generated at 2022-06-12 20:06:08.729275
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test with Attrs
    source = 'a.b'
    exclude = 'b'
    variable = Attrs(source, exclude)
    class A:
        class B:
            a = 1; b =2; c = 3
    a = A()
    frame = None
    variable.items(frame)
    assert variable.items(frame) == [('a.b', '<__main__.A.B object at 0x02FE2D50>'),
                            ('a.b.c', '3')]

    # Test with Keys
    source = 'a.b'
    exclude = 'b'
    variable = Keys(source, exclude)
    class A:
        class B:
            a = {'b':2, 'c': 3}
    a = A()
    frame = None

# Generated at 2022-06-12 20:06:12.045004
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys, os
    import doctest
    import inspect, dis
    sys.path.append(os.path.dirname(__file__))
    import test_utils
    test_utils.add_path('..')
    doctest.testmod(inspect.getmodule(dis), verbose=False, optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-12 20:06:40.431501
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from . import utils
    from . import pycompat

    import numpy as np
    nparray = np.array([1,2,3])

    # Case 1: source is a variable name
    source = 'a'
    code = pycompat.compile(source, '<variable>', 'eval')
    a = np.array([1,2,3])
    exclude = ()
    expect = [('a', utils.get_shortish_repr(a, normalize=False))]
    assert BaseVariable(source, exclude).items(code.co_varnames, code.co_filename, code.co_firstlineno).__eq__(expect)

    # Case 2: source is a dictionary
    source = '{1:1, 2:2}'
    code = pycompat

# Generated at 2022-06-12 20:06:44.640790
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    frame = inspect.currentframe().f_back
    sys.setrecursionlimit(2)
    a = ['abc'] * sys.getrecursionlimit()
    print(a)
    a[0].append(a)
    a[1] = a
    print(a)
    items = Attrs('a').items(frame)
    print(items)

# Generated at 2022-06-12 20:06:50.104693
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class SampleVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            pass
    var1 = SampleVariable('test', ('t', 'p'))
    var2 = SampleVariable('test', ('t', 'p'))
    var3 = SampleVariable('test', ('t', 's'))
    assert var1 == var2
    assert not var1 == var3



# Generated at 2022-06-12 20:06:56.812929
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame_info = inspect.exc_info()[2]
    frame = frame_info.tb_frame
    d = dict(a = 1, b = 2)
    d_var = Keys('d')
    print(d_var.items(frame))
    d_var = Indices('d')
    print(d_var.items(frame))
    d_var = Attrs('d')
    print(d_var.items(frame))
    d_var = Keys('d[1]')
    print(d_var.items(frame))
    d_var = Indices('d[1]')
    print(d_var.items(frame))
    d_var = Attrs('d[1]')
    print(d_var.items(frame))

# Generated at 2022-06-12 20:07:07.321234
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import debugpy.common.contract as tp
    import debugpy.common.frame_utils as utils
    import inspect
    import pprint
    frame = inspect.currentframe()
    main_value = {}
    main_value["key1"] = "value1"

    frame_dic = utils.frame_to_dic(frame)
    # print("frame_dic")
    # pprint.pprint(frame_dic)
    Var = Attrs("main_value")
    s = Var.items(frame_dic, normalize=False)
    # print("s")
    # pprint.pprint(s)


    # test for case return []
    Var = Attrs("main_value")
    s = Var.items(frame_dic)
    # print("s")
    # pprint

# Generated at 2022-06-12 20:07:16.330852
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from .utils import Seq2SeqList
    from .utils import first_match, Null
    
    def is_elem_in(key, value, dic):
        for item in dic:
            if item[0] == key and item[1] == value:
                return True
        return False

    #test variable_list
    variable_list = ["a", "b", "c"]  # variable_list is a list
    variable_list_1 = [1, 2, 3]  # variable_list_1 is a list
    variable_list_2 = ["a", variable_list, variable_list_1]  # variable_list_2 is a list
    variable_list_3 = ["a", variable_list, variable_list_1, variable_list_2]  # variable_list_3 is

# Generated at 2022-06-12 20:07:27.761256
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:07:36.676471
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable("name").items("asd") == []
    assert Attrs("name").items("asd") == [("name", "'asd'")]
    assert Keys("name").items("asd") == [("name", "'asd'")]
    assert Indices("name").items("asd") == [("name[0]", "'a'"), ("name[1]", "'s'"), ("name[2]", "'d'")]
    assert Attrs("name").items("asd", normalize=True) == [("name", "'a'...")]
    assert Keys("name").items("asd", normalize=True) == [("name", "'a'...")]

# Generated at 2022-06-12 20:07:44.702527
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frame
    from . import dataset
    from . import utils
    from . import exceptions

    # setup
    frame_ = frame.Frame.from_file(utils.get_test_file('test_dataset.py'))
    frame_ = frame_[frame_['fn'] == 'test_dataset']
    frame_ = frame_[frame_['ln'].isin([226, 233])]
    frame_ = frame_.set_index(['fn', 'ln', 'col_0'])
    call = frame_.loc['test_dataset', 226][0]
    locals_ = call.f_locals
    locals_['self'] = dataset.Dataset()
    locals_['self']['a'] = 3
    locals_['self']['b'] = 4

    var_test = Base

# Generated at 2022-06-12 20:07:54.721924
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import sys
    sys.path.append("..")
    from lib.Variable import BaseVariable
    # The first example
    source = "__builtins__"
    exclude = "HOHO"
    a = BaseVariable(source, exclude)
    source = "__builtins__"
    exclude = "HOHO"
    b = BaseVariable(source, exclude)
    assert a == b
    # The second example
    source = "__builtins__"
    exclude = "HOHO"
    a = BaseVariable(source, exclude)
    source = "__builtins__"
    exclude = "oHO"
    b = BaseVariable(source, exclude)
    assert a != b
    # The third example
    source = "__builtins__"
    exclude = "HOHO"