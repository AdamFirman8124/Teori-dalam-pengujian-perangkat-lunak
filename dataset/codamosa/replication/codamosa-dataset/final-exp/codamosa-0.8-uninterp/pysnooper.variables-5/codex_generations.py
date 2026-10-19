

# Generated at 2022-06-12 19:58:53.508243
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Positive cases:
    i = BaseVariable('i', exclude=())
    assert i == BaseVariable('i', exclude=())

    i = BaseVariable('i', exclude=('A','B','C'))
    assert i == BaseVariable('i', exclude=('B','C','A'))

    i = BaseVariable('i', exclude=('A','B','C'))
    assert i == BaseVariable('i', exclude=('A','C','B'))

    i = BaseVariable('i', exclude=('A','B','C'))
    assert i == BaseVariable('i', exclude=('A','B','C'))

    # Negative cases:
    i = BaseVariable('i', exclude=('A','B','C'))
    assert not (i == BaseVariable('i', exclude=()))


# Generated at 2022-06-12 19:59:02.798385
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class V(BaseVariable):
        def __init__(self, a, b, c, d=1, e=2):
            pass

    v0 = V(1, 2, 3)
    v1 = V(1, 2, 3)
    v2 = V(1, 2, 3, d=1)
    v3 = V(1, 2, 3, d=3)
    v4 = V(1, 2, 3, 1, 2)
    v5 = V(1, 2, 3, e=2, d=1)
    v6 = V(1, 2, 3, e=3, d=1)

    assert v0 == v0
    assert v0 == v1
    assert v0 == v2
    assert v0 == v4
    assert v0 == v5
    assert v4 == v

# Generated at 2022-06-12 19:59:11.883247
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys
    frame = inspect.currentframe()
    frame = frame.f_back
    frame = frame.f_back
    # Utils.get_shortish_repr
    frame = frame.f_back
    # BaseVariable.items
    frame = frame.f_back

    source_code = "sys.executable"
    baseVariable = BaseVariable(source_code)
    result = baseVariable.items(frame)
    assert result == [('sys.executable', '<str>')]

    # There is a method named items in class BaseVariable and a function named items in module ScopeAccess

    # Look up items in class BaseVariable
    # '_items' is a private method
    result = inspect.getmembers(baseVariable, inspect.isfunction)
    assert len(result) == 2

# Generated at 2022-06-12 19:59:18.837615
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Aclass(BaseVariable):
        def _items(self, key, normalize=False):
            pass
    variable1 = Aclass('a')
    variable2 = Aclass('b')
    variable3 = Aclass('a')
    variable4 = Aclass('a', exclude=('a',))

    assert variable1 != variable2
    assert variable1 == variable3
    assert variable1 != variable4


# Generated at 2022-06-12 19:59:24.762555
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert(BaseVariable('x') == BaseVariable('x'))
    assert(not BaseVariable('x') == BaseVariable('y'))
    assert(BaseVariable('x', exclude='y') == BaseVariable('x', exclude='y'))
    assert(not BaseVariable('x', exclude='y') == BaseVariable('x', exclude='z'))
    assert(BaseVariable('x', exclude=('y',)) == BaseVariable('x', exclude='y'))

# Generated at 2022-06-12 19:59:27.502242
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    bv = BaseVariable('x')
    result = bv.items(None)
    assert result == ()


# Generated at 2022-06-12 19:59:33.257968
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def tracing_items(frame, normalize=False):
        return True

    # record the tracing_items method
    original_method = BaseVariable.items
    BaseVariable.items = tracing_items
    # call the function
    bv = BaseVariable('', '')
    assert(bv.items(None, True) == True)
    # restore the original method
    BaseVariable.items = original_method

# Generated at 2022-06-12 19:59:40.234018
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    sample_source = "sample_source" 
    sample_exclude = ['sample_exclude']
    BaseVariable_instance = BaseVariable(sample_source,sample_exclude)
    assert BaseVariable_instance.source == "sample_source" 
    assert BaseVariable_instance.exclude == ('sample_exclude',)
    assert BaseVariable_instance.code == compile("sample_source", '<variable>', 'eval')
    assert BaseVariable_instance.unambiguous_source == "sample_source" 
    assert BaseVariable_instance._items(None) == ()
    assert BaseVariable_instance._items(None,True) == ()


