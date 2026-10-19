

# Generated at 2022-06-12 19:58:46.941800
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    indices = Indices('a', ())
    slice = slice(1, 2, 3)
    assert indices[slice]._slice is slice
    assert indices[slice] is not indices

# Generated at 2022-06-12 19:58:54.087491
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .utils import get_shortish_repr_test
    import sys
    def get_shortish_repr_test_patch(obj, normalize=False):
        return obj

    # Test for keys are not in exclude
    class test(BaseVariable):
        def _items(self, main_value, normalize=False):
            return (('a.a',get_shortish_repr_test_patch(main_value.a)),('a.b',get_shortish_repr_test_patch(main_value.b)),('a.c',get_shortish_repr_test_patch(main_value.c)))
    class a:
        def __repr__(self):
            return 'a'
        a=5
        b=6
        c=7
        x=a()
        y=b

# Generated at 2022-06-12 19:58:59.900490
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('foo') == BaseVariable('foo')
    assert BaseVariable('foo', exclude=['bar']) == BaseVariable('foo', exclude=['bar'])
    assert BaseVariable('foo') != BaseVariable('bar')
    assert BaseVariable('foo', exclude=['bar']) != BaseVariable('foo')
    assert BaseVariable('foo', exclude=['bar']) != BaseVariable('foo', exclude=['baz'])


# Generated at 2022-06-12 19:59:04.672812
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    foo1 = BaseVariable('foo')
    foo2 = BaseVariable('foo')
    bar = BaseVariable('bar')

    assert foo1 == foo2
    assert foo1 != bar



# Generated at 2022-06-12 19:59:06.961499
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    ind = Indices('a').__getitem__(slice(2,7))
    print(ind._slice)
    
    

# Generated at 2022-06-12 19:59:09.078951
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    inst = Indices("logger.handlers")
    assert inst._slice == slice(None)
    inst0 = inst[0:2]
    assert inst0._slice == slice(0, 2)


# Generated at 2022-06-12 19:59:10.054861
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():
    ind = Indices("main_value")[2:4]
    assert ind._slice == slice(2,4,None)

# Generated at 2022-06-12 19:59:12.121356
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    obj_1 = BaseVariable(source='a', exclude=('b',))
    obj_2 = BaseVariable(source='a', exclude=('b',))
    assert(obj_1.__eq__(obj_2) == True)


# Generated at 2022-06-12 19:59:20.175840
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class MyVariable(CommonVariable):
        def _keys(self, main_value):
            return main_value.keys()
        def _format_key(self, key):
            return '[{}]'.format(key)
        def _get_value(self, main_value, key):
            return main_value[key]

    d = {"aa":22, "bb":33}
    variable = MyVariable(source = "d")

# Generated at 2022-06-12 19:59:29.393636
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import test_utils
    from . import test_integration

    # A test frame
    frame = test_utils.create_frame({'a':3, 'b':4})

    # A BaseVariable
    var = BaseVariable('a')
    items = var.items(frame)
    assert isinstance(items, tuple)
    assert len(items) == 1
    assert items[0][0] == 'a'
    assert items[0][1] == '3'

    # A BaseVariable
    var = BaseVariable('a', exclude=['a'])
    items = var.items(frame)
    assert isinstance(items, tuple)
    assert len(items) == 0

    # A BaseVariable
    var = BaseVariable('a', exclude=['b'])
    items = var.items(frame)

# Generated at 2022-06-12 19:59:39.811930
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # create two objects of class BaseVariable
    obj_BaseVariable_1 = BaseVariable('src1')
    obj_BaseVariable_2 = BaseVariable('src1')
    
    # test the method __eq__
    assert obj_BaseVariable_1.__eq__(obj_BaseVariable_2) == True, "test of method __eq__ in class BaseVariable failed!"


# Generated at 2022-06-12 19:59:46.741407
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import cli
    import inspect
    import os
    import re

    # Test file for unit test
    f = inspect.currentframe()
    rootdir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(rootdir, 'test_BaseVariable.py')
    fname = os.path.basename(filepath)

    # Determine the source code of this unit test
    source = inspect.getsourcelines(f)[0]
    source_str = ''.join(source)
    # Get the source code of lines that are calling the print method to print the variables
    print_lines = [re.search('# (.*)', line).group(1) for line in source if 'print' in line]

    # Use vars of class cli.Exploding

