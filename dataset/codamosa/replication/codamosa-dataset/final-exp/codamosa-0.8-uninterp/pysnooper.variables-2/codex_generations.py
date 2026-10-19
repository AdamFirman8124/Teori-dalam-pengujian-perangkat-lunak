

# Generated at 2022-06-12 19:58:50.804775
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')


# Generated at 2022-06-12 19:58:55.503074
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    v = Indices('x')
    for i in range(1, 7):
        assert v[:i] == v[:i]
        assert v[:i] == Indices('x')[:i]
        assert v[:i] == deepcopy(v[:i])
        assert v[:i] != v[:i+1]
        assert v[:i] != Indices('x')[:i+1]
        assert v[:i] != deepcopy(v[:i+1])

# tests

# Generated at 2022-06-12 19:58:59.990274
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    test = Indices('key')[1:-1]
    assert test._slice == slice(1, -1)
    assert test.source == 'key'
    assert test._fingerprint == (Indices, 'key', ())
    assert test._keys('foo') == range(3)[slice(1, -1)]


# Generated at 2022-06-12 19:59:05.002899
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    x = Indices('var')
    assert str(x[:]) == str(Indices('var'))
    assert str(x[1:3]) == str(Indices('var[1:3]'))


# Generated at 2022-06-12 19:59:07.625976
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # initialization
    a = BaseVariable('p.x', exclude=['y'])
    b = BaseVariable('p.x', exclude=['y'])
    # case of equal
    assert a == b, 'Test Failed - class variable should be equal'
    # modification
    b.source = 'q.z'
    # case of not equal
    assert a != b, 'Test Failed - class variable should not be equal'


# Generated at 2022-06-12 19:59:13.127687
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import os
    import sys
    import this
    import math
    from datetime import datetime
    from random import randint
    from itertools import cycle, chain

    var_i, var_j = 'i', 'j'
    ok_msg, fail_msg = 'passed', 'failed'
    assert this.s.startswith('The Zen of Python')