# Generated at 2022-06-12 19:59:46.584952
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("foo") == BaseVariable("foo")
    assert BaseVariable("foo", exclude=("bar",)) == BaseVariable("foo", exclude=("bar",))
    assert BaseVariable("foo") != BaseVariable("foo", exclude=("bar",))
    assert BaseVariable("foo") != BaseVariable("bar", exclude=("bar",))
    assert BaseVariable("foo") != BaseVariable("foo", "bar")
    assert BaseVariable("foo", exclude=("bar",)) != BaseVariable("bar", exclude=("bar",))
    assert BaseVariable("foo", exclude=("bar",)) != BaseVariable("foo", exclude=("baz",))
    assert BaseVariable("foo", "bar") != BaseVariable("foo", "baz")


# Generated at 2022-06-12 19:59:48.350926
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    var = Indices('var')
    assert var[0] == Indices('var', _slice=slice(0, 1))

# Generated at 2022-06-12 20:00:07.245491
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert not BaseVariable('a') == BaseVariable('b')
    assert BaseVariable('a', exclude='a') == BaseVariable('a', exclude='a')
    assert not BaseVariable('a', exclude='a') == BaseVariable('a', exclude='b')

# Generated at 2022-06-12 20:00:12.409371
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var_1 = BaseVariable('x')
    var_2 = BaseVariable('x')
    var_3 = BaseVariable('y')
    var_4 = BaseVariable('x', 'y')
    var_5 = BaseVariable('x', 'y')

    assert(var_1 == var_2)
    assert(var_2 == var_1)
    assert(var_1 != var_3)
    assert(var_1 != var_4)
    assert(var_4 == var_5)


# Generated at 2022-06-12 20:00:19.476797
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'foo'
    exclude = ('aaa', 'bbb', 'ccc')
    bv1 = BaseVariable(source, exclude)
    bv2 = BaseVariable(source, exclude)
    assert(bv1 == bv2)
    bv1 = BaseVariable(source, 'aa')
    bv2 = BaseVariable(source, ('a', 'b', 'c'))
    assert(bv1 == bv2)
    bv1 = BaseVariable(source, 'aa')
    bv2 = BaseVariable(source, 'aa')
    assert(bv1 == bv2)

# Generated at 2022-06-12 20:00:24.104475
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    obj = Indices(source='x[1:3]', exclude=())
    result = obj[1:3]
    expected = Indices(source='x[1:3]', exclude=(), _slice=slice(1,3))
    assert result == expected

# Generated at 2022-06-12 20:00:33.844100
# Unit test for method __eq__ of class BaseVariable

# Generated at 2022-06-12 20:00:39.295183
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('') == BaseVariable('')
    assert BaseVariable('') == BaseVariable('', ())
    assert BaseVariable('') == BaseVariable('', [])
    assert BaseVariable('') != BaseVariable('', ['x'])
    assert BaseVariable('') != BaseVariable('', ('x',))
    assert BaseVariable('') != BaseVariable('', 'x')

    # Test to make sure that the method __eq__ returns NotImplemented if the types are different.
    # This is necessary for the correct behavior of the method __hash__.
    assert BaseVariable('') != 'boo'


test_BaseVariable___eq__()

# Generated at 2022-06-12 20:00:49.725345
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from .variables import BaseVariable
    from .variables import CommonVariable
    from .variables import Attrs
    from .variables import Keys
    from .variables import Indices

    class test_class_1(object):
        """
        Test class for testing __eq__ method of BaseVariable class
        """

        def __init__(self):
            self.source = 1
            self.exclude = 2

    class test_child_class_1(BaseVariable):
        """
        Test child class 1
        """

        def __init__(self, source, exclude):
            super().__init__(source, exclude)
            self.var1 = 1

    class test_class_2(object):
        """
        Test class 2
        """

        def __init__(self):
            self.source = None

