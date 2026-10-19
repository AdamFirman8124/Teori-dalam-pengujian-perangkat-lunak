

# Generated at 2022-06-12 19:58:43.627809
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 19:58:52.236469
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test module variable
    print("*** Test module variable ***")
    import mytool.variable
    bv = BaseVariable('.*', exclude=['exclude'])
    print(bv.items(mytool.variable.__dict__))

    # Test instance variable
    print("*** Test instance variable ***")
    class TestVariable:
        def __init__(self):
            self.var1 = 'var1'
            self.var2 = 'var2'
        def __str__(self):
            return '<Test Variable>'
    tv = TestVariable()
    bv = BaseVariable('tv')
    for item in bv.items(mytool.variable.__dict__):
        print(item)
    print(bv.items(mytool.variable.__dict__, normalize=True))


# Unit test

# Generated at 2022-06-12 19:59:00.413483
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a', 'b')
    var2 = BaseVariable('a', 'b')
    assert var1 == var2

    var1 = BaseVariable('a', 'b')
    var2 = BaseVariable('a', 'c')
    assert not var1 == var2

    var1 = BaseVariable('a', 'b')
    var2 = BaseVariable('b', 'b')
    assert not var1 == var2

    var1 = BaseVariable('a', 'b')
    var2 = 'a'
    assert not var1 == var2

test_BaseVariable___eq__()

# Generated at 2022-06-12 19:59:09.682410
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('source', 'exclude')
    v2 = BaseVariable('source', 'exclude')
    v3 = BaseVariable('source', 'exclude')
    assert v1 == v2
    assert v1 == v3
    attributes = [
        'source',
        'exclude',
        'code',
        'unambiguous_source'
    ]
    for i in range(len(attributes)):
        for j in range(i + 1, len(attributes)):
            assert v1 == v2
            assert v2 == v3
            setattr(v2, attributes[i], object())
            setattr(v3, attributes[j], object())


# Generated at 2022-06-12 19:59:15.037037
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    (var, var_items) = BaseVariable('a').items(frame)
    assert var == 'a'
    assert var_items == '1'
    (var, var_items) = Items('a').items(frame)
    assert var == 'a'
    assert var_items == '1'
    (var, var_items) = Keys('a').items(frame)
    assert var == 'a'
    assert var_items == '{}'
    (var, var_items) = Attrs('a').items(frame)
    assert var == 'a'
    assert var_items == 'ClassA'
    (var, var_items) = Indices('a').items(frame)
    assert var == 'a'
    assert var_items == '[]'
    (var, var_items) = Indices('a')

# Generated at 2022-06-12 19:59:18.179456
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('abc') == BaseVariable('abc')
    assert BaseVariable('abc').__eq__(BaseVariable('abd')) is False

# Generated at 2022-06-12 19:59:28.291559
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def test_variable(v1, v2, expected):
        print('compare {} to {}'.format(v1, v2))
        result = v1 == v2
        print('\t{} == {}? -> {}'.format(v1, v2, result))
        assert result == expected
        result = v2 == v1
        print('\t{} == {}? -> {}'.format(v2, v1, result))
        assert result == expected


    test_variable(Attrs('x'), Attrs('x'), True)
    test_variable(Attrs('x'), Attrs('y'), False)
    test_variable(Attrs('x', exclude=['y']), Attrs('x', exclude=['y']), True)

# Generated at 2022-06-12 19:59:38.011852
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    class A(object):
        def __init__(self):
            self.b = 1
            self.c = 2
            self.d = '3'
            self.e = sys
    a = A()
    a.A = A
    a.B = [1, 2, 3]
    a.C = {'a': 11, 'b': 22}
    a.D = (1, 2)
    # print(a)
    # print(dir(a))