# Generated at 2022-06-12 19:59:25.040990
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from pprint import pprint
    # Custom exception class
    class MyException(Exception): pass
    # Custom exceptions
    exc1 = MyException('bad luck')
    exc2 = MyException('bad, bad luck')
    # An instance of a custom exception class
    exc3 = MyException()
    # A class with regular attributes and a __slots__
    class C(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
        __slots__ = ['d', 'e', 'f']
    c = C()
    c.d = 4
    c.e = 5
    c.f = 6
    # A tuple
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# Generated at 2022-06-12 19:59:29.323435
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = {'b': {'c': 'd'}}
    cls = Keys('a')
    assert cls.items(a, normalize=True) == [('a["b"]', '{"c": "d"}')]

# Generated at 2022-06-12 19:59:32.382695
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    a = Indices('a')
    assert a[1:3]._slice == slice(1,3)

    b = Indices('b')
    assert b[2:3]._slice == slice(2,3)

# Generated at 2022-06-12 19:59:35.254289
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    class cls(Indices):
        source = "a"
    assert "a[10:]" == cls()[10:].source
    #assert "a" == cls()[:10].source

# Generated at 2022-06-12 19:59:50.900747
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import datetime
    from pandas import DataFrame

    def test_common_variable(variable_cls, value, items):
        variable = variable_cls('foo')
        assert variable.items({'foo': value}) == items

    test_common_variable(Attrs, 1, [('foo', '1')])
    test_common_variable(Attrs, True, [('foo', 'True')])
    test_common_variable(Attrs, None, [('foo', 'None')])
    test_common_variable(Attrs, 'bar', [('foo', "'bar'")])
    test_common_variable(Attrs, datetime.date(2015, 1, 1), [('foo', "datetime.date(2015, 1, 1)")])

# Generated at 2022-06-12 20:00:00.398534
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from collections import defaultdict
    from pytest import raises
    from . import frame

    from datetime import datetime
    from . import exception

    def f():
        x = 1

    def add(lst, x):
        lst.append(x)

    def g():
        add([], 1)
        1 / 0

    def normalize(obj):
        return "<<<{}>>>".format(obj)

    frm = frame.Frame.from_frame(f.__globals__)
    # Test with the case of dict and list
    dct = {'a': {'b': 1, 'c': [2, 3], 'd': 4}, 'e': 5}
    lst = [{'a': 100}, {'b': [200, 300]}]

# Generated at 2022-06-12 20:00:10.189981
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import hashlib, binascii
    v1 = BaseVariable("test","test1","test2")
    v2 = BaseVariable("test","test2","test1")
    print("v1.__eq__(v2)=",v1.__eq__(v2))
    v3 = BaseVariable("test1","test2","test1")
    print("v1.__eq__(v3)=",v1.__eq__(v3))
    v4 = BaseVariable("test","test2","test3")
    print("v1.__eq__(v4)=",v1.__eq__(v4))
    v5 = BaseVariable("test","test2","test1")
    print("v2.__eq__(v5)=",v2.__eq__(v5))
    v5_hash = binas

# Generated at 2022-06-12 20:00:19.549686
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import CallData
    from .filters import Filter

    class MockFrame:
        @staticmethod
        def get_values(names):
            return [(name, None) for name in names.split(',')]

        def __init__(self, filename, lineno, **locals):
            self.f_globals = {}
            self.f_locals = locals
            self.f_code = CallData(filename, lineno)

    # test case 1
    # the source is a non-tuple non-dict
    source = '3'
    frame = MockFrame('test_BaseVariable_items', 3)
    var = BaseVariable(source)
    assert var.items(frame) == [(source, '3')]

    # test case 2
    source = 'a'

# Generated at 2022-06-12 20:00:24.103873
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    for source in ['1', '1+1', '[1,2]', '{"a":1}']:
        print("------", source, "--")
        var = BaseVariable(source)
        print(var.items({}))


# Generated at 2022-06-12 20:00:27.703083
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Given
    source = "someVar"
    exclude = 'dict'
    vs1 = BaseVariable(source, exclude)
    vs2 = BaseVariable(source, exclude)

    # When
    result = vs1.__eq__(vs2)

    # Then
    assert result == True

# Generated at 2022-06-12 20:00:29.065181
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs('foo.bar') == Attrs('foo.bar')


# Generated at 2022-06-12 20:00:35.410669
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import packets
    from .utils import format_frames
    import sys

    for packet in packets.parse(sys.stdin):
        print(format_frames([packet.frame], variables=[
            sys.exc_info()[0],  # builtin class
            packet.frame.f_code,  # code object
            packet.frame.f_locals,  # dictionary
            packet.frame.f_code.co_varnames  # tuple
        ]))

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:00:47.212186
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """Test if the items are correctly returned"""
    from . import stack
    from . import variables
    def test_func(i):
        f1 = 3
        f2 = 3
        f3 = 3
        f4 = 3
        f5 = 3
        f6 = 3
        f7 = 3
        f8 = 3
        f9 = 3
        f10 = 3
        f11 = 3
        f12 = 3
        f13 = 3
        f14 = 3
        f15 = 3
        f16 = 3
        f17 = 3
        f18 = 3
        f19 = 3
        f20 = 3
        f21 = 3
        f22 = 3
        f23 = 3
        f24 = 3
        f25 = 3
        f26 = 3
        f27 = 3
        f28 = 3

# Generated at 2022-06-12 20:00:58.654438
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # test Attrs class
    class A(object):
        name = 'adas'
        def __init__(self):
            self.age = 18
        def test_method(self):
            return True
    class B(object):
        pass

    a = A()
    a.b = B()
    a.b.c = 'adas'
    a.b.d = [1,2,3]

    v = Attrs('a')
    assert v.items(locals()) == [('a', 'adas'), ('a.name', '{}'), ('a.age', '18'), ('a.test_method', '<function test_method...>')]

    v_exclude = Attrs('a', exclude=['test_method'])

# Generated at 2022-06-12 20:01:10.241618
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert (
        BaseVariable('a') == BaseVariable('a')
    )
    assert (
        BaseVariable('a', exclude='b') == BaseVariable('a', exclude='b')
    )
    assert (
        BaseVariable('a', exclude='b') != BaseVariable('a', exclude='c')
    )
    assert (
        BaseVariable('a', exclude=('b',)) != BaseVariable('a', exclude=('c',))
    )
    assert (
        BaseVariable('a') != BaseVariable('b')
    )
    assert (
        BaseVariable('a') != BaseVariable('a', exclude='b')
    )
    assert (
        BaseVariable('a', exclude=('b', 'c')) == BaseVariable('a', exclude=('c', 'b'))
    )

# Generated at 2022-06-12 20:01:21.369762
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    locals = {'a':'abc', 'b':'abc', 'c':'abc'}
    globals = {'a':'abc', 'b':'abc', 'c':'abc'}
    iframe = pycompat.DummyObject()
    iframe.f_globals = globals
    iframe.f_locals = locals
    variable = Exploding('a.b.c')
    actual = variable.items(iframe)
    expected = [('a.b.c', 'abc')]
    assert actual == expected

    actual = variable.items(iframe, normalize = True)
    assert actual == expected

    variable = BaseVariable('a.b.c', exclude=())
    actual = variable.items(iframe)
    expected = [('a.b.c', 'abc')]
    assert actual == expected

# Generated at 2022-06-12 20:01:31.022197
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import inspect
    class BaseVariable_sub(BaseVariable):
        pass
    bv = BaseVariable_sub('bv.b')
    bv_sub = BaseVariable_sub('bv_sub.sub')
    bv2 = BaseVariable_sub('bv2.sub')
    print('-'*79)
    print(inspect.getsource(bv.__eq__))
    print('-'*79)
    print(bv.__eq__(bv_sub))
    print(bv.__eq__(bv2))
    print('-'*79)
    print(bv_sub.__eq__(bv2))
    print('-'*79)
    print(bv.__hash__())
    print(bv_sub.__hash__())

# Generated at 2022-06-12 20:01:37.591110
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def a(**kwargs):
        pass

    def b(z):
        pass

    def c(x, y):
        return x + y

    def d(x=1, y=2):
        return x + y

    f_globals = {
        'func_a': a,
        'func_b': b,
        'func_c': c,
        'func_d': d
    }
    frame = utils.Frame(0, '<module>', '', 'x=10', f_globals, {})

    assert BaseVariable('x').items(frame) == [('x', '10')]
    assert BaseVariable('x+1').items(frame) == [('(x+1)', '11')]
    assert BaseVariable('x', 'x').items(frame) == []


# Generated at 2022-06-12 20:01:38.957643
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    assert BaseVariable('a').items(None) == [('a', None)]



# Generated at 2022-06-12 20:01:47.508203
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Same source, same exclude
    assert BaseVariable('a', exclude='c') == BaseVariable('a', exclude='c')
    assert BaseVariable('a', exclude=('c',)) == BaseVariable('a', exclude='c')
    assert BaseVariable('a', exclude=['c']) == BaseVariable('a', exclude='c')
    assert BaseVariable('a', exclude='c') == BaseVariable('a', exclude=('c',))
    assert BaseVariable('a', exclude='c') == BaseVariable('a', exclude=['c'])
    assert BaseVariable('a', exclude=('c',)) == BaseVariable('a', exclude=['c'])
    # Same source, same exclude, but different instances subclasses:
    assert Attrs('a', exclude='c') == Keys('a', exclude='c')

# Generated at 2022-06-12 20:01:54.244623
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = BaseVariable('a')
    a.items(1)
    b = BaseVariable('b')
    b.items(1)
    BaseVariable('c')
    BaseVariable('c')
    items = [('a', 3), ('b', 4)]
    assert a.items(1) == items
    assert b.items(1) == items
    assert BaseVariable('c').items(1) == [('c', 1)]



# Generated at 2022-06-12 20:02:01.527219
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import pytest
    from . import print_tb
    from .utils import ensure_tuple


# Generated at 2022-06-12 20:02:06.981181
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from . import variables
    from pprint import pformat

    class X(BaseVariable):
        def _items(self, main_value, normalize=False):
            return None

    m1 = X('m1', ('foo',))
    m2 = X('m2', ('foo',))
    n1 = X('m1', ('foo',))
    n2 = X('m2', ('foo',))

    assert m1 == n1
    assert m2 == n2
    assert m1 != n2
    assert m2 != n1

    m = X('m.x')
    n = X('m.x')
    o = X('m.y')

    assert m == n
    assert m != o

    m = variables.Attrs('m')
    n = variables.Attrs('n')


# Generated at 2022-06-12 20:02:11.881497
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = None
    items = BaseVariable('a', 'b').items(frame)
    #print(items)
    #assert items == [(0,1), (1,4)]
    
    

if __name__ == '__main__':
    # Unit test for method items of class BaseVariable
    test_BaseVariable_items()

# Generated at 2022-06-12 20:02:27.627819
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # global variable
    global_var = 10
    class BaseVariableTest():
        def __init__(self):
            self.a = 100
            self.b = 200

    global_var = BaseVariableTest()
    variable = BaseVariable('global_var', ('a',))
    # Calling items method of class BaseVariable
    variable_result = variable.items(None)
    # The result should be a tuple of variables
    assert isinstance(variable_result, tuple)
    # The first variable is global_var
    assert variable_result[0][0] == 'global_var'
    # The first variable value is BaseVariableTest object
    assert variable_result[0][1] == 'BaseVariableTest'
    # The second variable is global_var.b
    assert variable_result[1][0] == 'global_var.b'


# Generated at 2022-06-12 20:02:34.650354
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = Attrs('a')
    a2 = Attrs('a')
    assert a1 == a2

    a3 = Attrs('a', exclude=('a', 'b'))
    a4 = Attrs('a', exclude=('a', 'b'))
    a5 = Attrs('a', exclude=('a', 'b', 'c'))
    assert a3 == a4
    assert a4 != a5
    assert a4 != 'a'



# Generated at 2022-06-12 20:02:39.924137
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    variable1 = BaseVariable('a')
    variable2 = BaseVariable('b')
    variable3 = BaseVariable('a')
    variable4 = BaseVariable('b')
    variable5 = BaseVariable('a', exclude=['b'])
    variable6 = BaseVariable('a', exclude=['b'])

    assert variable1 == variable3
    assert variable2 == variable4
    assert variable1 != variable2
    assert variable2 != variable1
    assert variable1 != variable5
    assert variable5 == variable6

    assert variable1 != object()
    assert variable1 == variable1

# Generated at 2022-06-12 20:02:49.471906
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = sys._getframe()

    # Test the case of a non-executable expression.
    class BaseVariable1(BaseVariable):
        def __init__(self):
            super(BaseVariable1, self).__init__(source='a b')
    variable1 = BaseVariable1()
    assert variable1.items(frame) == ()

    # Test the case of a single variable.
    class BaseVariable2(BaseVariable):
        def __init__(self):
            super(BaseVariable2, self).__init__('_')
    variable2 = BaseVariable2()
    assert variable2.items(frame) == (('_', '<built-in function id>'),)

    # Test the case of attributes
    class BaseVariable3(BaseVariable):
        def __init__(self):
            super(BaseVariable3, self).__

# Generated at 2022-06-12 20:02:58.175765
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import frame_codeinfo

    local_variable = {'local_num':1, 'local_list':[1,2]}
    global_variable = {'global_num':1, 'global_list':[1,2]}
    frame = frame_codeinfo(local_variable=local_variable, global_variable=global_variable)

    variable_dict = {
        'a': Attrs('a'),
        'b': Attrs('b', exclude='x'),
        'c': Keys('c'),
        'd': Keys('d', exclude='y'),
        'e': Indices('e'),
        'f': Indices('f', exclude=2),
        'g': Exploding('g'),
        'h': Exploding('h', exclude='z')
    }


# Generated at 2022-06-12 20:03:07.050139
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Variable(BaseVariable):

        def __init__(self, source, exclude=()):
            self.source = source
            self.exclude = utils.ensure_tuple(exclude)
            self.code = compile(source, '<variable>', 'eval')

        def items(self, frame, normalize=False):
            try:
                main_value = eval(self.code, frame.f_globals or {}, frame.f_locals)
            except Exception:
                return ()
            return self._items(main_value, normalize)

        def _items(self, main_value, normalize=False):
            return self.source

    assert Variable("a", "b") is not Variable("a", "b")
    assert Variable("a", "b") == Variable("a", "b")

# Generated at 2022-06-12 20:03:18.181299
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect

    class A:
        _foo = 'bar'
        _list = [1, 2, 3]

        def method(self):
            return 42

    local_variables = inspect.getargvalues(sys._getframe()).locals

    assert list(Attrs('A').items(sys._getframe())) == [
        ('A', 'A()'),
        ("A.__module__", repr(__name__)),
        ("A._foo", repr("bar")),
        ("A._list", repr([1, 2, 3])),
        ("A.method", repr(A.method))
    ]

# Generated at 2022-06-12 20:03:23.122914
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = None
    v = BaseVariable('a', 'b')
    print(v.items(frame))
    v = Attrs('a', 'b')
    print(v.items(frame))
    v = Keys('a', 'b')
    print(v.items(frame))
    v = Indices('a', 'b')
    print(v.items(frame))
    v = Exploding('a', 'b')
    print(v.items(frame))

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:03:27.856394
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('foo')
    v2 = BaseVariable('foo')
    v3 = BaseVariable('bar')

    assert v1 == v1
    assert v1 == v2
    assert v2 == v1
    assert v1 != v3
    assert v3 != v1
    assert v2 != v3
    assert v3 != v2



# Generated at 2022-06-12 20:03:34.794527
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = Keys('a')
    b = Keys('b')
    c = Keys('a')
    d = Keys('a', exclude=('abc'))
    assert a == a # __eq__ is reflexive
    assert a != b and b != a # __eq__ is symmetric
    assert a != b and b != c and a != c # __eq__ is transitive
    assert a == c # __eq__ is congruent
    assert a != d

if __name__ == '__main__':
    import inspect
    for name, obj in inspect.getmembers(utils):
        if inspect.isclass(obj) and issubclass(obj, BaseVariable):
            eval(name + '.test()')

# Generated at 2022-06-12 20:03:48.235136
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = stack.Frame(None, 'test_BaseVariable_items', 'test.py', 10, None, None)
    frame.f_locals = {'a': {0: {1: 2}}}
    v = BaseVariable('a')
    print(v.items(frame))

test_BaseVariable_items()


# Generated at 2022-06-12 20:03:55.950092
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    sys.path.append('/home/lxj/PycharmProjects/PythonData/PythonData/traceback_variables_example')
    import vars

    object_vars = [Attrs('obj').items(vars.frame, normalize=False),
                   Keys('dict').items(vars.frame, normalize=False),
                   Indices('list')[:].items(vars.frame, normalize=True),
                   Exploding('explode').items(vars.frame, normalize=False),
                   ]
    # print(object_vars)

test_BaseVariable_items()

# Generated at 2022-06-12 20:04:03.043710
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = {
        'a': {
            'b': 1,
            'c': 2
        }
    }
    assert Attrs('a').items(frame) == [('a', "{'b': 1, 'c': 2}")]
    assert Keys('a').items(frame) == [('a', "{'b': 1, 'c': 2}")]
    assert Indices('a').items(frame) == [('a', "{'b': 1, 'c': 2}")]
    assert Exploding('a').items(frame) == [('a', "{'b': 1, 'c': 2}")]
    assert Attrs('a', 'b').items(frame) == [('a', "{'b': 1, 'c': 2}")]

# Generated at 2022-06-12 20:04:03.863425
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    pass



# Generated at 2022-06-12 20:04:11.395756
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import codecs
    from io import StringIO
    from . import utils

    class FakeFrame(object):
        def __init__(self, f_locals):
            self.f_locals = f_locals

    def normalize(s):
        return utils.get_shortish_repr(s, normalize=True)

    frame = FakeFrame({
        'x': lambda: 1,
        'y': 'abc',
        'z': [1, 2, 3]
    })

    # test class Attrs
    x = Attrs('x')
    assert x.items(frame) == [
        ('x', normalize('<function <lambda> at 0x%x>' % id(x.items))),
        ('x()', '1')
    ]

    y = Attrs('y')
   

# Generated at 2022-06-12 20:04:14.380594
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = frame_mock()
    a = BaseVariable(source='a', exclude=())
    assert(a.items(frame) == [('a', 'a')])

# Unit tests for class Attrs

# Generated at 2022-06-12 20:04:24.467363
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import os
    from . import utils
    from . import pycompat

    class CustomDict(pycompat.dict):
        pass
    custom_dict = CustomDict()
    custom_dict['key'] = 'val'

    frame_variables = {'main_value': custom_dict, 'source': 'source', 'exclude': 'exclude'}
    frame = utils.Frame(sys._getframe())
    frame.f_globals = frame_variables
    frame.f_locals = frame_variables

    class Mock(BaseVariable):
        pass

    base_variable = Mock(frame_variables['source'], frame_variables['exclude'])
    result = base_variable.items(frame)
    assert type(result) is tuple
    assert len(result) == 1

# Generated at 2022-06-12 20:04:29.917900
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import debug
    import inspect

    def x():
        y = 2
        z = 3
        return locals()
    frame = inspect.currentframe()
    frame = frame.f_back
    frame.f_locals = x()

    var = BaseVariable('x')
    items = var.items(frame, normalize = True)
    debug.pp(items)

    assert items[0] == ('x', '2')



# Generated at 2022-06-12 20:04:36.185123
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = pycompat.FakeFrame(f_locals={'a_variable':{'a':2,'b':3,'c':4},\
                                         'another_variable':[1,2,3,4],\
                                         'yet_another_variable':{'a':2,'b':3,'x':5}})

    a_variable = Keys('a_variable')
    assert a_variable.items(frame) == [('a_variable', a_variable.unambiguous_source),
                                       ('a_variable[\'a\']', '2'),
                                       ('a_variable[\'b\']', '3'),
                                       ('a_variable[\'c\']', '4')]

    another_variable = Indices('another_variable')

# Generated at 2022-06-12 20:04:46.608629
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import dis
    import sys
    import types

    test_code_1 = """\
    def test():
    x = 1
    """
    test_code_2 = """\
    def test():
        x = 1
        y = 2
        def inner():
            z = 1
            y = 3
        inner()
    """
    test_code_3 = """\
    def test():
        z = 1
        y = 2
        def inner():
            z = 1
            y = 3
        inner()
    """
    test_code_4 = """\
    def test():
        x = 1
        for i in range(10):
            x = i
    """

    def get_code(source):
        """ Construct and return a code object for a function containing a given source code """
        # Get the source code

# Generated at 2022-06-12 20:05:10.556323
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Exploding(BaseVariable):
        pass

    class Attrs(BaseVariable):
        pass

    class Keys(BaseVariable):
        pass

    class Indices(BaseVariable):
        pass

    x1 = Exploding('x')
    x2 = Exploding('y')
    x3 = Exploding('x', exclude=['x'])
    x4 = Exploding('x', exclude=['y'])
    x5 = Attrs('x')
    x6 = Keys('x')
    x7 = Indices('x')
    assert x1 == x1
    assert x1 != x2
    assert x1 != x3
    assert x1 != x4
    assert x1 != x5
    assert x1 != x6
    assert x1 != x7


# Generated at 2022-06-12 20:05:19.460697
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    source = 'frame'
    exclude = ('f_lasti', 'f_back')
    baseVariable = BaseVariable(source)
    baseVariable.items(frame)
    baseVariable.items(frame, normalize=False)
    baseVariable.items(frame, normalize=True)
    baseVariable.items(frame, normalize=True)
    baseVariable.items(frame, normalize=False)
    baseVariable.items(frame, normalize=True)
    baseVariable.items(frame, normalize=False)
    baseVariable.items(frame, normalize=True)
    baseVariable.items(frame, normalize=False)
    baseVariable._items(frame)
    exclude = exclude + range(0, len(exclude))

# Generated at 2022-06-12 20:05:30.887872
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect

    def test(expected, code, input_dict):
        frame = inspect.currentframe()
        frame = frame.f_back.f_back.f_back
        assert BaseVariable(code).items(frame, False) == expected, str(code) + " " + str(input_dict)
    test([('a', '0')], 'a', {'a':0})
    test([('b', '1')], 'b', {'b':1, 'a':0})
    test([('b.x', '2')], 'b.x', {'b':{'x':2, 'y':3}, 'a':0})

# Generated at 2022-06-12 20:05:42.382458
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from spyder.utils.codeanalysis import get_definition
    from spyder.utils.qthelpers import qapplication
    _app = qapplication()

    def code(s):
        return compile(s, '<variable>', 'eval').co_code

    def _get_names_helper(frame, *names):
        return set(name for name, _ in get_definition(code(name),
                   name, frame) for name in names)

    def _get_variables_helper(frame, source):
        variables = Variables(source, ())
        return {name: repr(value) for name, value in variables.items(frame)}

    test_source = 'a.b.c[1]'
    a = C()
    b = C()
    c = C()
    a.b = b

# Generated at 2022-06-12 20:05:47.440811
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class TestVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return ('foo', 'bar')

    frame = inspect.currentframe()
    variable = TestVariable('source')
    assert variable.items(frame) == ('foo', 'bar')

# Generated at 2022-06-12 20:05:56.415533
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Test(BaseVariable):
         def _items(self, main_value, normalize=False):
             return [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]

    test = Test('self')
    items = test.items(test)
    assert items[0] == ('self', '{...}')
    items = test.items(test, normalize=True)
    assert items[0] == ('self', '{...}')

    test = Test('i')
    items = test.items(test)
    assert items[0] == ('i', '...')
    items = test.items(test, normalize=True)
    assert items[0] == ('i', '...')


# Generated at 2022-06-12 20:06:01.291197
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    import doctest
    doctest.testmod(verbose=True)
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('b', 'c') == BaseVariable('b', 'c')
    assert BaseVariable('b') != BaseVariable('b', 'c')
    assert BaseVariable('d', 'c') != BaseVariable('b', 'c')

# Generated at 2022-06-12 20:06:06.294591
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # 1. source, exclude is empty
    # 1.1 Cls1 == Cls1
    assert BaseVariable("", "") == BaseVariable("", "")
    # 1.2 Cls1 == Cls2
    assert BaseVariable("", "") != BaseVariable("", "")
    # 2. source, exclude is NOT empty
    # 2.1 Cls1 == Cls1
    assert BaseVariable("x.y", "") == BaseVariable("x.y", "")
    # 2.2 Cls1 == Cls2
    assert BaseVariable("x.y", "") != BaseVariable("x.y", "")

# Generated at 2022-06-12 20:06:13.871285
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import types

    def f(a):
        return a + 1

    expected = (('a', '1'), ('a.x', '1'))

    class A(object):
        x = 1

    a = A()
    # Test class Attrs
    frame = sys._getframe()
    frame.f_locals['a'] = a
    frame.f_locals['b'] = Attrs('a')
    frame.f_globals['A'] = A
    frame.f_globals['f'] = f
    frame.f_globals['sys'] = sys
    frame.f_globals['types'] = types

    assert next(b.items(frame)) == ('a.x', '1')

    # Test class Keys
    b = Keys('a')

# Generated at 2022-06-12 20:06:14.673368
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    v = BaseVariable("fred")


# Generated at 2022-06-12 20:06:55.593167
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frame
    from . import tracer
    from . import fake_filesystem
    from . import source

    line = '\n'
    filename = 'test_BaseVariable_items.py'

    # write test file
    with fake_filesystem.FakeFilesystem():
        with fake_filesystem.FakeFileOpen(filename, 'w') as testfile:
            testfile.write(line)

    # read test file
    tracer = tracer.Tracer()
    with tracer.ignore_package(source):
        with open(filename) as testfile:
            globals_dict = {'testfile': testfile}
            with tracer.trace():
                exec(line, globals_dict)

    frame_list = list(tracer.frame_iterator())
    assert len(frame_list) == 1
   

# Generated at 2022-06-12 20:07:05.951533
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    result = BaseVariable('a', exclude=('a',)).items(frame=None)
    assert result == ()
    assert isinstance(result, tuple)

    result = BaseVariable('a', exclude='a').items(frame=None)
    assert result == ()
    assert isinstance(result, tuple)

    result = BaseVariable('a').items(frame=None)
    assert result == (('a', "NameError: name 'a' is not defined"), )
    assert isinstance(result, tuple)

    result = BaseVariable('a').items(frame={'a': [1,2]})
    assert result == (
        ('a', '[1, 2]'),
        ('a[0]', '1'),
        ('a[1]', '2')
    )
    assert isinstance(result, tuple)

# Generated at 2022-06-12 20:07:15.376356
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    class Base(Exception):
        pass

    class A(Exception):
        x = 12

    class B(A):
        y = 34

    class C(B):
        z = 56

    class D(C):
        def __init__(self, s=''):
            super(D, self).__init__()
            self.s = s

    try:
        raise D('Hello world!')
    except D as e:
        f = sys.exc_info()[2].tb_frame
        print(list(Attrs('e').items(f)))
        print(list(Indices('sys.argv').items(f)))
        print(list(Exploding('sys.argv').items(f)))
        print(list(Exploding('e').items(f)))


# Generated at 2022-06-12 20:07:26.733905
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class Sub_BaseVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return self.source, normalize

    class Sub_CommonVariable(CommonVariable):
        def _keys(self, main_value):
            return self.source, normalize

        def _format_key(self, key):
            return [(self.source, self.unambiguous_source, key)]

        def _get_value(self, main_value, key):
            return self.source, self.unambiguous_source, key

    frame = {'x': 'xyz'}
    r = Sub_BaseVariable('x').items(frame)
    assert r == 'x', False

    r = Sub_CommonVariable('x').items(frame)

# Generated at 2022-06-12 20:07:33.744275
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import frame
    f = frame.Frame(None, None, None, None)
    t = (1, 2, 3)
    x = Attrs('t')
    assert x.items(f) == x._items(t)
    str(x.items(f)[0][0]) == 't'
    str(x.items(f)[0][1]) == '(1, 2, 3)'
    str(x.items(f)[1][0]) == 't.__add__'
    str(x.items(f)[1][0]) == 't.__add__'

# Generated at 2022-06-12 20:07:38.747137
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
  v1 = BaseVariable('x', exclude = ['a', 'b'])
  v3 = BaseVariable('x', exclude = 'b')
  v4 = BaseVariable('x')
  v2 = BaseVariable('x', exclude = ['a', 'b'])
  assert v1 == v2
  assert v1 != v3
  assert v1 != v4
  assert v1 != 5
  assert v1 != 'x'


# Generated at 2022-06-12 20:07:39.769001
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('x') == BaseVariable('x')


# Generated at 2022-06-12 20:07:47.031392
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestVar(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (
                ('self.source', self.source),
                ('self.exclude', self.exclude),
                ('type(self)', type(self)),
                ('self.code', self.code)
            )
    testvar = TestVar('testvar', exclude=['testvar'])

# Generated at 2022-06-12 20:07:51.263855
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    d = {'a': 1, 'b': 2}
    source = 'd'
    frame = {}
    frame['d'] = d
    v = BaseVariable(source)
    assert v.items(frame) == [('d', "dict")]

# Generated at 2022-06-12 20:07:57.623853
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from inspect import currentframe
    from byexample.common import Variable, Example
    from byexample.parser import ExampleParser
    from byexample.runner import ExampleRunner
    from byexample.finder import ExampleFinder
    from byexample.registry import ExampleFinderRegistry
    #
    # Given a variable, a single example and a Example Runner
    class SimpleVar(BaseVariable):
        def __init__(self):
            BaseVariable.__init__(self, "var")

        def items(self, frame, normalize=False):
            return []

        def _items(self, main_value, normalize=False):
            return []