# Generated at 2022-06-12 20:01:00.721676
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import pytest
    from . import test_utils
    from .test_utils import mock_frame
    from . import utils
    import mock

    # Patch isinstance to make all objects instances of Sequence and Mapping
    with mock.patch.object(utils, 'isinstance') as isinstance:
        isinstance.side_effect = lambda x, y: True
        frame = mock_frame(test_utils.test_frame.f_globals, {'x': [{'a': 1}, {'b': 2}]})

        assert Keys('x').items(frame) == [('x', "[{'a': 1}, {'b': 2}]")]
        assert Attrs('x').items(frame) == [('x', "[{'a': 1}, {'b': 2}]")]
        assert Indices('x').items

# Generated at 2022-06-12 20:01:06.724127
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from unittest.mock import Mock
    frame = Mock(f_globals={})
    v = BaseVariable('a')
    v.code = Mock()
    v._items = Mock()
    v.items(frame)
    v.code.assert_called_once_with('a', frame.f_globals, frame.f_locals)
    v._items.assert_called_once_with(v.code.return_value, normalize=False)


# Generated at 2022-06-12 20:01:12.665169
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    m = BaseVariable('a', 'b')
    m1 = BaseVariable('a', 'b')
    m2 = BaseVariable('a.b', 'b')
    m3 = BaseVariable('a.f', 'b')
    assert m == m1
    assert m != m2
    assert m != m3


register_built_ins = utils.register_built_ins


# Generated at 2022-06-12 20:01:27.549255
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = mock.send_command("eval -i 1 --no-namespace print(self)")
    variable = Attrs("self")
    result = variable.items(frame)
    variable = Indices("self")
    result = variable.items(frame)
    variable = Keys("self")
    result = variable.items(frame)

# Generated at 2022-06-12 20:01:29.284619
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("x", "y") == BaseVariable("x", "y")


# Generated at 2022-06-12 20:01:37.763585
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # mock code
    frame = Mock()
    frame.f_globals = None
    frame.f_locals = {}
    # mock data
    data = [
        (Mock(), frame),
        (Mock(), frame)
    ]
    data[0][0].source = 'source1'
    data[0][0].exclude = ()
    data[1][0].source = 'source2'
    data[1][0].exclude = 'test'

    for test in data:
        obj, frame = test
        assert(obj.items(frame) == ())



# Generated at 2022-06-12 20:01:46.694157
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    def _test_eq(lhs, rhs, expected):
        print('{{{lhs}}}.__eq__({{{rhs}}}) == {expected}'.format(lhs=lhs, rhs=rhs, expected=expected))
        v1 = Attrs(lhs)
        v2 = Attrs(rhs)
        assert v1.__eq__(v2) == expected

    def _test_ne(lhs, rhs):
        print('{{{lhs}}}.__eq__({{{rhs}}}) == False'.format(lhs=lhs, rhs=rhs))
        v1 = Attrs(lhs)
        v2 = Attrs(rhs)
        assert v1.__eq__(v2) == False

    _test_eq('x', 'x', True)
    _test

# Generated at 2022-06-12 20:01:47.240725
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    pass

# Generated at 2022-06-12 20:01:50.415012
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    bv1 = BaseVariable(source=1, exclude=2)
    bv2 = BaseVariable(source=1, exclude=2)
    assert bv1 == bv2


# Generated at 2022-06-12 20:01:59.430598
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import os
    import io

    def io_wrapper(s):
        s = io.StringIO(s)
        s.name = '<string>'
        return s

    def get_var(stdout, **kwargs):
        return BaseVariable(stdout.getvalue(), **kwargs)

    for stdout in (io_wrapper('a'), 'a', 'a.b', 'a[0]', 'a()', 'a'):
        var = get_var(stdout)
        var_items = var.items(None)
        assert len(var_items) == 1
        assert var_items[0][0] == 'a'
        assert var_items[0][1] == 'a'

    stdout = io_wrapper('a: {b}')
    var = get_var(stdout)
   

