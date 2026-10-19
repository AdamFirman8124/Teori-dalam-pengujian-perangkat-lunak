

# Generated at 2022-06-13 20:05:29.041395
# Unit test for function no_map_instance
def test_no_map_instance():
    c1 = [1, 2, 3]
    c2 = [4, 5, 6]
    c1 = no_map_instance(c1)
    c2 = no_map_instance(c2)
    c_new = map_structure(lambda x: 2*x, [c1, c2])
    assert all(x == y for x, y in zip(c_new, [c1, c2]))

# Generated at 2022-06-13 20:05:31.275323
# Unit test for function no_map_instance
def test_no_map_instance():
    x = no_map_instance(["1"])
    print(x)

if __name__ == "__main__":
    test_no_map_instance()

# Generated at 2022-06-13 20:05:39.294584
# Unit test for function map_structure_zip
def test_map_structure_zip():
    list_of_list = [[1, 2, 3], [4, 5, 6]]
    assert map_structure_zip(lambda x, y: x + y, list_of_list) == [5, 7, 9]

    list_of_dict = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    assert map_structure_zip(lambda x, y: x + y, list_of_dict) == {"a": 4, "b": 6}

    list_of_dict = [{"a": 1, "b": 2}, {"a": 3, "c": 4}]
    assert map_structure_zip(lambda x, y: x + y, list_of_dict) == {"a": 4, "b": 2, "c": 4}

test_map_structure

# Generated at 2022-06-13 20:05:45.679088
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = {
        "a": 1,
        "b": [1, 2, 3],
        "c": ["a", "b", "c"]
    }

    b = {
        "a": 2,
        "b": [4, 5, 6],
        "c": ["x", "y", "z"]
    }

    ans = map_structure_zip(lambda x, y: x - y, [a, b])
    assert ans == {"a": -1, "b": [-3, -3, -3], "c": [0, 0, 0]}


if __name__ == '__main__':
    test_map_structure_zip()

# Generated at 2022-06-13 20:05:51.631847
# Unit test for function no_map_instance
def test_no_map_instance():
    test_list = [0,2,3,4]
    test_list_0 = no_map_instance(test_list)
    test_list_1 = no_map_instance(test_list)
    assert(test_list_0==test_list)
    assert(test_list_0!=test_list_1)

# Generated at 2022-06-13 20:06:01.198606
# Unit test for function no_map_instance
def test_no_map_instance():
    a = ['a', 'b', 'c']
    b = no_map_instance(a)
    c = no_map_instance(a)
    assert a == b
    assert a == c
    assert id(a) == id(b)
    assert id(b) == id(c)
    d = no_map_instance(['a', 'b', 'c'])
    assert a != d
    assert id(a) == id(d)
    e = no_map_instance([['a', 'b'], ['b', 'c']])
    assert a != e
    assert id(a) != id(e)
    assert e == d
    assert id(d) == id(e)


if __name__ == '__main__':
    test_no_map_instance()

# Generated at 2022-06-13 20:06:06.710749
# Unit test for function map_structure
def test_map_structure():
    def fn(x):
        return x * 2
    obj = [1, 2, 3, 4]
    assert map_structure(fn, obj) == [2, 4, 6, 8]
    obj = (1, 2, [3, 4])
    assert map_structure(fn, obj) == (2, 4, [6, 8])
    obj = {'a': 1, 'b': 2, 'c': [3, 4]}
    assert map_structure(fn, obj) == {'a': 2, 'b': 4, 'c': [6, 8]}
test_map_structure()

# Generated at 2022-06-13 20:06:17.741362
# Unit test for function map_structure
def test_map_structure():
    def f(x):
        return x + 1
    # dic
    dic = {
        'a': 1,
        'b': (1, 2),
        'c': [(2,3,4), 3, 4, 5],
        'd': {'t': 4}
    }
    assert map_structure(f, dic) == {
        'a': 2,
        'b': (2, 3),
        'c': [(3,4,5), 4, 5, 6],
        'd': {'t': 5}
    }
    # list
    assert map_structure(f, [1, 2, 3, 4]) == [2, 3, 4, 5]

    # tuple

# Generated at 2022-06-13 20:06:25.243378
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def test(a, b):
        return (a,b)
    s = [
        {
            "a": {
                "a": "a",
                "b": "b"
            },
            "b": {
                "a": "aa",
                "b": "bb"
            }
        },
        {
            "a": {
                "a": "aa",
                "b": "bb"
            },
            "b": {
                "a": "aaa",
                "b": "bbb"
            }
        }
    ]
    print(map_structure_zip(test, s))

# Generated at 2022-06-13 20:06:28.074557
# Unit test for function no_map_instance
def test_no_map_instance():
    list_obj = no_map_instance(['a','b','c'])
    assert list_obj == ['a','b','c']
    assert hasattr(list_obj, "--no-map--") == True
    assert hasattr(['a','b','c'], "--no-map--") == False