# Generated at 2022-06-12 19:59:53.339420
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import demo
    from inspect import currentframe
    from copy import deepcopy
    from .utils import get_shortish_repr
    # Create an instance of testDemo class
    d = demo.testDemo("test")
    # Create an instance of BaseVariable class
    b = BaseVariable("d")
    # initialize list of expected tuples of tracked variable items
    expected = []
    # generate list of expected tuples of tracked variable items
    for k in b._keys(d):
        expected.append((
            '{}{}'.format(b.unambiguous_source, b._format_key(k)),
            get_shortish_repr(b._get_value(d, k))
        ))
    # append the main variable in the list
    expected.append(("d", get_shortish_repr(d)))

# Generated at 2022-06-12 19:59:58.172994
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import inspect
    frame = inspect.currentframe()
    src = 'frame.f_back.f_back.f_back.f_locals[\'x\']'
    variable_instance = BaseVariable(src,exclude = 'y')
    for item in variable_instance.items(frame):
        print(item)


if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:00:08.451789
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    good_sources_1 = ['my_list', 'my_function()']
    bad_sources_1 = ['A', 'a', 'a1', 'd[0]']
    exclude_1 = ()
    variable_1 = BaseVariable(good_sources_1[0], exclude_1)

    good_sources_2 = ['my_list', 'my_function()']
    bad_sources_2 = ['A', 'a', 'a1', 'd[0]']
    exclude_2 = 'a'
    variable_2 = BaseVariable(good_sources_2[1], exclude_2)

    # Two variables are not equal if their sources are not equal
    assert not (BaseVariable(bad_sources_1[0]) == BaseVariable(bad_sources_2[0]))

# Generated at 2022-06-12 20:00:17.190524
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert Attrs('a') == Attrs('a')
    assert Keys('a') == Keys('a')
    assert Indices('a') == Indices('a')
    assert Exploding('a') == Exploding('a')

    assert BaseVariable('a') != BaseVariable('b')
    assert Attrs('a') != Attrs('b')
    assert Keys('a') != Keys('b')
    assert Indices('a') != Indices('b')
    assert Exploding('a') != Exploding('b')

    assert BaseVariable('a') != Attrs('a')
    assert Attrs('a') != Keys('a')
    assert Keys('a') != Indices('a')
    assert Indices('a') != Exploding('a')
    assert Exploding('a') != Base

# Generated at 2022-06-12 20:00:20.589939
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    source = source = "os.path.abspath('.')"
    variable1 = BaseVariable(source)
    variable2 = BaseVariable(source)
    variable3 = BaseVariable(source, "path")
    variable4 = BaseVariable(source, "path")
    assert variable1 == variable2
    assert variable3 == variable4
    assert variable1 != variable3

# Generated at 2022-06-12 20:00:24.103623
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('k') == BaseVariable('k')
    assert BaseVariable('k') != BaseVariable('v')

# Generated at 2022-06-12 20:00:33.181921
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
  class TestClass1(BaseVariable):
      def __init__(self, source, exclude=()):
          BaseVariable.__init__(self, source, exclude)
          self.code = compile(source, '<variable>', 'eval')

  class TestClass2(BaseVariable):
      def __init__(self, source, exclude=()):
          BaseVariable.__init__(self, source, exclude)
          self.code = compile(source, '<variable>', 'eval')

  a = TestClass1(1, 2)
  b = TestClass1(1, 2)
  assert a == b
  c = TestClass2(1, 2)
  assert a != c
  d = TestClass1(1, 3)
  assert a != d

# Generated at 2022-06-12 20:00:37.742468
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class DummyVariable(BaseVariable):
        def _items(self, main_value, normalize=False):
            return ('DummyVariable', main_value)

    assert DummyVariable('foo').items({'foo': 'bar'}) == ('DummyVariable', 'bar')