# Generated at 2022-06-12 20:02:04.646202
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1_0 = BaseVariable.BaseVariable("a")
    v1_1 = BaseVariable.BaseVariable("a")
    v2_0 = BaseVariable.BaseVariable("b")
    assert v1_0 == v1_1
    assert v1_0 != v2_0

# Generated at 2022-06-12 20:02:08.916957
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a', 'b')
    b = BaseVariable('a', 'b')
    c = BaseVariable('a', 'c')
    d = BaseVariable('c', 'b')
    e = BaseVariable('d', 'c')

    assert a == a
    assert a == b
    assert a != c
    assert a != d
    assert a != e

# Generated at 2022-06-12 20:02:12.370946
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    main_value = {'a':1}
    k = Keys('main_value')
    c = k.items(None)
    print(c)


if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:02:21.666789
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a')
    v2 = BaseVariable('b')
    v3 = BaseVariable('b')
    assert v1 != v2
    assert v2 == v3


# Generated at 2022-06-12 20:02:30.782068
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'my_variable'
    exclude = 'value'
    tmp_1 = BaseVariable(source, exclude)
    tmp_2 = BaseVariable(source, exclude)
    tmp_3 = BaseVariable(source, exclude)
    assert(tmp_1.__eq__(tmp_2) and tmp_2.__eq__(tmp_3))
    source = None
    tmp_1 = BaseVariable(source, exclude)
    assert(not tmp_1.__eq__(tmp_2) and not tmp_2.__eq__(tmp_1))
    exclude = None
    tmp_1 = BaseVariable(source, exclude)
    tmp_2 = BaseVariable(source, exclude)
    assert(tmp_1.__eq__(tmp_2) and tmp_2.__eq__(tmp_1))

# vim: et sw

# Generated at 2022-06-12 20:02:39.684962
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    '''
    # Case 1
    BaseVariable(BaseVariable('foo')) == BaseVariable(BaseVariable('foo'))
    '''
    # Case 1
    # Function: BaseVariable.__eq__
    assert BaseVariable(BaseVariable('foo')) == BaseVariable(BaseVariable('foo'))
    '''
    # Case 2
    BaseVariable(BaseVariable('foo')) != BaseVariable(BaseVariable('foo'))
    '''
    # Case 2
    # Function: BaseVariable.__eq__
    assert BaseVariable(BaseVariable('foo')) != BaseVariable(BaseVariable('foo'))
    return 0


# Generated at 2022-06-12 20:02:43.517344
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class BaseVariable0(BaseVariable):
        def _items(self, key, normalize=False):
            return ()
    class BaseVariable1(BaseVariable):
        def _items(self, key, normalize=False):
            return ()
    assert BaseVariable0(source='a') != BaseVariable0(source='b')
    assert BaseVariable0(source='a') != BaseVariable1(source='a')
    assert BaseVariable0(source='a', exclude='b') != BaseVariable0(source='a')
    v0 = BaseVariable0(source='a')
    assert v0 == v0



# Generated at 2022-06-12 20:02:46.736098
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Variable(source, list_exclude)
    a = BaseVariable('a')
    b = BaseVariable('a')
    c = BaseVariable('a')
    e = BaseVariable('e')
    d = BaseVariable('a', ('b',))
    # print(a == b)
    # print(a == c)
    # print(a == e)
    # print(a == d)
    assert a == b
    assert a == c
    assert  a != e
    assert  a != d

if __name__ == '__main__':
    test_BaseVariable___eq__()

# Generated at 2022-06-12 20:02:50.167815
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('a')
    var2 = BaseVariable('b')
    var3 = BaseVariable('a')
    assert var1 == var1
    assert var1 != var2
    assert var1 == var3