# Generated at 2022-06-13 20:06:40.892934
# Unit test for function no_map_instance
def test_no_map_instance():
  t = (1, 2, 3)
  x = no_map_instance(t)
  assert x == t
  assert x is not t

  t = [1, 2, 3]
  x = no_map_instance(t)
  assert x == t
  assert x is not t

  t = {1, 2, 3}
  x = no_map_instance(t)
  assert x == t
  assert x is not t
  
  t = {1:1, 2:2, 3:3}
  x = no_map_instance(t)
  assert x == t
  assert x is not t

# Generated at 2022-06-13 20:06:47.355097
# Unit test for function map_structure
def test_map_structure():
    a = {'a': 1, 'b': 2}
    b = [[1, 2, 3], (3, 4, 5)]
    def f(x):
        return x ** 2
    c = map_structure(f, a)
    print(c)
    d = map_structure(f, b)
    print(d)


# Generated at 2022-06-13 20:06:51.264093
# Unit test for function no_map_instance
def test_no_map_instance():
    @no_type_check
    def is_mappable(obj):
        try:
            getattr(obj, _NO_MAP_INSTANCE_ATTR)
            return False
        except AttributeError:
            return True
    
    map_structure(is_mappable, no_map_instance([[1], no_map_instance("2")]))

# Generated at 2022-06-13 20:07:02.982433
# Unit test for function no_map_instance
def test_no_map_instance():
    assert no_map_instance(list()) == no_map_instance(list())
    assert no_map_instance([1]) == no_map_instance([1])
    assert no_map_instance([1, 2]) == no_map_instance([1, 2])
    assert no_map_instance([1, 2]) != no_map_instance([1])
    assert no_map_instance(set()) == no_map_instance(set())
    assert no_map_instance({1}) == no_map_instance({1})
    assert no_map_instance({1, 2}) == no_map_instance({1, 2})
    assert no_map_instance({1, 2}) != no_map_instance({1})
    assert no_map_instance(tuple()) == no_map_instance(tuple())
    assert no_map

# Generated at 2022-06-13 20:07:13.043675
# Unit test for function map_structure
def test_map_structure():
    def test_fn(x):
        return 'test'

    obj = [1,2,3,4]
    mapped_obj = map_structure(test_fn, obj)
    assert(mapped_obj == ['test', 'test', 'test', 'test'])

    obj2 = {'1':1, '2':2, '3':3}
    mapped_obj2 = map_structure(test_fn, obj2)
    assert(mapped_obj2 == {'1':'test', '2':'test', '3':'test'})

    obj3 = (1, 2, 3, 4)
    mapped_obj3 = map_structure(test_fn, obj3)
    assert(mapped_obj3 == ('test', 'test', 'test', 'test'))


# Generated at 2022-06-13 20:07:16.412822
# Unit test for function map_structure_zip
def test_map_structure_zip():
    first = [[1, 2, 3]]
    second = [[4, 5, 6]]
    third = map_structure_zip(lambda x, y: x + y, first, second)
    assert(third == [[5, 7, 9]])

# Generated at 2022-06-13 20:07:18.036563
# Unit test for function no_map_instance
def test_no_map_instance():
    assert no_map_instance([]) == [] and no_map_instance(()) == ()



# Generated at 2022-06-13 20:07:28.921895
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # map_structure_zip tests
    obj1 = [{'a': [1, 2, 3], 'b': (4, 5)}, [{'c': 6}]]
    obj2 = [{'a': [2, 3, 4], 'b': (5, 6)}, [{'c': 7}]]
    obj3 = [{'a': [3, 4, 5], 'b': (6, 7)}, [{'c': 8}]]
    obj4 = [{'a': [4, 5, 6], 'b': (7, 8)}]
    obtained = map_structure_zip(lambda x, y, z, w: x + y + z + w, [obj1, obj2, obj3, obj4])

# Generated at 2022-06-13 20:07:33.973363
# Unit test for function map_structure_zip
def test_map_structure_zip():
    obj1 = [1, 2, 3]
    obj2 = [4, 5, 6]
    result = map_structure_zip(lambda x, y: x + y, [obj1, obj2])
    assert(result == [5, 7, 9])

    obj1 = {'A': 1, 'B': 2}
    obj2 = {'A': 4, 'B': 5}
    result = map_structure_zip(lambda x, y: x + y, [obj1, obj2])
    assert(result == {'A': 5, 'B': 7})

# Generated at 2022-06-13 20:07:44.046485
# Unit test for function map_structure_zip
def test_map_structure_zip():
    test = [
        [
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [10, 11, 12]]
        ],
        [
            [[13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24]]
        ]
    ]

    def fn(*x):
        return sum(x)

    result = map_structure_zip(fn, test)
    assert result == [[[1, 2, 3], [4, 5, 6]], [[13, 14, 15], [16, 17, 18]], [[7, 8, 9], [10, 11, 12]],
                      [[19, 20, 21], [22, 23, 24]]]