# Generated at 2022-06-12 19:59:45.483720
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = sys._getframe(5)
    test_var1 = BaseVariable('frame.f_locals', exclude=['__builtins__'])
    test_var2 = BaseVariable('frame.f_locals.__builtins__', exclude=['__builtins__'])
    test_var3 = BaseVariable('frame.f_locals.__builtins__')
    test_var4 = BaseVariable('frame.f_locals.worng_var')
    assert test_var1.items(frame) == test_var1.items(frame, normalize=True)
    assert test_var2.items(frame) == test_var2.items(frame, normalize=True)
    assert test_var3.items(frame) == test_var3.items(frame, normalize=True)
    assert test_var

# Generated at 2022-06-12 19:59:47.629423
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = 'a'
    frame = {'a': 1}
    frame_globals = frame.copy()
    frame_locals = frame.copy()
    exclude = ()

    test_case = BaseVariable(source, exclude)
    result = test_case.items(frame, normalize=False)
    expected = [('a', '1')]

    assert result == expected



# Generated at 2022-06-12 20:00:00.778873
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Create a list of dictionaries
    dict1 = dict(a=1, b=2)
    dict2 = dict(a=1, b=dict(c=3, d=4))
    dict3 = dict(a=1, b=dict(c=3, d=dict(e=5, f=6)))
    dict_list = [dict1, dict2, dict3]
    
    # Create a list of strings
    string1 = "a = 1, b = 2"
    string2 = "a = 1, b = c = 3, d = 4"
    string3 = "a = 1, b = c = 3, d = e = 5, f = 6"
    string_list = [string1, string2, string3]
    
    # Use a list of strings to create a list of dicitonaries of

# Generated at 2022-06-12 20:00:06.492326
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs("json_data").__eq__(Attrs("json_data"))
    assert Attrs("json_data") != Attrs("json_data", exclude=("user",))
    assert Attrs("json_data") != Attrs("json_data", exclude=("user",), source="json_data2")
    assert Attrs("json_data", source="json_data2") != Attrs("json_data2", source="json_data")

# Generated at 2022-06-12 20:00:13.591199
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class DummyVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return []
    var1 = DummyVariable('source1', ('exclude1', 'exclude2'))
    var1_equal = DummyVariable('source1', ('exclude1', 'exclude2'))
    assert var1 == var1_equal
    assert var1.__hash__() == var1_equal.__hash__()
    var1_not_equal = DummyVariable('source2', ('exclude1', 'exclude2'))
    assert var1 != var1_not_equal
    assert var1.__hash__() != var1_not_equal.__hash__()
    assert var1 != 'var1'

# Generated at 2022-06-12 20:00:16.392569
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = Indices('cpu_count')
    import multiprocessing
    cpu_count = multiprocessing.cpu_count()
    assert len(v.items(1)) == cpu_count

# Generated at 2022-06-12 20:00:22.744813
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    from . import utils
    from . import pycompat
    from . import variables
    from .variables import BaseVariable
    from .variables import CommonVariable
    from .variables import Attrs
    from .variables import Keys
    from .variables import Indices
    from .variables import Exploding
    print('\n*** test_Indices___getitem__ ***')
    print('Creating object o: attrs, keys or indices')
    o = Indices('foo')[::-1]
    print('Running method __getitem__')
    print(o)
    print('\n*** End of test_Indices___getitem__ ***')
    return


# Generated at 2022-06-12 20:00:24.452409
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    a = Indices('a')
    b = a[:2]
    c = a[:]
    
    assert(b._fingerprint == (Keys, 'a', ()))
    assert(c._fingerprint == (Keys, 'a', ()))



# Generated at 2022-06-12 20:00:34.152865
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def function_under_test():
        pass

    frame = sys._getframe()

    var_obj = BaseVariable(source='frame', exclude=())
    assert var_obj.items(frame) == [('frame', '<frame object>')]

    # Test Attrs variable
    var_obj = Attrs(source='function_under_test', exclude=('__code__',))

# Generated at 2022-06-12 20:00:36.559389
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    myIndices = Indices('myDict')
    myIndices[0:0]
    assert myIndices._slice == slice(0,0,None)