# Generated at 2022-06-12 20:00:52.439258
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    x = [100, 200]
    frame = utils.mock.MagicMock(f_locals={'x':x})

    variable = Keys('x')
    assert variable.items(frame) == [('x', '[100, 200]'), ('x[0]', '100'), ('x[1]', '200')]

    variable = Indices('x')
    assert variable.items(frame) == [('x', '[100, 200]'), ('x[0]', '100'), ('x[1]', '200')]

    variable = Attrs('x')
    assert variable.items(frame) == [('x', '[100, 200]')]

    variable = Exploding('x')

# Generated at 2022-06-12 20:00:57.289820
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('e.c')
    v2 = BaseVariable('e.c')
    assert v1 == v2
    assert hash(v1) == hash(v2)


if __name__ == '__main__':
    import sys
    import pytest
    pytest.main(sys.argv)

# Generated at 2022-06-12 20:01:04.228377
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # initialize a object for a frame
    import os
    import sys
    from .frame import Frame
    frame = Frame(sys._getframe())
    # initialize a object for a BaseVariable
    var1 = BaseVariable('os', exclude=('O_RDWR','O_RDONLY','O_NONBLOCK','O_APPEND','F_OK','R_OK','W_OK','X_OK','O_CLOEXEC','O_CREAT','O_EXCL','O_NOCTTY','O_TRUNC','O_TTY_INIT','O_WRONLY','SEEK_CUR','SEEK_END','SEEK_SET','P_NOWAIT','P_WAIT'))
    # test the method items of BaseVariable
    actual = var1.items(frame)

# Generated at 2022-06-12 20:01:10.952315
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    local_dict = {
        'a' : [1,2]
    }
    a = local_dict['a']
    b = local_dict['b']
    attrs = Attrs('a').items(sys._getframe())
    assert attrs[0] == ('a', '[1, 2]')
    keys = Keys('a').items(sys._getframe())
    assert keys[0] == ('a', '[1, 2]')
    assert keys[1] == ('a[0]', '1')
    assert keys[2] == ('a[1]', '2')
    indices = Indices('a').items(sys._getframe())
    assert indices[0] == ('a', '[1, 2]')
    assert indices[1] == ('a[0]', '1')

# Generated at 2022-06-12 20:01:16.378595
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable("a", "b")
    var2 = BaseVariable("a", "b")
    var3 = BaseVariable("a", "b", "c")

    assert var1 == var2
    assert not var1 == var3


# Generated at 2022-06-12 20:01:23.564666
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # create a frame object, initialize it
    frame = inspect.currentframe()
    frame.f_locals = {
        'v1': '1', 'v2': [2, 3], 'v3': {4: 5}, 'v4': [[6], [7, 8]],
        'v5': {9: [10, 11]}, 'v6': 'None', 'v7': 'True', 'v8': 'False',
        'v9': '',
    }
    # check the items of v1
    items = BaseVariable('v1').items(frame)
    assert items == [('v1', '1')]

    # check the items of v2
    items = BaseVariable('v2').items(frame)

# Generated at 2022-06-12 20:01:32.652374
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from _pydevd_bundle.pydevd_constants import DICT_KEYS_ARE_ORDERED, DICT_KEYS_ARE_NOT_ORDERED
    from .local import List
    
    original_DICT_KEYS_ORDERED = DICT_KEYS_ARE_ORDERED
    DICT_KEYS_ARE_ORDERED = DICT_KEYS_ARE_ORDERED and DICT_KEYS_ARE_NOT_ORDERED

# Generated at 2022-06-12 20:01:43.308657
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("n+1") == BaseVariable("n+1")
    assert BaseVariable("n+1", exclude=("a", "b")) == BaseVariable("n+1", exclude=("a", "b"))
    assert BaseVariable("n+1") != BaseVariable("n+1", exclude=("a", "b"))
    assert BaseVariable("n+1") != BaseVariable("n+2")
    assert BaseVariable("n+1") != BaseVariable("m+1")
    assert BaseVariable("n+1") != BaseVariable("n+1", exclude=("a"))
    assert BaseVariable("n+1", exclude=("a", "b")) != BaseVariable("n+1", exclude=("a"))