# Generated at 2022-06-13 20:07:59.849504
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test function with 2 nested Lists
    def add_list(x, y):
        return [x[0] + y[0], x[1] + y[1]]

    # Test function with 2 nested Lists
    def add_list_list(x, y):
        return [[x[0][0] + y[0][0], x[0][1] + y[0][1]],
                [x[1][0] + y[1][0], x[1][1] + y[1][1]]]

    # Test function with 2 nested Tuples
    def add_tuple(x, y):
        return (x[0] + y[0], x[1] + y[1])

    # Test function with 2 nested Tuples

# Generated at 2022-06-13 20:08:04.705062
# Unit test for function map_structure

# Generated at 2022-06-13 20:08:19.940161
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import torch
    from torch.autograd import Variable
    from torch.nn.modules.batchnorm import _BatchNorm
    from torch.nn.modules.conv import _ConvNd
    from torch.nn.modules.pooling import _MaxPoolNd
    from torch.nn.modules.linear import _Linear
    from torch.nn.modules.module import Module
    from torch.nn import functional as F
    from torch.nn.modules.loss import _Loss
    from torch.autograd import Function
    from torch.autograd.function import once_differentiable
    from torch.nn.utils import spectral_norm

    class _FunctionLinear(Function):
        @staticmethod
        def forward(ctx, input, weight, bias=None):
            output = input.mm(weight.t())

# Generated at 2022-06-13 20:08:28.253803
# Unit test for function map_structure
def test_map_structure():
    a_list = [[[1,2]],[[3,4]],[[5,6]]]
    a_dict = {'a':1, 'b':2, 'c':3}
    a_tuple = ([4,5], [6,7])
    a_nested_list = [[a_list,a_dict,a_tuple],[a_list,a_dict,a_tuple]]
    a_nested_dict = {'a':a_list, 'b':a_dict, 'c':a_tuple}
    a_nested_tuple = (a_list, a_dict, a_tuple)
    a_set = {1,2,3}
    
    def add_two(x):
        return x+2

# Generated at 2022-06-13 20:08:34.428717
# Unit test for function map_structure_zip
def test_map_structure_zip():
    list_ = [(1,2), (2,1), (3,1)]
    list_ = [map_structure_zip(lambda x: x[0] + x[1], list_)]
    assert list_ == [[4, 4, 4]]

# Generated at 2022-06-13 20:08:43.589668
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import namedtuple
    from pprint import pprint

    def test_fn(a, b):
        a['sum'] = a['x']+b['z']
        b['sum'] = a['x']+b['z']
        return a, b

    d1 = {'x': 1, 'y': 2}
    d2 = {'x': 3, 'y': 4, 'z': 5}
    d3 = {'x': 6, 'y': 7}
    d4 = {'x': 8, 'y': 9, 'z': 9}
    l1 = [d1, d2]
    l2 = [d3, d4]
    l3 = [d1, d2]
    l4 = [d1, d2, d4]
    t1 = tuple(l1)

# Generated at 2022-06-13 20:08:53.058059
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import namedtuple
    from pprint import pprint
    from copy import copy,deepcopy
    Data = namedtuple("Data", "id, age, name, address")
    D = namedtuple("D", "data1, data2, data3")

    # test 1: Case: data1, data2, data3 are all different collection type
    data1 = [(1, 25, "Aditya", 4800), (2, 21, "Lohit", 4800), (3, 26, "Rakesh", 4801)]

# Generated at 2022-06-13 20:09:04.163322
# Unit test for function map_structure
def test_map_structure():
    # List
    assert map_structure(lambda x: x**2, [1, 2, 3]) == [1, 4, 9]
    # Tuple
    assert map_structure(lambda x: x**2, (1, 2, 3)) == (1, 4, 9)
    assert map_structure(lambda x: x**2, (1, 2)) == (1, 4)
    assert map_structure(lambda x: x**2, (1,)) == (1,)
    # Dict
    assert map_structure(lambda x: x**2, {"a": 1, "b": 2}) == {"a": 1, "b": 4}
    assert map_structure(lambda x: x**2, {"a": 1}) == {"a": 1}
    # Set

# Generated at 2022-06-13 20:09:15.815047
# Unit test for function map_structure
def test_map_structure():
    from collections import namedtuple
    import torch
    import torch.nn as nn
    from torch.autograd import Variable

    # Register some classes as non-mappable
    register_no_map_class(torch.Size)
    register_no_map_class(nn.Parameter)

    # Define some test instances
    TestCase = namedtuple('TestCase', ['name', 'input_structure'])