# Generated at 2022-06-12 20:00:42.012339
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    simple_variable_1 = BaseVariable('something')
    simple_variable_2 = BaseVariable('something')
    simple_variable_3 = BaseVariable('something_else')
    assert simple_variable_1 == simple_variable_2
    assert simple_variable_1 != simple_variable_3


# Generated at 2022-06-12 20:00:46.105016
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    assert a == a
    assert a != BaseVariable('b')
    assert a != BaseVariable('a', exclude='x')
    assert a != BaseVariable('a', exclude=['x'])
    assert a != object()


# Generated at 2022-06-12 20:00:58.754063
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import doctest

    local_variables = inspect.currentframe().f_locals
    docstr = BaseVariable.items.__doc__
    failures, tested = doctest.testmod(m=local_variables, name='BaseVariable', optionflags=doctest.ELLIPSIS, extraglobs={'stack': [], 'BaseVariable': BaseVariable})
    print('{}/{} tests failed in docstr of method items of class BaseVariable'.format(failures, tested))

# Generated at 2022-06-12 20:01:06.684086
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class V1(BaseVariable):
        def _items(self, key, normalize=False):
            return (key, '1')

    class V2(BaseVariable):
        def _items(self, key, normalize=False):
            return (key, '2')

    assert V1('a').items(1) == V2('a').items(1)
    assert V1('a').items(1) == V1('a').items(1)
    assert V1('a').items(1) != V2('a').items(2)
    assert V1('a').items(1) != V1('b').items(1)
    assert V1('a').items(1) != V1('a').items(2)

# Generated at 2022-06-12 20:01:13.091904
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import Frame
    from . import source
    import sys
    import math
    import builtins

    def f():
        foo = dict(a=1, b=2, c=3, d=4)
        bar = dict(a=1, b=2, c=3, d=4, e=5)
        baz = dict(a=1, b=2, c=3, d=4, e=5, f=6)
        qux = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
        quux = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)

# Generated at 2022-06-12 20:01:19.301297
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    dummy = inspect.currentframe()
    dummy.f_locals = {
        's':'hello world',
        'a':{'b':1, 'c':3},
        'l':[1,2,3]
    }
    dummy.f_globals = {}
    result = {}
    for v in [Attrs('a', 'b'), Keys('a'), Indices('l'), Exploding('a')]:
        result[str(v)] = v.items(dummy)

# Generated at 2022-06-12 20:01:30.274616
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Test(BaseVariable):
        def _items(self, main_value, normalize=False):
            return [('a', 'A'), ('b', 'B')]

    frame = utils.Frame(
        'tests/fixtures/frame_with_dict.py',
        'source_code',
        {
            'argument': 'value',
            'argument2': 'value2',
        },
        '__main__')

    assert Test('argument').items(frame) == [('argument', "'value'")]
    assert Test('argument.__class__').items(frame) == [('argument.__class__', "<type 'str'>")]

# Generated at 2022-06-12 20:01:41.366021
# Unit test for method items of class BaseVariable

# Generated at 2022-06-12 20:01:46.035340
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from importlib import import_module
    from . import sample_reporting_env

    frame = sample_reporting_env.get_sample_frame()
    frame.f_loca = 'A'
    frame.f_locb = {'B':'b'}
    def _test(variables):
        var_val = {}
        for var in variables:
            var_val[var] = var.items(frame)
        return var_val
    # test class BaseVariable

# Generated at 2022-06-12 20:01:55.139496
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = 1
    b = 2
    frame = frame_factory(a,b)
    var = BaseVariable("a")
    assert var.items(frame) == [("a",1)]
    var = BaseVariable("b")
    assert var.items(frame) == [("b",2)]
    var = BaseVariable("a*b")
    assert var.items(frame) == [("a*b",2)]
    var = BaseVariable("a*b+1")
    assert var.items(frame) == [("a*b+1",3)]
    var = BaseVariable("a*b+c")
    assert var.items(frame) == [("a*b+c",3)]