# Generated at 2022-06-12 20:01:48.066366
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class BaseVariableMock(BaseVariable):
        def __init__(self, source, exclude=()):
            self.source = source
            self.code = compile(source, '<variable>', 'eval')
    frame = {"abc": 123, "x": "123", "y": "456"}
    test_BaseVariable = BaseVariableMock("abc")
    assert test_BaseVariable.items(frame, True)[0] == ("abc", "123")
    test_BaseVariable = BaseVariableMock("x+y")
    assert test_BaseVariable.items(frame, True)[0] == ("x+y", "(123 + 456)")


# Generated at 2022-06-12 20:01:52.894368
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable("a") == BaseVariable("a")
    assert BaseVariable("a", exclude="b") == BaseVariable("a", exclude="b")

    assert BaseVariable("a") != BaseVariable("b")
    assert BaseVariable("a") != BaseVariable("a", exclude="b")


# Generated at 2022-06-12 20:02:12.129427
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    source = 'sys.version_info'
    v = BaseVariable(source)
    assert 'sys.version_info' in v.items(sys._getframe())
    # test black_list
    b = Attrs(source, ['__name__'])
    assert all('__name__' not in s for s, _ in b.items(sys._getframe()))

test_BaseVariable_items()

# Generated at 2022-06-12 20:02:13.888907
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert not (BaseVariable('a') == BaseVariable('b'))


# Generated at 2022-06-12 20:02:18.765720
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    local_varialbles_dict={'x':'local', 'y':'local'}
    global_varialbles_dict={'x':'global'}
    Attrs('x').items(global_varialbles_dict)

    Keys('x').items(global_varialbles_dict)

    Indices('x').items(global_varialbles_dict)

    Exploding('x').items(global_varialbles_dict)

test_BaseVariable_items()

# Generated at 2022-06-12 20:02:24.786600
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import copy
    from .utils import get_mock_frame
    from .init import config
    from . import variables

    conf = copy.copy(config)

    conf.show_values = True
    conf.show_default_values = True
    conf.show_args = True
    conf.show_locals = True
    conf.show_globals = True

    conf.show_hidden_frames = True
    var_dct = dict()
    var_dct['num'] = 1
    var_dct['num2'] = 2
    var_dct['real'] = 1.1
    var_dct['real2'] = 2.2
    var_dct['str'] = 'str'
    var_dct['str2'] = 'str2'

# Generated at 2022-06-12 20:02:29.350457
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from . import stack

    class KV(BaseVariable):
        def _items(self, key, normalize=False):
            return [('key', key), ('value', '')]

    class KV2(KV):
        pass

    assert KV('x').items(stack.get_frame(0)) == KV2('x').items(stack.get_frame(0))



# Generated at 2022-06-12 20:02:34.164290
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    BaseVariable_obj = BaseVariable('source')
    def __init__(source, exclude=()):
        BaseVariable.__init__(BaseVariable_obj, source, exclude)
    BaseVariable_obj.__init__ = __init__
    assert BaseVariable_obj == BaseVariable_obj


# Generated at 2022-06-12 20:02:38.834186
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a', ('b', 'c')) == BaseVariable('a', ('b', 'c'))
    assert BaseVariable('a', ('b', 'c')) != BaseVariable('a', ('b', 'c', 'd'))
    assert BaseVariable('a', ('b', 'c')) != BaseVariable('a', ('b', 'c',))
    assert BaseVariable('a', ('b', 'c')) != BaseVariable('b', ('b', 'c'))

# Generated at 2022-06-12 20:02:43.498224
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('foo')
    var2 = BaseVariable('foo')
    var3 = BaseVariable('foo', exclude=('bar',))
    var4 = BaseVariable('foo', exclude='bar')
    var5 = BaseVariable('foo', exclude='baz')
    assert var1 == var2
    assert var1 != var3
    assert var3 == var4
    assert var1 != var5



# Generated at 2022-06-12 20:02:46.740597
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    func1 = BaseVariable('x')
    func2 = BaseVariable('x')
    func3 = BaseVariable('y')
    func4 = BaseVariable('x', ('y',))
    assert (func1 == func2) == True
    assert (func1 == func3) == False
    assert (func1 == func4) == False