# Generated at 2022-06-13 20:09:27.055795
# Unit test for function map_structure
def test_map_structure():
    import unittest
    from collections import namedtuple

    from .dict_utils import tmap
    from .exceptions import AssertionError

    Point = namedtuple('Point', ['x', 'y'])
    NamedPoint = namedtuple('NamedPoint', ['x', 'y'])

    def is_point_instance(x):
        return isinstance(x, Point)

    def is_namedpoint_instance(x):
        return isinstance(x, NamedPoint)

    def is_point(x):
        return x == Point

    class IsPoint:
        def __eq__(self, other):
            return is_point_instance(other)

    class IsNamedPoint:
        def __eq__(self, other):
            return is_namedpoint_instance(other)


# Generated at 2022-06-13 20:09:34.798957
# Unit test for function no_map_instance
def test_no_map_instance():
    a = [1, 2, 3]
    assert no_map_instance(a) is a
    assert len(no_map_instance(a)) == 3
    assert len(no_map_instance(a).__dict__) == 0
    assert map_structure(lambda x: x+1, a) == [2, 3, 4]
    assert no_map_instance(a) is a
    assert len(no_map_instance(a)) == 3
    assert len(no_map_instance(a).__dict__) == 1
    assert map_structure(lambda x: x+1, a) == [1, 2, 3]
    assert no_map_instance(a) is a
    assert len(no_map_instance(a)) == 3
    assert len(no_map_instance(a).__dict__)

# Generated at 2022-06-13 20:09:38.639401
# Unit test for function map_structure_zip
def test_map_structure_zip():
    objs = [{1:'a', 2:'b'}, {1:'c', 2:'d'}]
    fn = lambda x, y: x+y
    result = map_structure_zip(fn, objs)
    assert(result == {1:'ac', 2:'bd'})

test_map_structure_zip()

# Generated at 2022-06-13 20:09:49.263318
# Unit test for function map_structure
def test_map_structure():
    list_tuple = [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
    dict_tuple = {'a': ('b', 'c'), 'd': ('e', 'f'), 'g': ('h', 'i')}
    list_dict = [{'a': 'b', 'c': 'd'}, {'e': 'f', 'g': 'h'}, {'i': 'j', 'k': 'l'}]
    dict_dict = {'a': {'b': 'c'}, 'd': {'e': 'f'}, 'g': {'h': 'i'}}
    str1 = 'abc'
    str2 = 'def'
    fn1 = lambda x: x + str1

# Generated at 2022-06-13 20:09:55.862004
# Unit test for function map_structure
def test_map_structure():
    def fn(x):
        return x + 1

    def test(obj):
        mapped = map_structure(fn, obj)
        mapped_manual = type(obj)((k, fn(v) if isinstance(v, int) else test(v) if isinstance(v, dict) else v) for k, v in obj.items())
        assert mapped == mapped_manual

    test({
        1: 2,
        3: {
            4: 5
        }
    })

    test({
        1: 2,
        3: {
            4: 5,
            6: 7
        }
    })

    test({
        1: 2,
        3: {
            4: 5,
            6: 7
        },
        8: 9
    })

# Generated at 2022-06-13 20:10:03.006057
# Unit test for function no_map_instance
def test_no_map_instance():
    assert no_map_instance([1, 2, 3]) == [[1, 2, 3]]
    assert no_map_instance((1, 2, 3)) == ((1, 2, 3),)
    assert no_map_instance({1, 2, 3}) == {1, 2, 3}
    assert no_map_instance({1: 1, 2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}


if __name__ == '__main__':
    test_no_map_instance()

# Generated at 2022-06-13 20:10:11.215823
# Unit test for function map_structure_zip
def test_map_structure_zip():
    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x},{self.y})"

    class Point3D(Point):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x},{self.y},{self.z})"


# Generated at 2022-06-13 20:10:15.367154
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def add(x: int, y: int) -> int:
        return x + y

    a = [1]
    b = [2]
    c = [add(a, b)]
    print(c)


if __name__ == '__main__':
    test_map_structure_zip()

# Generated at 2022-06-13 20:10:21.929409
# Unit test for function no_map_instance
def test_no_map_instance():
    lst = [1, 2, 3]
    dict_ = {'a': 1, 'b': 2}
    new_lst = no_map_instance(lst)
    new_dict = no_map_instance(dict_)
    assert new_lst == lst
    assert new_dict == dict_
    assert id(new_lst) != id(lst)
    assert id(new_dict) != id(dict_)



# Generated at 2022-06-13 20:10:35.537574
# Unit test for function no_map_instance
def test_no_map_instance():
    print("Test 1 - list")
    test_list = [[2, 3], [3, 4]]
    test_list = no_map_instance(test_list)
    test_list = [[2, 3], 4]
    print("Test 2 - set")
    test_set = {3, 4, 5}
    test_set = no_map_instance(test_set)
    test_set = {3, 4, 5, 6}
    print("Test 3 - tuple")
    test_tuple = (2, 3)
    test_tuple = no_map_instance(test_tuple)
    test_tuple = (2, 4)
    print("Test 4 - dict")
    test_dict = {'key1': {'key2': 4}, 'key3': 5}
    test_dict = no_map