# Generated at 2022-06-12 20:02:58.642512
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    from . import pycompat
    from . import BaseVariable

    class BaseVariable(BaseVariable):
        class BaseVariable(BaseVariable):
            pass

        pass

    class BaseVariable(BaseVariable):
        class BaseVariable(pycompat.ABC):
            pass

        def BaseVariable(self, source, exclude=()):
            self.source = source
            self.exclude = utils.ensure_tuple(exclude)
            self.code = compile(source, '<variable>', 'eval')
            if needs_parentheses(source):
                self.unambiguous_source = '({})'.format(source)
            else:
                self.unambiguous_source = source

    class BaseVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            self.source

# Generated at 2022-06-12 20:03:03.963516
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert Attrs('x') == Attrs('x')
    assert Attrs('x') != Attrs('x', exclude='a')
    assert Attrs('x') != Attrs('y', exclude='a')
    assert Attrs('x') != Attrs('y')
    assert Attrs('x') != Keys('x')
    assert Attrs('x') != Indices('x')
    assert Attrs('x') != object()


# Generated at 2022-06-12 20:03:09.462024
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'c'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b', 'c'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b', 'd'))
    print(BaseVariable('a', 'b') == BaseVariable('a', 'b', 'c', 'd'))
    print(BaseVariable('b', 'a') == BaseVariable('a', 'b'))
    print(BaseVariable('a', 'b', 'c') == BaseVariable('a', 'b', 'd'))

# Generated at 2022-06-12 20:03:14.337827
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class Test1(BaseVariable):
        def __init__(self, test):
            self.test = test

        def _items(self, main_value, normalize=False):
            return self.test

        @property
        def _fingerprint(self):
            return (type(self), self._test)

        def __hash__(self):
            return hash(self._fingerprint)


    class Test2(BaseVariable):
        def __init__(self, test):
            self.test = test

        def _items(self, main_value, normalize=False):
            return self.test

        @property
        def _fingerprint(self):
            return (type(self), self._test)

        def __hash__(self):
            return hash(self._fingerprint)


    assert Test1('a') == Test

# Generated at 2022-06-12 20:03:31.931585
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class MyVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return []
    assert MyVariable('a') == MyVariable('a')
    assert MyVariable('a') != MyVariable('b')
    assert MyVariable('a', [0]) == MyVariable('a', [0])
    assert MyVariable('a', [0]) != MyVariable('a', [])
    assert MyVariable('a', [0]) != MyVariable('b', [0])
    assert MyVariable('a', [0]) != MyVariable('a', [1])

# Generated at 2022-06-12 20:03:36.791223
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # yes
    bv1 = BaseVariable("a")
    bv2 = BaseVariable("a")
    assert bv1 == bv2

    bv3 = BaseVariable("a", ("b",))
    bv4 = BaseVariable("a", ("b",))
    assert bv3 == bv4

    # no
    bv5 = BaseVariable("a", ("c",))
    bv6 = BaseVariable("a", ("b",))
    assert bv5 != bv6

    bv7 = BaseVariable("a", ("c", "d"))
    bv8 = BaseVariable("a", ("b",))
    assert bv7 != bv8


# Generated at 2022-06-12 20:03:47.195437
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    for c in [Attrs, Keys, Indices, Exploding]:
        # c is a class inherited from BaseVariable
        assert isinstance(c, pycompat.ABCMeta)
        assert issubclass(c, BaseVariable)
        g = {}
        exec('\n'.join([
            'class Child(BaseVariable):',
            '    def _items(self, main_value, normalize=False):',
            '        return ("source: "+self.source.__repr__(), "main_value: "+main_value.__repr__())'
            ]), g)
        Child = g['Child']
        assert issubclass(Child, BaseVariable)
        source = 'source_value'
        a = Child(source)
        assert a.source == source
        items_a = a.items(None)
        assert items

# Generated at 2022-06-12 20:03:56.809682
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    import sys
    import os
    os.chdir("..")
    import config
    import datetime
    def test_items(variable, frame = inspect.currentframe()):
        print("\nvariable: " + variable.source)
        for k, v in variable.items(frame):
            print("{} {}".format(k, v))
    # Test for method Keys._keys
    Keys("config.data")._keys(config.data)
    # Test for method Items._format_key
    Keys("config.data")._format_key("redis")
    # Test for method Items._get_value
    Keys("config.data")._get_value(config.data, "redis")
    # Test for method Items._items
    test_items(Keys("config.data"))
    # Test for method Indices