# Generated at 2022-06-12 20:02:56.866705
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import random
    import string

    def create_random_variable_name():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

    def get_local_variables_from_debugger_protocol(frame):
        return frame.f_locals

    def get_local_variables_from_pycompat_Frame(frame):
        return frame.f_locals

    def random_test():
        random.seed(0)
        nb_step = random.randint(1, 5)
        variables = [create_random_variable_name() for _ in range(nb_step)]

        def get_random_value_from_existing_variables():
            if variables:
                return variables[random.randint(0, len(variables)-1)]

# Generated at 2022-06-12 20:03:09.145600
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('x') == BaseVariable('x')
    assert BaseVariable('x', exclude=('y')) == BaseVariable('x', exclude=('y'))

# Generated at 2022-06-12 20:03:13.929034
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class DummyVariable(BaseVariable):
        def __init__(self, source, exclude=()):
            BaseVariable.__init__(self, source, exclude)

        def _items(self, key, normalize=False):
            return ()

    import inspect

    class C(object):
        def __init__(self):
            self.x = 1
            self.y = 2
            self.z = 3

    def func():
        c_inst = C()
        d_inst = {'a': 1, 'b': 2, 'c': 3}
        l_inst = [1, 2, 3]
        m_inst = C()

        return c_inst, d_inst, l_inst, m_inst

    a, b, c, d = func()
    frame = inspect.stack()[1][0]



# Generated at 2022-06-12 20:03:17.722113
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('abc')
    v2 = BaseVariable('abc')
    assert v1 == v2

    v2 = BaseVariable('abc', exclude=('.'))
    assert v1 != v2

    class SubVar(BaseVariable):
        pass

    v2 = SubVar('abc')
    assert v1 != v2

# Generated at 2022-06-12 20:03:19.479364
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    base_variable = BaseVariable("print(1)")
    if base_variable.__eq__(base_variable) != True:
        return False
    return True


# Generated at 2022-06-12 20:03:23.755537
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', exclude=['b']) != BaseVariable('a')

# Generated at 2022-06-12 20:03:32.853706
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    test_cases = [
        {'source': 'a',
         'exclude': (),
         'expected_result': True},
        {'source': 'a',
         'exclude': ('b',),
         'expected_result': False},
        {'source': 'a',
         'exclude': ('b'),
         'expected_result': False}]
    for test_case in test_cases:
        test_case['source'] = BaseVariable(test_case['source'], test_case['exclude'])
    test_cases[0]['source1'] = BaseVariable('a', ())
    test_cases[1]['source1'] = BaseVariable('a', ('b',))
    test_cases[2]['source1'] = BaseVariable('a', ('b'))

# Generated at 2022-06-12 20:03:37.875121
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    #import inspect
    #frame_info = inspect.getouterframes(inspect.currentframe())
    frame_info = sys._getframe(1)
    #print(frame_info)
    frame = frame_info[0]
    frame_locals = frame.f_locals
    res = BaseVariable('a').items(frame)

    print('result =', res)



# Generated at 2022-06-12 20:03:48.002713
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import unittest

    class AttrDict(dict):
        def __getattr__(self, item):
            return self[item]

    class TestBaseVariable(unittest.TestCase):
        def setUp(self):
            class Base(object):
                def __init__(self):
                    self.dict = AttrDict(
                        {'a': 1, 'b': 2}
                    )
                    self.list = [1, 2, 3, 4]
                    self.tuple = (1, 2, 3, 4)

                def getdict(self):
                    return self.dict

                def getlist(self):
                    return self.list

                def gettuple(self):
                    return self.tuple

            self.frame = sys._getframe(1)
            self.show = Base()

# Generated at 2022-06-12 20:03:52.353123
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    v1 = BaseVariable('a', exclude=['b'])
    v2 = BaseVariable('a', exclude=('b',))
    assert v1==v2
    v3 = BaseVariable('a', exclude=['b'])
    assert v1==v3

# Generated at 2022-06-12 20:04:00.400978
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    import inspect
    frame_globals = sys._getframe(1).f_globals
    frame_locals = sys._getframe(1).f_globals
    # test a sample expression
    BaseVariable('2*2').items(frame_locals)
    # test a sample expression
    BaseVariable('Frame_locals').items(frame_locals)
    # test a sample expression
    BaseVariable('Frame_locals').items(frame_globals)
    # test a sample expression
    BaseVariable('Frame_locals.f_globals').items(frame_locals)
    # test a sample expression
    BaseVariable('Frame_locals.f_globals').items(frame_globals)
    # test a sample expression