# Generated at 2022-06-13 20:10:43.459606
# Unit test for function map_structure_zip
def test_map_structure_zip():
    obj1 = [0, 1, 2]
    obj2 = [1, 2, 3]
    obj3 = [2, 3, 4]
    objs = [obj1, obj2, obj3]
    obj4 = [4, 5, 6]
    objs_with_not_match_structure = [obj4, obj2, obj3]
    def add(x, y, z):
        return x + y + z
    result = map_structure_zip(add, objs)
    result2 = map_structure_zip(add, objs_with_not_match_structure)

# Generated at 2022-06-13 20:10:55.048564
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections.abc import MutableMapping
    from typing import Any
    import torch

    class A(MutableMapping):
        def __init__(self, data: Any):
            self.data = data

        def __len__(self) -> int:
            return len(self.data)

        def __getitem__(self, key: Any) -> Any:
            return self.data[key]

        def __setitem__(self, key: Any, value: Any) -> None:
            self.data[key] = value

        def __delitem__(self, key: Any) -> None:
            del self.data[key]

        def __iter__(self) -> Any:
            return iter(self.data)

    class B(A):
        pass

    class C(A):
        pass


# Generated at 2022-06-13 20:11:05.402456
# Unit test for function map_structure_zip
def test_map_structure_zip():
    build_mask_from_lengths = lambda lengths, batch_size: lengths.new(batch_size, max(lengths)).fill_(0)
    mask = build_mask_from_lengths(10, 32).type(torch.int32)
    tensor = torch.arange(100).view(2, 10, 5).type(torch.float32)
    fn = lambda tensor, mask: tensor[0]*mask[0] + tensor[1]*mask[1]
    output = map_structure_zip(fn, [tensor, mask])
    assert output.shape == (2,10)
    assert output[0].shape == (10,)
    assert output[1].shape == (10,)



# Generated at 2022-06-13 20:11:08.394168
# Unit test for function no_map_instance
def test_no_map_instance():
    import collections
    d = collections.OrderedDict({"1":1,"2":2,"3":3})
    d_no_map = no_map_instance(d)
    assert d_no_map == d
    assert d_no_map.__class__ not in _NO_MAP_TYPES

    l = [1,2,3]
    l_no_map = no_map_instance(l)
    assert l_no_map == l
    assert l_no_map.__class__ not in _NO_MAP_TYPES

test_no_map_instance()

# Generated at 2022-06-13 20:11:11.514834
# Unit test for function no_map_instance
def test_no_map_instance():
    for i in [list, tuple, dict]:
        assert len(no_map_instance([i()])) == 1

    # Make sure no_map_instance is idempotent
    assert len(no_map_instance([no_map_instance(dict())])) == 1



# Generated at 2022-06-13 20:11:16.454574
# Unit test for function no_map_instance
def test_no_map_instance():
    def add1(x):
        return x + 1

    a = [1, 2, 3, 4]
    a = no_map_instance(a)
    b = map_structure(add1, a)

    # Make sure that the entire list is added by 1
    assert (b == a)

    # Make sure that b is not a list
    assert (b.__class__ != list)



# Generated at 2022-06-13 20:11:22.613553
# Unit test for function no_map_instance
def test_no_map_instance():
    input_class = [{'a': 1, 'b': '2'}]
    data_class = input_class.copy()

    assert map_structure(lambda x: x, data_class) == input_class
    assert map_structure(lambda x: x + 1, data_class) == [{'a': 2, 'b': '21'}]

    data_class = no_map_instance(data_class)

    assert map_structure(lambda x: x, data_class) == data_class
    assert map_structure(lambda x: x + 1, data_class) == [{'a': 2, 'b': '21'}]
    return

# Generated at 2022-06-13 20:11:30.230269
# Unit test for function no_map_instance
def test_no_map_instance():
    import pytest
    # Test for a list
    lis = [1, 2, 3]
    lis_norecurse = no_map_instance(lis)
    res = map_structure(lambda x: -x, lis_norecurse)
    assert res == lis_norecurse
    # Test for a namedtuple
    class Struct(collections.namedtuple('Struct', 'a b')):
        pass
    s = Struct(1,2)
    s_norecurse = no_map_instance(s)
    res = map_structure(lambda x: -x, s_norecurse)
    assert res == s_norecurse
    # Test for a dictionary
    dic = {'a': 1, 'b': 2}
    dic_norecurse

# Generated at 2022-06-13 20:11:36.848070
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Implementation of this test function is directly tested in function: test_map_structure_zip_in_structs
    # This method is just a wrapper around that
    # This wrapper is needed to be able to test map_structure_zip from this file
    # (the method above is in a different file)
    from .structs import test_map_structure_zip_in_structs
    return test_map_structure_zip_in_structs()