# Generated at 2022-06-12 20:04:01.965219
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable(source="source", exclude="exclude")
    b = BaseVariable(source="source_b", exclude="exclude")
    c = BaseVariable(source="source", exclude="exclude_c")
    d = BaseVariable(source="source", exclude="exclude")
    e = str()
    assert a.__eq__(b) != True
    assert a.__eq__(c) != True
    assert a.__eq__(d) == True
    assert a.__eq__(e) != True


# Generated at 2022-06-12 20:04:04.055341
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__(): 
    """Test function of method __eq__ of BaseVariable"""
    assert(BaseVariable("a.b.c","d")==BaseVariable("a.b.c","d"))


# Generated at 2022-06-12 20:04:11.526941
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # pylint:disable=unused-variable
    class TestClass(object):
        def __init__(self):
            self.__dict__['foo'] = 42
            self.bar = 33
            self.baz = None
        @property
        def prop(self):
            return 'prop'
    # pylint:enable=unused-variable

    # Given
    instance = TestClass()
    frame = inspect.currentframe()
    # And
    base_var_attrs = Attrs('instance')
    base_var_keys = Keys('instance')
    base_var_indices = Indices('instance')
    base_var_exploding = Exploding('instance')
    # When
    items_attrs = list(base_var_attrs.items(frame))

# Generated at 2022-06-12 20:04:21.855967
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class TestClass:
        def __init__(self, a, b=1, c=2, d=3):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        def test_method(self):
            pass
        def __repr__(self):
            return 'TestClass(a=%s, b=%s, c=%s, d=%s)' % (self.a, self.b, self.c, self.d)

    test_obj = TestClass('test_1')
    test_obj.test_dict = dict(test_key='test_value')


# Generated at 2022-06-12 20:04:24.383946
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (('a', 'b'), ('c', 'd'))

    source = 'source'
    var = MyVariable(source)
    var.items = BaseVariable.items # using the original function
    frame = 'frame'
    normalize = 'normalize'
    assert var.items(frame, normalize) == (('source', 'b'), ('source', 'd'))


# Generated at 2022-06-12 20:04:28.351196
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    source = "a_variable"
    exclude = "key_to_exclude"
    v = BaseVariable(source, exclude)
    assert v.items("a frame") == ((source, ""), ('{}{}'.format(source, '.' + exclude), ""))

# Generated at 2022-06-12 20:04:53.057237
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    key = 'abcdefghijklmnopqrstuvwxyz1234567890'
    main_value = {key: 1}
    frame = {key: main_value}
    result = Keys(key).items(frame)
    assert result == [(key, 1)]
    result = Attrs(key).items(frame)
    assert result == []
    result = Indices(key).items(frame)
    assert result == []
    result = Exploding(key).items(frame)
    assert result == [(key, 1)]

# Generated at 2022-06-12 20:04:58.161395
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    bob = BaseVariable("abc")
    tom = BaseVariable("qwerty")
    bob_bob = BaseVariable("abc")
    bob_tom = BaseVariable("qwerty")
    bob_qwerty = BaseVariable("qwerty")
    assert(bob == bob_bob)
    assert(tom == bob_tom)
    assert(bob != tom)
    assert(bob != bob_tom)
    assert(tom != bob)
    assert(tom != bob_bob)
    assert(bob != bob_qwerty)
    assert(tom != bob_qwerty)


# Generated at 2022-06-12 20:05:08.092371
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    '''
    Description:
        Method __eq__ of class BaseVariable returns True or False as expected.

    Success Criteria:
        Method __eq__ of class BaseVariable returns True when two instances are equal, 
        and returns False when two instances are not equal.
    '''
    # Initialize two instances of class BaseVariable to test method __eq__
    var1 = BaseVariable('source', exclude=('exc', 'exc2'))
    var2 = BaseVariable('source', exclude=('exc2', 'exc'))
    var3 = BaseVariable('source', exclude=('exc',))
    var4 = BaseVariable('source1', exclude=('exc',))
    var5 = BaseVariable('source', exclude=('exc', 'exc2', 'exc3'))

    # Return True when two instances are equal
    assert (var1 == var2)