# Generated at 2022-06-12 20:02:03.786639
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global_environ = {
        'a': {'b': 'd'},
        'aaa': {'bbb': 'ddd'},
        'xyz': {'zyx': 'zyx'},
        'xyz2': {'zyx2': 'zyx2'},
        'abc': ['abc'],
        'abc2': ['abc2']
    }

    def test_f(x):
        class DummyAttr(object):
            attr1 = 'attr1'
            attr2 = 'attr2'
            attr3 = 'attr3'

        return x if x == 'e' else DummyAttr

    global_environ['test_f'] = test_f


# Generated at 2022-06-12 20:02:11.960762
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types
    import __main__
    import inspect
    from .utils import TestCase

    # Python 2.x has no MappingProxyType
    if sys.version_info < (3,):
        MappingProxyType = object
    else:
        # py2.7/types.pyc
        MappingProxyType = types.MappingProxyType
    # py2.7/types.pyc
    SimpleNamespace = types.SimpleNamespace

    class MyTestCase(TestCase):
        pass

    # Python 2.x
    if sys.version_info < (3,):
        def get_local_frame(fun):
            return inspect.getargvalues(fun.__closure__[0].cell_contents).locals
    # Python 3.x

# Generated at 2022-06-12 20:02:29.859175
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import tracemalloc
    tracemalloc.start()
    var = BaseVariable("sys")
    # test no exception while calling
    var.items({})
    tracemalloc.stop()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    for stat in top_stats:
        if stat.size > 0:
            print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
            line = stat.traceback.format()[-1]
            print("\t"+line)
    print("type of var is ",str(type(var)))

# Generated at 2022-06-12 20:02:38.901736
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import monkeytype.tracing
    frame = monkeytype.tracing.fake_frame
    import sys
    frame.f_globals = sys.modules['__main__'].__dict__
    frame.f_locals = locale.__dict__
    # test variables excluding
    my_excludes = set(['D_FMT', 'D_T_FMT'])
    test_var = Keys('locale', exclude=my_excludes)
    items = test_var.items(frame)
    assert len(items) > 0
    print(items)
    for i in items:
        assert i[0] not in my_excludes

    # test variables explode
    test_var = Exploding('locale')
    items = test_var.items(frame)
    assert len(items) > 0

# Generated at 2022-06-12 20:02:47.562137
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pytest
    # test the case that main_value is a type value
    class A:
        pass
    a = A()
    a.b = A()
    a.b.c = A()
    a.b.c.d = 'hi'

    source = 'a.b'
    v = Attrs(source)
    with pytest.raises(Exception):
        v.items(None)
    
    source = 'a.b'
    v = Attrs(source)
    result = v.items(a.__dict__)
    assert result == [
        ('a.b', '<AttributeError>'), 
        ('a.b.c', '<AttributeError>')
    ]

    source = 'a.b'
    v = Attrs(source)

# Generated at 2022-06-12 20:02:57.365772
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test for method items of class Attrs
    iobj = utils.InspectObject()
    iobj.f_locals['test'] = {'a': 1, 'b': 2, 'c': 3}
    iobj.f_globals['test2'] = [1,2,3]
    test = Attrs('test')
    assert test.__class__.items(iobj) == [('test', '{...}'), ('test.a', '1'), ('test.b', '2'), ('test.c', '3')]
    assert test.__class__.items(iobj, True) == [('test', '{...}'), ('test.a', '1'), ('test.b', '2'), ('test.c', '3')]
    
    # test for method items of class Keys
    test = Keys

# Generated at 2022-06-12 20:03:06.369357
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = frame_info.FrameInfo()
    frame.f_locals = {'a': 1}
    assert BaseVariable('a')._items(1, normalize=True) == [('a', '1')]
    assert BaseVariable('a')._items('qw', normalize=True) == [('a', '"qw"')]
    assert BaseVariable('a')._items(1.123, normalize=True) == [('a', '1.123')]
    assert BaseVariable('a')._items([1, 2, 3], normalize=True) == [('a', '[1, 2, 3]')]
    assert BaseVariable('a')._items(frame, normalize=True) == [('a', '<frame>')]