# Generated at 2022-06-13 20:11:43.129012
# Unit test for function no_map_instance
def test_no_map_instance():
    a = no_map_instance(5)
    b = no_map_instance(5)
    c = no_map_instance([5,6])
    d = no_map_instance(c)
    assert hash(a) == hash(b)
    assert hash(c) == hash(d)
    assert hash(a) != hash(c)

if __name__ == "__main__":
    test_no_map_instance()

# Generated at 2022-06-13 20:11:52.515856
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections import namedtuple

    class ComplexTensor(list):
        def get_property(self):
            return "property"

    a = [no_map_instance({"a": 1}), {"b": 2}, namedtuple('Test', 'a b')(1, 3),
         no_map_instance(tuple(no_map_instance({"a": 1}))), no_map_instance(ComplexTensor([1, 2, 3]))]

    def test_func(a):
        return a


# Generated at 2022-06-13 20:11:59.081967
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = np.array([1,2,3])
    b = np.array([1,2,3])
    c = map_structure_zip(lambda a,b:a+b, [a,b])
    assert np.all(np.equal(c,np.array([2,4,6])))

# Generated at 2022-06-13 20:12:01.776618
# Unit test for function map_structure
def test_map_structure():
    def fn(a):
        # print(a)
        return a + "_haha"

    a = [1, 2, 3]
    assert map_structure(fn, a) == ["1_haha", "2_haha", "3_haha"]


# Generated at 2022-06-13 20:12:06.128467
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def fn(*xs):
        return sum(xs)

    obj1 = [1, 2, 3]
    obj2 = {'a': 1, 'b': 2, 'c': 3}
    obj3 = (1, 2, 3)
    objs = (obj1, obj2, obj3)

    assert map_structure_zip(fn, objs) == 6


# Generated at 2022-06-13 20:12:11.025202
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    from torch import Tensor
    from typing import Tuple

    def _test_instance(instance, expected):
        for fn in ("map_structure", "map_structure_zip"):
            result = globals()[fn](lambda x: x + 1, instance)
            assert result == expected

    _test_instance(no_map_instance(torch.tensor([1, 2])), [2, 3])
    _test_instance(
        no_map_instance((torch.tensor([1, 2]), torch.tensor([3, 4]))),
        (torch.tensor([2, 3]), torch.tensor([4, 5]))
    )

# Generated at 2022-06-13 20:12:17.611069
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import torch
    from transformers import BertTokenizer
    import numpy as np
    from collections import OrderedDict
    from torch.utils.data import Dataset, DataLoader
    import logging
    import argparse
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.INFO)

    class MyDataset(Dataset):
        def __init__(self, sentences):
            self.sentences = sentences
        def __getitem__(self, idx):
            return np.array(self.sentences[idx])
        def __len__(self):
            return len(self.sentences)



# Generated at 2022-06-13 20:12:30.834209
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # no nested structure
    assert map_structure_zip(lambda x,y: [x, y], [[1,2], [3,4]]) == [[[1,3], [2,4]]]

    # nested structure, depth = 2
    assert map_structure_zip(lambda x, y: [[x, x + 1], [y, y + 1]], [[1,2], [3,4]]) \
        == [[[[1, 2], [3, 4]], [[2, 3], [4, 5]]], [[[3, 4], [5, 6]], [[4, 5], [6, 7]]]]

    # nested structure, depth = 1

# Generated at 2022-06-13 20:12:32.518016
# Unit test for function no_map_instance
def test_no_map_instance():
    a = no_map_instance([1, 2, 3])
    print(a)

# Generated at 2022-06-13 20:12:42.704604
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections import OrderedDict
    from torch.autograd import Variable

    list_ = [1, 2, 3]
    list_ = no_map_instance(list_)
    dict_ = {"a": 1, "b": 2, "c": 3}
    dict_ = no_map_instance(dict_)
    order_dict_ = OrderedDict({"a": 1, "b": 2, "c": 3})
    order_dict_ = no_map_instance(order_dict_)
    tensor_ = Variable(torch.Tensor([1,2,3]))
    tensor_ = no_map_instance(tensor_)
    numpy_ = numpy.array([1,2,3])
    numpy_ = no_map_instance(numpy_)


# Generated at 2022-06-13 20:12:48.657703
# Unit test for function no_map_instance
def test_no_map_instance():
    register_no_map_class(list)
    x = no_map_instance(list([1, 2, 3]))
    assert(type(x) is not list)
    assert(x == list([1, 2, 3]))



# Generated at 2022-06-13 20:12:55.020963
# Unit test for function map_structure
def test_map_structure():
    obj = {
        "a": 1,
        "b": [
            {"c": 2, "d": 4,},
            {"c": 3, "d": 5,},
        ],
        "e": (1, 2, 3),
    }
    assert map_structure(lambda x: 2 * x, obj) == {
        "a": 2,
        "b": [
            {"c": 4, "d": 8,},
            {"c": 6, "d": 10,},
        ],
        "e": (2, 4, 6),
    }
    assert map_structure(lambda x: x, obj["b"]) == obj["b"]
    assert map_structure(lambda x: x, obj["b"][0]) == obj["b"][0]