# Generated at 2022-06-12 20:04:22.682824
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    obj_1 = BaseVariable('a')
    obj_2 = BaseVariable('b')
    obj_3 = BaseVariable('a')
    assert obj_1 == obj_3
    assert not obj_1 == obj_2
    assert not obj_2 == obj_3
    assert not obj_1 == 'not a BaseVariable'
    assert not obj_1 == None

# Generated at 2022-06-12 20:04:30.138103
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    """
        Test for method items of class BaseVariable
    """
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # normalize=True
    assert(list(Indices('l').items(sys._getframe(), normalize=True)) == [
       ('l[0]', '0'),
       ('l[1]', '1'),
       ('l[2]', '2'),
       ('l[3]', '3'),
       ('l[4]', '4'),
       ('l', '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
    ])

    # normalize=False

# Generated at 2022-06-12 20:04:34.744565
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    class AttrExample:
        def __init__(self, x):
            self.a = x
            self.b = x + 1
            self.c = x + 2
            self.d = x + 3
            self.e = x + 4
            self.f = x + 5
            self.g = x + 6
            self.h = x + 7
            self.i = x + 8
            self.j = x + 9
            self.k = x + 10
            self.l = x + 11
            self.m = x + 12
            self.n = x + 13
            self.o = x + 14
            self.p = x + 15

        def __getitem__(self, item):
            if item == 'q':
                return 'q'

# Generated at 2022-06-12 20:04:38.361941
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('i')
    b = BaseVariable('i')
    c = BaseVariable('i.a')
    assert (a == b) == True
    assert (a == c) == False


# Generated at 2022-06-12 20:04:48.377043
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    from . import globals
    from . import variables
    from . import function
    from . import builtins
    from . import frames

    locals = {'test_var': 1}

    frm = sys._getframe()
    assert variables.BaseVariable('test_var').items(frm) == [('test_var', '1')]
    assert variables.BaseVariable('test_var', ('test_var',)).items(frm) == []
    assert variables.BaseVariable('test_var', 'test_var').items(frm) == []
    assert variables.BaseVariable('test_var', tuple()).items(frm) == [('test_var', '1')]

# Generated at 2022-06-12 20:04:53.003135
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a=1
    b=2
    c=[1,2,3]
    s='hello'
    d={'k1':'v1','k2':'v2','k3':'v3'}
    source='d'
    test_obj=BaseVariable(source)
    res=test_obj.items(locals(),False)
    print(res)

# Generated at 2022-06-12 20:04:59.307009
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():

    class MyDict(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__slots__ = ['__dict__', '__slots__']

    frame = {'d': MyDict()}

    a = Attrs('a', ['__doc__'])
    b = Attrs('b', ['__doc__', '__dict__'])
    c = Keys('c', ['__doc__', '__dict__'])
    d = Indices('d', ['__doc__', '__dict__'])
    e = Indices('d[:3]', ['__doc__', '__dict__'])
    f = Exploding('d[:3]', ['__doc__', '__dict__'])
    g = Exploding

# Generated at 2022-06-12 20:05:07.942047
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    import sys
    f = Attrs('f')
    x = sys._getframe()
    y = f.items(x, True)
    y1 = dict(y)
    print(y1['f'].split('.')[-1]+'('+y1['f.__module__']+')')
    print('f.__dict__:'+y1['f.__dict__'])
    print('f.__name__:'+y1['f.__name__']+' '+'f.__doc__:'+y1['f.__doc__'])
    print('f.__self__:'+y1['f.__self__'])

if __name__ == '__main__':
    test_BaseVariable_items()

# Generated at 2022-06-12 20:05:17.833214
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .context import Context
    
    code = '''def fn1(x):
        return x*x
    def fn2(x):
        return fn1(x)
    '''
    frame = utils.eval_code(code, 'fn2', {'x':2})
    context = Context(frame)
    
    for normalize in [False, True]:
        context.normalize = normalize
        items = context._find_variables(['x'])
        if normalize:
            value = '2'
        else:
            value = 'x'
        assert items['x'] == value
        
        items = context._find_variables(['x', '$x'])
        assert items['x'] == value and '$x' not in items


# Generated at 2022-06-12 20:05:29.994371
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    global_dict = {'name': 'value'}
    local_dict = {'local_name': 'local_value'}
    frame = type('frame', (object,), {'f_locals': local_dict, 'f_globals': global_dict})()

    variable = BaseVariable('name')
    result = list(variable.items(frame))
    assert result == [('name', repr('value'))]

    variable = BaseVariable('names.name')
    result = list(variable.items(frame))
    assert result == [('names.name', repr('value'))]

    variable = BaseVariable('names.name', ('name'))
    result = list(variable.items(frame))
    assert result == [('names.name', repr('value'))]


# Generated at 2022-06-12 20:06:10.706324
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = BaseVariable('request.user', 'request')
    assert var1 == var1

    var2 = BaseVariable('request.user', 'request')
    assert var1 == var2

    var3 = Attrs('request.user', 'request')
    assert var3 == var1

    var4 = BaseVariable('request.user', 'request')
    assert var4 == var3

    var5 = Attrs('request.user2', 'request')
    assert var5 != var3

    var6 = BaseVariable('request.user', 'request')
    assert var6 == var5


# Generated at 2022-06-12 20:06:12.150852
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
   assert BaseVariable("a") == BaseVariable("a")
   assert not BaseVariable("a") == BaseVariable("b")

# Generated at 2022-06-12 20:06:19.407696
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    a = 5
    b = 3
    c = {'key':123, 'other_key':345, 'excluded':456}
    d = 'test string'
    e = {'key1':{'key2': 1, 'key3': 2}, 'key4': 2}
    frame = inspect.currentframe()
    v = BaseVariable('a')
    assert v.items(frame, normalize=False) == ('a', '5')
    assert v.items(frame, normalize=True) == ('a', '5')
    assert v.items(frame) == ('a', '5')
    v = BaseVariable('b')
    assert v.items(frame, normalize=False) == ('b', '3')
    assert v.items(frame, normalize=True) == ('b', '3')
    assert v

# Generated at 2022-06-12 20:06:25.214214
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    class A(BaseVariable):
        pass

    assert BaseVariable('foo') == BaseVariable('foo')
    assert BaseVariable('foo', 'bar') == BaseVariable('foo', 'bar')
    assert BaseVariable('foo', ('bar', 'baz')) == BaseVariable('foo', ('bar', 'baz'))
    assert BaseVariable('foo', 'bar') != BaseVariable('foo', 'bar', 'baz')
    assert BaseVariable('foo') != BaseVariable('foo', 'bar')
    assert BaseVariable('foo') != A('foo')
    assert BaseVariable('foo') != 1

# Generated at 2022-06-12 20:06:29.265701
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    var1 = CommonVariable("var1")
    var2 = CommonVariable("var2")
    # var1 and var2 should be different
    assert var1 != var2
    var3 = CommonVariable("var1")
    # but var1 and var3 should be equal
    assert var1 == var3
    # var3 and var2 should still be different


# Generated at 2022-06-12 20:06:35.207425
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    code = compile("d", '<variable>', 'eval')
    assert code.co_code == compile("d.x", '<variable>', 'eval').co_code
    assert compile("(d).x", '<variable>', 'eval').co_code == compile("(d.x).x", '<variable>', 'eval').co_code



# Generated at 2022-06-12 20:06:40.848026
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    assert BaseVariable('a') == BaseVariable('a')
    assert BaseVariable('a') != BaseVariable('b')
    assert BaseVariable('a', 'b') == BaseVariable('a', 'b')
    assert BaseVariable('a', 'b') != BaseVariable('a', 'c')
    assert BaseVariable('a') == Attrs('a')
    assert BaseVariable('a') != Attrs('b')

# Generated at 2022-06-12 20:06:45.402220
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    from inspect import currentframe
    frame = currentframe()
    a = Keys('x')
    b = Keys('x')
    c = Attrs('x')
    d = Keys('y')
    assert a == b
    assert b == a
    assert a != c
    assert c != a
    assert a != d
    assert d != a
    a_items = a.items(frame)
    b_items = b.items(frame)
    c_items = c.items(frame)
    d_items = d.items(frame)
    assert a_items == b_items
    assert b_items == a_items
    assert a_items != c_items
    assert c_items != a_items
    assert a_items != d_items
    assert d_items != a_items


# Generated at 2022-06-12 20:06:49.184098
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    code = compile('test', '<test>', 'eval')
    source = 'test'
    var = BaseVariable(code, source, '')
    assert var.items('test') == []

# Unit tests for method items and _items of class CommonVariable

# Generated at 2022-06-12 20:06:54.831696
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    a = BaseVariable('a', 'c')
    b = BaseVariable('a', 'c')
    assert a == b
    a.source = 'b'
    assert a != b
    a.source = 'a'
    a.exclude = ('b',)
    assert a != b
    a.exclude = ('c',)
    assert a != b
    b = object()
    assert a != b
    b = object.__new__(Attrs)
    assert a != b
    b.source = 'a'
    b.exclude = ('c',)
    assert a != b


# Generated at 2022-06-12 20:08:10.050947
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    # Test Function
    def test_BaseVariable(self, source, exclude, f_globals, f_locals, expected):
        bv = BaseVariable(source, exclude)
        # Create a mock frame
        frame = Mock()
        frame.f_locals = f_locals
        frame.f_globals = f_globals
        # Call method items of bv
        result = bv.items(frame)
        # Test result
        self.assertEqual(result, expected)

    # Test Classes
    class Test(TestCase):
        def test_A(self):
            test_BaseVariable(self, 'x', [], {'x': 2}, {}, [('x', 2)])


# Generated at 2022-06-12 20:08:19.126052
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    """
    Test for the method __eq__ of class BaseVariable
    """
    from . import variables
    from . import utils
    # First test when the given objects are not of the same class
    test_variable1 = variables.BaseVariable('a')
    test_variable2 = variables.Variable('a')
    assert not test_variable1.__eq__(test_variable2)
    # Then when the given objects are of the same class
    test_variable1 = variables.BaseVariable('a')
    test_variable2 = variables.BaseVariable('b')
    assert not test_variable1.__eq__(test_variable2)
    test_variable1 = variables.BaseVariable('a')
    test_variable2 = variables.BaseVariable('a')
    assert test_variable1.__eq__(test_variable2)
    # Then

# Generated at 2022-06-12 20:08:23.018783
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():
    from .test_utils import setup_testcase
    setup_testcase()
    
    import sys

    # Test case 1:
    # - declare a BaseVariable object
    # - call the method items on it
    # - assert the output
    v = BaseVariable('sys')
    assert v.items(sys._getframe()) == [('sys', "'sys' (built-in module)")]



# Generated at 2022-06-12 20:08:24.550162
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    print(BaseVariable.__eq__(BaseVariable('Hello'), BaseVariable('Hello')))

# Generated at 2022-06-12 20:08:31.596039
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # Case 1: Two different class objects
    var1 = Exploding("var1")
    var2 = Attrs("var2")
    print("Case 1: Two different class objects")
    print("Is var1 the same class object as var2?", var1 == var2)
    print("------------------------------------------------------------------")

    # Case 2: Two different source objects
    var3 = Exploding("var3")
    var4 = Exploding("var4")
    print("Case 2: Two different source objects")
    print("Is var3 from the same source as var4?", var3 == var4)
    print("------------------------------------------------------------------")

    # Case 3: Two different exclude objects
    var5 = Exploding("var5", exclude=("e1", "e2"))
    var6 = Exploding("var6", exclude=("e3", "e4"))

# Generated at 2022-06-12 20:08:41.792017
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():
    # As BaseVariable is an abstract class, this test is done on its subclasses
    # CommonVariable
    var1 = CommonVariable('a')
    var2 = CommonVariable('a')
    assert var1 == var2

    # Keys
    var3 = Keys('a')
    assert var3 == var2
    assert not var1 == var3

    # Indices
    var4 = Indices('a')
    assert var4 == var2
    assert var4 == var3
    assert not var1 == var4

    # Attrs
    var5 = Attrs('a')
    assert var5 == var2
    assert var5 == var3
    assert var5 == var4
    assert not var1 == var5

    # Exploding
    var6 = Exploding('a')
    assert var6 == var2
    assert var6 == var