# Generated at 2022-06-12 20:03:18.010488
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class sample_main_value(object):
        def __getattr__(self, key):
            return key + '_attribute'
        def __getitem__(self, key):
            return key

    def test_method_items(self):
        test_items = self.items(None)
        return test_items

    def test_method_items_value_is_None(self):
        test_items = self.items(None)
        for test_item in test_items:
            assert test_item[1] == 'None'

    def test_method_items_value_not_None(self):
        test_items = self.items(None, sample_main_value())
        for test_item in test_items:
            assert test_item[1] == '<function>'


# Generated at 2022-06-12 20:03:18.704838
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-12 20:03:20.603166
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = frame_context.FrameContext(1)
    variable = BaseVariable('__name__')
    assert variable.items(frame)[0][1] == '\'__main__\''

# Generated at 2022-06-12 20:03:25.882392
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (('1', '2'), ('3', '4'))

    local_variable = TestVariable('main_value', 'exclude')
    assert local_variable.items('frame', 'normalize') == (('1', '2'), ('3', '4'))


# Generated at 2022-06-12 20:03:34.233061
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global_variables = {'x': 'x', 'y':'y', 'z': 'z'}
    local_variables = {'x': 'xx', 'y':'yy', 'z': 'zz'}
    frame = utils.Frame(
        ('<test>', 'test_BaseVariable_items', None),
        global_variables,
        local_variables
    )
    assert Attrs('x').items(frame) == (('x', "'xx'"),)
    assert Attrs('x', exclude=['x']).items(frame) == (('x', "'xx'"),)
    assert Attrs('x', exclude='x').items(frame) == (('x', "'xx'"),)
    assert Attrs('x', exclude=()).items(frame) == (('x', "'xx'"),)
   

# Generated at 2022-06-12 20:03:57.536773
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    frame = inspect.currentframe()
    frame = frame.f_back.f_back
    common_variable = CommonVariable('sys')
    print(common_variable.items(frame))

if __name__ == "__main__":
    test_BaseVariable_items()

# Generated at 2022-06-12 20:04:05.699448
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = Attrs("b")
    v._items("abcd", normalize=True)
    v._items("abcd", normalize=False)
    v._items(None, normalize=True)
    v._items(None, normalize=False)
    v._items(BaseVariable, normalize=True)
    v._items(BaseVariable, normalize=False)

    v = Keys("b")
    v._items("abcd", normalize=True)
    v._items("abcd", normalize=False)
    v._items(None, normalize=True)
    v._items(None, normalize=False)
    v._items(BaseVariable, normalize=True)
    v._items(BaseVariable, normalize=False)

    v = Indices("b")

# Generated at 2022-06-12 20:04:09.650467
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('x').items({}) == []
    assert BaseVariable('x').items(dict(x=1)) == [('x', '1')]
    assert BaseVariable('x').items(dict(x=[1])) == [
        ('x', '[...]'), ('x[0]', '1')]


# Unit tests for method items of class Attrs

# Generated at 2022-06-12 20:04:13.338690
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    local_var = "local variable"
    source = "local_var"
    variable = BaseVariable(source)
    frame = inspect.currentframe()
    print(variable.items(frame))

# Generated at 2022-06-12 20:04:23.540963
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import MockFrame
    mock_frame = MockFrame(['def foo():\n', '    x = {"Hello":"World"}\n'])
    base_variable = BaseVariable("x['Hello']")
    base_variable_result = base_variable.items(mock_frame)
    assert base_variable_result == [("x['Hello']", "'World'")]

    mock_frame = MockFrame(['def foo():\n', '    x = {"Hello":"World"}\n'])
    base_variable_exclude = BaseVariable("x", exclude=['items'])
    base_variable_exclude_result = base_variable_exclude.items(mock_frame)
    assert base_variable_exclude_result == [("x", "{'Hello': 'World'}")]