# Generated at 2022-06-13 20:13:07.382910
# Unit test for function no_map_instance
def test_no_map_instance():
    class Sublist(list):
        def __init__(self, obj):
            super().__init__(obj)
    register_no_map_class(type(Sublist()))
    a = no_map_instance([1, 2, 3])
    b = no_map_instance(Sublist([1, 2, 3]))
    fn = lambda x: [0, x]
    result1 = map_structure(fn, a)
    result2 = map_structure(fn, b)
    print(result1)
    print(result2)

    assert result1 == [0, [1, 2, 3]]
    assert result2 == [0, [1, 2, 3]]


# Generated at 2022-06-13 20:13:18.383947
# Unit test for function no_map_instance
def test_no_map_instance():
    t = no_map_instance([3, 2, 1])
    assert t == [3, 2, 1]
    assert not hasattr(t, '__iter__')
    assert hasattr(t, _NO_MAP_INSTANCE_ATTR)
    t = no_map_instance((1, 2, 3))
    assert t == (1, 2, 3)
    assert not hasattr(t, '__iter__')
    assert hasattr(t, _NO_MAP_INSTANCE_ATTR)
    t = no_map_instance({'a': 1, 'b': 2, 'c': 3})
    assert t == {'a': 1, 'b': 2, 'c': 3}
    assert not hasattr(t, '__iter__')

# Generated at 2022-06-13 20:13:22.338977
# Unit test for function no_map_instance
def test_no_map_instance():
    a = no_map_instance([[0, 1, 2],[3, 4, 5]])
    assert a == [[0, 1, 2], [3, 4, 5]]
    b = map_structure(lambda o: o + 5, a)
    assert b == [[0, 1, 2], [3, 4, 5]]

# Generated at 2022-06-13 20:13:37.655142
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import numpy as np

    def fn(a, b):
        return [a, b]

    list_1 = [1, 2]
    list_2 = [1.0, 2.0]
    list_3 = [1.0, 2.0]

    assert map_structure_zip(fn, [list_1, list_2, list_3]) == [[1, 1.0, 1.0], [2, 2.0, 2.0]]

    np_1 = np.array(1.0)
    np_2 = np.array(2.0)
    np_3 = np.array(3.0)

    assert map_structure_zip(fn, [np_1, np_2, np_3]) == [np.array([1.0, 2.0, 3.0])]


# Generated at 2022-06-13 20:13:45.888956
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def fn(x: int, xs: Sequence[int]) -> int:
        return sum([x * y for y in xs])

    assert map_structure_zip(fn, ([0, 1, 2], [3, 4, 5])) == [0, 4, 10]
    assert map_structure_zip(fn, ([0, 1, 2], [3, 4, 5], [5, 4, 3])) == [0, 8, 24]

    def fn2(x: int, y: int, z: int) -> int:
        return x * y * z

    assert map_structure_zip(fn2, ([0, 1, 2], [3, 4, 5], [5, 4, 3])) == [0, 16, 30]

    from collections import namedtuple

# Generated at 2022-06-13 20:13:54.687479
# Unit test for function map_structure_zip
def test_map_structure_zip():
    ss = (1, "a", [1, 2])
    ss_dict = {"1":1, "2":"a", "3":[1, 2]}
    ts = (2, "b", [1, 3])
    ts_dict = {"1":2, "2":"b", "3":[1, 3]}
    def add(x, y):
        return x + y

    # Add two lists
    print(map_structure_zip(add, (ss,ts)))
    # Add two dictionaries
    print(map_structure_zip(add, (ss_dict,ts_dict)))

if __name__ == "__main__":
    test_map_structure_zip()

# Generated at 2022-06-13 20:14:05.584255
# Unit test for function map_structure
def test_map_structure():
    import random
    import functools
    random.seed(0)

    def random_function(x):
        return random.random()

    def random_list():
        return [random_list() for _ in range(random.randrange(0, 10))]

    def random_dict():
        return {str(i): random_list() for i in range(random.randrange(0, 10))}

    def random_namedtuple():
        return functools.namedtuple('X', range(5))(*random_list())

    def test_mapper(fn, *args):
        structure = random_list()
        mapped_structure = map_structure(fn, structure)
        if mapped_structure == structure:
            raise ValueError("map_structure did not map")