# Generated at 2022-06-12 20:05:10.111303
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable("1")
    v2 = Attrs("1")
    assert v1 == v2


# Generated at 2022-06-12 20:05:14.151633
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a1 = BaseVariable("bye",exclude)
    a2 = BaseVariable("bye",exclude)
    assert a1==a2
    a3 = BaseVariable("bye",[2])
    assert a1!=a3
    assert a1!=1
    assert a1!="hello"


# Generated at 2022-06-12 20:05:16.716374
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = 'f.g'
    base_variable = BaseVariable(source)
    assert base_variable.__eq__(base_variable)



# Generated at 2022-06-12 20:05:18.856573
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a')
    b = BaseVariable('a')
    assert a == b


# Generated at 2022-06-12 20:05:30.707495
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Unit test for method items of class CommonVariable
    def test_CommonVariable_items():
        # Unit test for method items of class Attrs
        def test_Attrs_items():
            def check(var, expected_result, **kwargs):
                frame = utils.DummyFrame()
                frame.f_globals = dict(kwargs.get('globals', {}))
                frame.f_locals = dict(kwargs.get('locals', {}))
                assert var.items(frame, kwargs.get('normalize', False)) == expected_result

            class TestClass(object):
                def method(self):
                    pass
            check(Attrs('a'), [])
            check(Attrs('c'), [], locals=dict(c=TestClass()))

# Generated at 2022-06-12 20:05:41.915708
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    t0 = type('A', (BaseVariable,), {'_keys': lambda self, x: 'A'})
    t1 = type('B', (BaseVariable,), {'_keys': lambda self, x: 'B'})
    assert t0('') == t0('')
    assert not (t0('') == t1(''))
    assert t0('x') == t0('x')
    assert not (t0('x') == t0(''))
    assert t0('x', ('x',)) == t0('x', ('x',))
    assert not (t0('x', ('x',)) == t0('x'))
    assert t0('x', ('x',)) == t1('x', ('x',))

# Generated at 2022-06-12 20:05:52.849258
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = Keys('a', exclude=['x'])
    v2 = Keys('a', exclude=['x'])
    v3 = Keys('a', exclude=['y'])
    v4 = Keys('b', exclude=['x'])
    print("v1.__hash__() = " + str(v1.__hash__()))
    print("v2.__hash__() = " + str(v2.__hash__()))
    print("v3.__hash__() = " + str(v3.__hash__()))
    print("v4.__hash__() = " + str(v4.__hash__()))
    print("v1 == v2 = " + str(v1 == v2))
    print("v1 == v3 = " + str(v1 == v3))

# Generated at 2022-06-12 20:06:37.814822
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame = pycompat.builtins.__dict__['_getframe']()
    print(frame.f_lineno)
    print(frame.f_globals)
    # print(frame.f_locals)
    print(frame.f_back)
    v = Keys('frame.f_locals', 'exclude')
    print(v.items(frame, True))

# Generated at 2022-06-12 20:06:46.312088
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    # my_var = {'a':1, 'b':2}
    source = 'my_var'
    v = BaseVariable(source)
    print(v.items(frame))
    # my_var = {'a':1, 'b':2}
    source = 'my_var'
    v = BaseVariable(source,exclude=['a'])
    print(v.items(frame))
    # my_var = {'a':1, 'b':2}
    source = 'my_var'
    v = BaseVariable(source,exclude=['a','b'])
    print(v.items(frame))


# Generated at 2022-06-12 20:06:51.157258
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # main_value.x
    var = BaseVariable('main_value.x')
    # main_value.x = 3
    frame_locals = {'main_value': {'x':3}}
    # Create a frame with the right locals
    frame = utils.create_frame('<test source>', frame_locals)
    # main_value.x = 3
    test_result = ('main_value.x', 3)
    assert test_result in var.items(frame)
    # main_value.y = 4
    frame_locals['main_value']['y'] = 4
    # Create a frame with the right locals
    frame = utils.create_frame('<test source>', frame_locals)
    # main_value.y = 4