# Generated at 2022-06-12 20:04:32.055803
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = Exploding('abc')
    assert bv.items(None) == [('abc', 'abc')]

    bv = Exploding('abc.xyz')
    assert bv.items(None) == [('abc.xyz', 'abc.xyz')]

    bv = Exploding('(abc).xyz')
    assert bv.items(None) == [('(abc).xyz', '(abc).xyz')]

    bv = Exploding('abc', exclude=['x'])
    assert bv.items(None) == [('abc', 'abc')]

    bv = Exploding('abc', exclude=['x'])
    assert bv.items(None) == [('abc', 'abc')]

    bv = Exploding('abc.xyz', exclude=['x'])
    assert b

# Generated at 2022-06-12 20:04:42.729175
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import types
    import pprint

    def get_vars():
        """
        Return the variables in the caller's local scope.
        """
        function_attrs = inspect.stack()[1][0].f_locals
        if '__code__' in function_attrs:
            # check if the caller is a function
            if isinstance(function_attrs['__code__'], types.CodeType):
                return function_attrs
        # fallback
        return globals(), {}
    func_globals, func_locals = get_vars()

    def count_vars(variables, function_globals, function_locals):
        """
        Return the number of variables in the caller's scope.
        """
        i=0

# Generated at 2022-06-12 20:04:48.797529
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import __main__
    class BaseVariable_test:
        def __init__(self, source):
            self.source = source
        def items(self, frame, normalize=False):
          try:
              main_value = eval(self.source, frame.f_globals or {}, frame.f_locals)
          except Exception:
              return ()
          self._items(main_value)

__main__.BaseVariable_test = BaseVariable_test

# Generated at 2022-06-12 20:04:56.182031
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_shortish_repr
    class TestVariable(BaseVariable):
        def _items(self, key, normalize=False):
            return [('testSource', get_shortish_repr(key, normalize))]

    assert TestVariable('testSource').items({}) == [('testSource', '{}')]
    assert TestVariable('testSource').items(frame=None) == [('testSource', 'None')]
    assert TestVariable('testSource').items(frame=1, normalize=False) == [('testSource', '1')]
    assert TestVariable('testSource').items(frame=1, normalize=True) == [('testSource', '1')]


# Generated at 2022-06-12 20:05:06.954452
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Frame is the frame object from the call stack
    from inspect import currentframe
    frame = currentframe()
    # The variable "a" is not found in the frame object
    assert BaseVariable('a').items(frame) == ()
    # The variable "a" is in the frame object
    a = 1
    assert BaseVariable('a').items(frame) == ('a', '1')
    # The variable "a" is not found in the frame object, but it is in the global variable of the frame
    assert BaseVariable('a').items(frame.f_back) == ('a', '1')
    # The variable "a.b" is not found
    assert BaseVariable('a.b').items(frame) == ()
    # The variable "a.b" is in the frame
    a.b = 2

# Generated at 2022-06-12 20:05:57.041428
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    sys.dont_write_bytecode = True

    import unittest

    class BaseVariableTestCase(unittest.TestCase):
        def test_items(self):
            class A(object):
                def __init__(self, x):
                    self.x = x
            a = A(1)
            self.assertEqual(BaseVariable('a').items(sys._getframe()),
                             [('a', '1')])
            self.assertEqual(BaseVariable('a', ('x', )).items(sys._getframe()),
                             [('a', 'A object')])
            self.assertEqual(Attrs('a').items(sys._getframe()),
                             [('a', 'A object'), ('a.x', '1')])

# Generated at 2022-06-12 20:06:07.050904
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    
    # test case 1
    # this is a example to test method items
    frame = inspect.currentframe()
    # assuming that the caller is in the function test_BaseVariable_items
    test_variable = frame.f_back.f_locals['test_variable']
    # test_variable = {1:2, 3:4}

    # test case 2
    # this is a example to test method items
    # frame = inspect.currentframe()
    # assuming that the caller is in the function test_BaseVariable_items
    # test_variable = frame.f_back.f_locals['test_variable']
    # test_variable = ['a', 'b', 'c']

    # test case 3
    # this is a example to test method items
    # frame = inspect.currentframe()
    # assuming that