# Generated at 2022-06-13 20:14:12.131778
# Unit test for function map_structure_zip
def test_map_structure_zip():
    cp_list_list = [['a','b','c'],['d','e','f']]
    cp_list_dict = [{'a':'b','c':'d','e':'f'},{'g':'h','i':'j','k':'l'}]
    cp_dict_dict = [{'a':'b','c':'d','e':'f'},{'a':'g','c':'i','e':'k'}]
    cp_tuple_tuple = ([(1,2),(3,4)],[(5,6),(7,8)])

    fn_list_list = lambda x,y: [x+y]
    fn_list_dict = lambda x,y: [x[key] + y[key] for key in x]
    fn_

# Generated at 2022-06-13 20:14:23.092734
# Unit test for function map_structure_zip
def test_map_structure_zip():
    fn = lambda x, y : [x, y]
    assert map_structure_zip(fn, [[1, 2], [3, 4]]) == [[[1, 3], [2, 4]]]
    assert map_structure_zip(fn, [[1, 2], [3, 4], [5, 6]]) == [[[1, 3, 5], [2, 4, 6]]]
    assert map_structure_zip(fn, [[1, 2, 3], [4, 5, 6]]) == [[[1, 4], [2, 5], [3, 6]]]
    assert map_structure_zip(fn, [[1], [2]]) == [[[1], [2]]]
    # Test dict

# Generated at 2022-06-13 20:14:30.886645
# Unit test for function map_structure
def test_map_structure():
    input_dict = {'a':1, 'b':2, 'c':{'d':'a', 'e':'b'}, 'd': [1,2,3,4]}
    def my_func(x):
        return x+1
    output_dict = map_structure(my_func, input_dict)
    output_dict_gt = {'a':2, 'b':3, 'c':{'d':'a1', 'e':'b1'}, 'd': [2,3,4,5]}
    assert (output_dict == output_dict_gt)

if __name__ == "__main__":
    test_map_structure()

# Generated at 2022-06-13 20:14:47.808337
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def _test(fn1, fn2):
        from torch.nn.utils.rnn import pad_packed_sequence, pack_padded_sequence
        from torch.nn.utils.rnn import get_lengths_from_binary_sequence_mask
        from torch.nn.utils.rnn import get_packed_sequence_info
        from torch.nn.utils.rnn import get_set_rnn_hidden_state
        from torch.nn.utils.rnn import PackedSequence
        from torch.nn import LSTM

        lstm = LSTM(5, 3, batch_first=True)
        lstm_packed = LSTM(5, 3, batch_first=True, bidirectional=True)
        x = torch.randn(2, 3, 5)
        x_lengths = torch.rand

# Generated at 2022-06-13 20:14:55.929006
# Unit test for function map_structure
def test_map_structure():
    from collections import namedtuple
    #Test list
    nested_list = [1, 2, [3, 4]]
    f = lambda v: v+1
    mapped_list = map_structure(f, nested_list)

    assert mapped_list == [2, 3, [4, 5]]

    #Test tuple
    nested_tuple = (1, 2, (3, 4), [5, 6])
    f = lambda v: v+1
    mapped_tuple = map_structure(f, nested_tuple)

    assert mapped_tuple == (2, 3, (4, 5), [6, 7])

    #Test dict
    nested_dict = {'a': [1, 2], 'b': {'c': [3, 4], 'd': tuple([5, 6])}}

# Generated at 2022-06-13 20:15:05.887026
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def plus3_tuple(args):
        return sum(args) + 3

    def plus3_list(args):
        return sum(args) + 3

    def plus3_dict(args):
        return sum(args.values()) + 3

    tup = (1, (2, [3]))
    list = [1, [2, (3,)]]
    dict = {"a": 1, "b": {"c": (2,), "d": [3]}}
    output = (5, (6, [7]))
    print(map_structure_zip(plus3_tuple, (tup, tup, tup)) == output)

# Generated at 2022-06-13 20:15:13.701669
# Unit test for function map_structure
def test_map_structure():
    def fn(x):
        return x + 1

    # simple test
    assert map_structure(fn, [1, 2, 3]) == [2, 3, 4]

    # nested test
    assert map_structure(fn, [1, 2, [3, 4]]) == [2, 3, [4, 5]]

    # namedtuple test
    class TestNamedTuple(NamedTuple):
        a: int
        b: int

    namedtuple_test = TestNamedTuple(1, 2)
    assert map_structure(fn, namedtuple_test) == TestNamedTuple(2, 3)

# Generated at 2022-06-13 20:15:22.689035
# Unit test for function map_structure
def test_map_structure():
    # normal case
    def func(x: int) -> int:
        return x + 1
    a = [[1, [2, 3]], 4, {"a": 5, "b": [6, 7]}]
    assert(map_structure(func, a) == [[2, [3, 4]], 5, {"a": 6, "b": [7, 8]}])
    # set as leaf node
    b = [[1, {2, 3}], {4, 5}, {"a": 5, "b": [6, 7]}]
    assert(map_structure(func, b) == [[2, {3, 4}], {5, 6}, {"a": 6, "b": [7, 8]}])
    # normal case with namedtuple