# Generated at 2022-06-12 20:06:52.982761
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    var = Indices('foo')
    frame = pycompat.fake_frame_with_locals({'foo': ['bar']})
    result = var.items(frame)
    assert result == [('foo[0]', "'bar'")]



# Generated at 2022-06-12 20:07:00.824440
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import utils
    class MockFrame(object):
        f_locals = {'a': 'frame_locals_a'}
    source = 'a'
    exclude = ('a', )
    bv = BaseVariable(source, exclude)
    frame = MockFrame()
    assert(bv.items(frame, normalize=False) == (('a', 'frame_locals_a'), ))
    # No effect on items
    assert(bv.items(frame, normalize=True) == (('a', 'frame_locals_a'), ))
    assert(bv.items(frame, normalize=False) == (('a', 'frame_locals_a'), ))
    

# Generated at 2022-06-12 20:07:11.700645
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    frame_globals = {}
    frame_locals = {}
    frame_locals['dictobj'] = {}
    frame_locals['dictobj']['key1'] = 'value1'
    frame_locals['dictobj']['key2'] = 'value2'
    frame_locals['dictobj']['key3'] = 'value3'

    frame_locals['listobj'] = ['listvalue1', 'listvalue2']

    frame_locals['classobj'] = type('ClassObject', (object,), {'attr1': 'attrvalue1', 'attr2': 'attrvalue2'})()

    # unit test for method items of class Attrs
    attrs = Attrs('.classobj')

# Generated at 2022-06-12 20:07:19.212079
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    variables = ['a', 'list', 'dict']
    list = [1, 2, 'hello']
    dict = {'a': 1, '2': 'b', 'c': [1, 2]}
    frame = {'a': 1, 'list': list, 'dict': dict}
    frame.update(f_locals=frame, f_globals=frame)

# Generated at 2022-06-12 20:07:28.822609
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    def test_BaseVariable_items_BaseVariable(BaseVariable, source, frame, expected):
        actual = dict(BaseVariable(source).items(frame))
        assert actual == expected

    def test_BaseVariable_items_CommonVariable(CommonVariable, source, frame, expected):
        actual = dict(CommonVariable(source).items(frame))
        assert actual == expected

    # BaseVariable
    source = 'x'
    frame = utils.DummyFrame(x=1)
    expected = {'x': '1'}
    test_BaseVariable_items_BaseVariable(BaseVariable, source, frame, expected)
    with pytest.raises(NotImplementedError):
        BaseVariable(source)._items(None)

    # CommonVariable
    source = 'x'
    frame = utils.DummyFrame(x=1)

# Generated at 2022-06-12 20:07:39.167482
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    dict_ = {'a': 1, 'b': 2}
    d = dict_['a']
    assert 'd = dict_[\'a\']' == d.items('d')[0][0]
    assert '1' == d.items('d')[0][1]
    dict_['a'] = dict_['b']
    assert 'dict_[\'a\']' != d.items('d')[0][0]
    assert 'dict_[\'b\']' == d.items('d')[0][0]
    assert '2' == d.items('d')[0][1]
    # unit test for method items of class CommonVariable
    dict_ = {'a': 1, 'b': 2}

# Generated at 2022-06-12 20:07:49.069385
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test items of class BaseVariable
    def test_one(var, frame, expected):
        got = list(var.items(frame))
        assert got == expected

    # Test items of class Attrs
    def test_attrs():
        # Get attribute of an object
        class C:
            attr = 'abc'

        var = Attrs('C')

        test_one(var, {'C': C}, [('C.attr', "'abc'")])

    # Test items of class Keys
    def test_keys():
        # Get index of a list
        var = Keys('l')

        test_one(var, {'l': [1, 2, 3]}, [('l[0]', '1'), ('l[1]', '2'), ('l[2]', '3')])

        # Get index of a tuple