# Generated at 2022-06-12 20:06:14.426637
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    input_list = [1, 2, 3]
    assert Keys('input_list').items(dict()) == [('input_list', 'list(1, 2, 3)')]
    assert Keys(utils.get_shortish_repr(input_list)).items(dict(), normalize=True) == [('1, 2, 3', 'list(1, 2, 3)')]
    assert Indices('input_list[2]').items(dict()) == [('input_list[2]', '3')]
    assert Indices(utils.get_shortish_repr(input_list[2])).items(dict(), normalize=True) == [('3', '3')]

# Generated at 2022-06-12 20:06:23.712678
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .frame import Frame
    from .utils import ensure_tuple

    class MockFrame:
        def __init__(self, f_globals, f_locals):
            self.f_globals = f_globals
            self.f_locals = f_locals

    class MockModule:
        def __init__(self, name):
            self.__name__ = name


# Generated at 2022-06-12 20:06:33.021443
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from . import pycompat
    
    import inspect
    import itertools
    import abc
    try:
        from collections.abc import Mapping, Sequence
    except ImportError:
        from collections import Mapping, Sequence
    from copy import deepcopy
    
    from . import utils
    from . import pycompat
    
    
    def needs_parentheses(source):
        def code(s):
            return compile(s, '<variable>', 'eval').co_code
    
        return code('{}.x'.format(source)) != code('({}).x'.format(source))
    
    
    class BaseVariable(pycompat.ABC):
        def __init__(self, source, exclude=()):
            self.source = source

# Generated at 2022-06-12 20:06:43.191034
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var1 = Attrs('main_value', ['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10','test11','test12','test13','test14','test15','test16','test17','test18','test19','test20','test21','test22','test23','test24','test25','test26','test27','test28','test29','test30','test31','test32','test33','test34','test35','test36','test37','test38','test39','test40','test41','test42','test43','test44','test45','test46','test47','test48','test49','test50','test51','test52',])

# Generated at 2022-06-12 20:06:52.275858
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import re
    import os

    def items(key, value, normalize=False):
        variable = BaseVariable(key, normalize=normalize)
        return variable.items(value)

    def pattern(str):
        # pattern like regular expression
        pat = str.replace('.', '\\.').replace('$', '.(\d+)\\$')
        return re.compile(pat)

    class A(object):
        def __init__(self):
            self.a = 'A'
            self.b = 'B'

    class B(A):
        def __init__(self):
            super(B, self).__init__()
            self.b = 'B2'
            self.c = 'C'

        def m(self):
            a = 10
            return a

    a = A()


# Generated at 2022-06-12 20:06:58.293729
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Attr(BaseVariable):
        def __init__(self, attr):
            super(Attr, self).__init__(attr)
            self.code = compile(attr, '<variable>', 'eval')

        def _items(self, main_value, normalize=False):
            """
            :param main_value: could be a object or dictionary
            :return:
            """
            result = [(self.source, utils.get_shortish_repr(main_value))]
            for key in self._keys(main_value):
                try:
                    if key in self.exclude:
                        continue
                    value = self._get_value(main_value, key)
                except Exception:
                    continue

# Generated at 2022-06-12 20:07:03.764920
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_1():
        a = 1
        b = 2
        c = 3
        main_value = a
        # main_value = eval(self.source, frame.f_globals or {}, frame.f_locals)
        main_value = a

# Generated at 2022-06-12 20:07:13.629051
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class TestClass(object):
        def __init__(self):
            # Class attribute
            self.x1 = 'x1'

            # Class attribute with exception
            self.x2 = None
            if 1:
                raise RuntimeError('Some error')

            # Private attributes
            self.__x3 = 'x3'
            self.__x4 = 'x4'

            # Slots
            self.__slots__ = ['slot5', '__slot6']
            self.slot5 = 'slot5'
            self.__slot6 = 'slot6'

            # Custom getter
            self.__x7 = 'x7'
            self.__x7_getter = lambda: self.__x7

    test = TestClass()