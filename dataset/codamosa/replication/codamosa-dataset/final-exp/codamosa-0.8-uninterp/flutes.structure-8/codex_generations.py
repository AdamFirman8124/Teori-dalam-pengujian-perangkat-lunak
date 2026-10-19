

# Generated at 2022-06-13 20:05:23.878596
# Unit test for function no_map_instance
def test_no_map_instance():
    class MyList(list):
        pass

    l = MyList([1, 2])
    l1 = no_map_instance(l)
    print(l1)
    assert l1 == l



# Generated at 2022-06-13 20:05:30.510406
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    class MyList(list):
        pass
    l = MyList([1, 2, 3, 4])
    l = no_map_instance(l)
    assert (list(map(lambda x:x + 1, l)) == [2,3,4,5])
    class MyTuple(tuple):
        pass
    t = MyTuple([1, 2, 3, 4])
    t = no_map_instance(t)
    assert (list(map(lambda x:x + 1, t)) == [2,3,4,5])
    class MyDict(dict):
        pass
    d = MyDict({'a': 1 , 'b': 2})
    d = no_map_instance(d)
    d['c'] = 3
    assert ('c' in d)

# Generated at 2022-06-13 20:05:37.311431
# Unit test for function no_map_instance
def test_no_map_instance():
    class A(list):
        def __init__(self, *args):
            super(A, self).__init__(*args)
            self.foo = 'bar'
    register_no_map_class(list)
    a = A([1, 2, 3])
    b = no_map_instance(a)
    assert a[0] == b[0]
    assert id(a) == id(b)
    assert a.foo == b.foo

# Generated at 2022-06-13 20:05:40.187921
# Unit test for function no_map_instance
def test_no_map_instance():
    from nlplingo.struct import IntArray, IntPairArray

    # a_list = ['a', 'b', 'c']
    a_list = IntArray([1, 2, 3])
    a_list_ = no_map_instance(a_list)
    asse

# Generated at 2022-06-13 20:05:47.304258
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import numpy as np
    from copy import copy
    from collections import defaultdict

    NUM = 30
    NUM_EVENT = 5
    NUM_TARGET = 3
    NUM_EXAMPLE = 2
    NUM_RECORD = 2
    NUM_DIM = 2

    ###################################################################
    # Prepare for test_data
    ###################################################################
    np.random.seed(0)
    def make_objects(num_target, num_event, num_example, num_record, num_dim):
        objects = []

# Generated at 2022-06-13 20:05:58.802208
# Unit test for function map_structure
def test_map_structure():
    # For a non-nested collection
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b', 'c')
    sample_dict = {'a': 1, 'b': 2, 'c':3 }
    sample_set = {'a', 'b', 'c'}

    # For a simple nested collection
    sample_nested_list = [[1,2],[2,3],[3,4]]
    sample_nested_tuple = (('a',1), ('b',2), ('c',3))
    sample_nested_dict = {'a': {'d':1, 'e':2}, 'b':{'d':3, 'e':4}, 'c': {'d':5, 'e':6}}

    # For an arbitrarily nested collection
    # Only supports cases

# Generated at 2022-06-13 20:06:05.458716
# Unit test for function map_structure_zip
def test_map_structure_zip():
    d = {'a': 1, 'b': torch.tensor(1.0), 'c': {'d': 123, 'e': 321}, 'f': [1, 2, 3],
        'g': [1, torch.tensor(2.0), 3], 'h': [torch.tensor(1.0), 2, 3]}
    d2 = {'a': 2, 'b': torch.tensor(2.0), 'c': {'d': 1, 'e': -1}, 'f': [1, 2, 3],
        'g': [1, torch.tensor(2.0), 3], 'h': [torch.tensor(1.0), 2, 3]}
    d_new = map_structure_zip(lambda x, y: x - y, [d, d2])

# Generated at 2022-06-13 20:06:16.604954
# Unit test for function no_map_instance
def test_no_map_instance():
    import sys
    # check for Python 3.8+
    if sys.version_info < (3, 8):
        return
    from dataclasses import dataclass
    from torch import nn
    from torch.nn import functional as F
    @dataclass
    class Instance:
        list_: list
        list2: list
        dict_: dict
        tuple_: tuple
        tuple2: tuple
        named_tuple: nn.utils.rnn.PackedSequence

# Generated at 2022-06-13 20:06:26.062772
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = OrderedDict()
    a['a'] = OrderedDict()
    a['a']['a'] = 1
    a['a']['b'] = 2
    a['b'] = OrderedDict()
    a['b']['a'] = 3
    a['b']['b'] = 4
    b = OrderedDict()
    b['a'] = OrderedDict()
    b['a']['a'] = 5
    b['a']['b'] = 6
    b['b'] = OrderedDict()
    b['b']['a'] = 7
    b['b']['b'] = 8
    result = map_structure_zip(lambda x, y: x + y, [a, b])
    print(result)


# Generated at 2022-06-13 20:06:30.853245
# Unit test for function map_structure
def test_map_structure():
    a = [{"a": 1, "b": 2}, {"c": 3}, {"d": 4}]
    b = map_structure(lambda x: x, a)
    assert a == b

if __name__ == "__main__":
    test_map_structure()

# Generated at 2022-06-13 20:06:41.738390
# Unit test for function no_map_instance
def test_no_map_instance():
    import numpy as np
    arr = np.array([1, 2])
    arr2 = no_map_instance(arr)
    assert arr2 == arr

    from torch import rand
    rand1 = rand(5, 5)
    rand2 = no_map_instance(rand1)
    assert rand2 == rand1

# Generated at 2022-06-13 20:06:51.682241
# Unit test for function no_map_instance
def test_no_map_instance():
    from itertools import count
    from collections import Counter

    assert no_map_instance([1, 2, 3]) == [1, 2, 3]
    assert no_map_instance((1, 2, 3)) == (1, 2, 3)
    assert Counter(no_map_instance([1, 2, 3])) == Counter([1, 2, 3])
    assert Counter(no_map_instance([1, 2, 3])) == Counter(no_map_instance((1, 2, 3)))
    assert Counter(no_map_instance([1, 2, 3])) == Counter(no_map_instance((1, 2, 3,)))
    assert Counter(no_map_instance([1, 2, 3])) == Counter(no_map_instance(((1, 2, 3))))

    class C(list):
        pass

   

# Generated at 2022-06-13 20:07:03.009726
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    res = map_structure_zip(lambda x, y, z: x+y+z, a, b, c)
    assert res == [12, 15, 18]

    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    c = [[9, 10], [11, 12]]
    res = map_structure_zip(lambda x, y, z: x+y+z, a, b, c)
    assert res[0] == [15, 18]
    assert res[1] == [21, 24]

    a = ((1, 2), (3, 4))

# Generated at 2022-06-13 20:07:08.107598
# Unit test for function no_map_instance
def test_no_map_instance():
    no_map_instance([[1, 2], [1, 2]])
    no_map_instance({'a': 1, 'b': 2})
    no_map_instance({1, 2, 3})
    no_map_instance((1, ))
    no_map_instance((1, 2, 3))


if __name__ == '__main__':
    test_no_map_instance()

# Generated at 2022-06-13 20:07:18.193819
# Unit test for function no_map_instance
def test_no_map_instance():
    assert(no_map_instance(torch.Size([])) != no_map_instance([]) != no_map_instance(('',)))
    assert(no_map_instance(torch.Size([])) != no_map_instance([1]))
    assert(no_map_instance([]) != no_map_instance((1,)))
    assert(not isinstance(no_map_instance(torch.Size([]))[0], int))
    assert(not isinstance(no_map_instance([]), torch.Size))
    assert(not isinstance(no_map_instance(('',)), torch.Size))
    assert(len(no_map_instance(torch.Size([]))) == 0)
    assert(len(no_map_instance([])) == 0)

# Generated at 2022-06-13 20:07:24.153241
# Unit test for function map_structure_zip
def test_map_structure_zip():
    x = [{'b': [1, 2, 3], 'a': [0, 0, 0]}]
    y = [{'b': [0, 0, 0], 'a': [1, 2, 3]}]
    z = map_structure_zip(lambda xx, yy: xx + yy, x, y)
    assert z == [{'b': [1, 2, 3], 'a': [1, 2, 3]}]



# Generated at 2022-06-13 20:07:31.445088
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    from torch.nn import Module

    class MyModule(Module):
        def __init__(self, size):
            super(MyModule, self).__init__()
            self.size = no_map_instance(size)

        def extra_repr(self):
            return 'size={}'.format(self.size)

    obj = MyModule(torch.Size([5, 5]))
    assert (obj.size == torch.Size([5, 5])), "no_map_instance is not working"



# Generated at 2022-06-13 20:07:42.696320
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test for list
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    def fn(x, y, z):
        return x + y + z    
    mapped_list = map_structure_zip(fn, list_of_lists)
    print(mapped_list)
    assert mapped_list == [9, 12]
    # Test for tuple
    list_of_tuples = [(1, 2), (3, 4), (5, 6)]
    def fn(x, y, z):
        return x + y + z    
    mapped_tuple = map_structure_zip(fn, list_of_tuples)
    print(mapped_tuple)
    assert mapped_tuple == (9, 12)
    # Test for dict
    list_of_dict

# Generated at 2022-06-13 20:07:50.346549
# Unit test for function map_structure_zip
def test_map_structure_zip():
    list1 = [1, 2]
    list2 = [3, 4]
    def add(num1, num2):
        return num1 + num2

    assert(map_structure_zip(add, [list1, list2]) == [4, 6])
    list3 = [[5, 6], [7, 8]]
    list4 = [[9, 10], [11, 12]]
    assert(map_structure_zip(add, [list3, list4]) == [[14, 16], [18, 20]])
    dict1 = {'1' : list1, '2' : list2}
    dict2 = {'1' : list3, '2' : list4}

# Generated at 2022-06-13 20:08:03.031735
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Single element lists
    test_list_zipped = map_structure_zip(
        lambda l1, l2: [l1[0], l2[0]],
        [
            [1],
            [2],
        ],
    )
    assert test_list_zipped == [[1, 2]]

    # Multiple element lists
    test_list_zipped = map_structure_zip(
        lambda l1, l2: [l1[0], l2[0]],
        [
            [1, 3, 4],
            [2, 3, 5],
        ],
    )
    assert test_list_zipped == [[1, 2], [3, 3], [4, 5]]

    # Namedtuple
    from collections import namedtuple

# Generated at 2022-06-13 20:08:13.371826
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import torch
    net1 = torch.nn.Sequential(
        torch.nn.Linear(10, 20),
        torch.nn.ReLU(),
        torch.nn.Linear(20, 30),
    )
    net2 = torch.nn.Sequential(
        torch.nn.Linear(10, 20),
        torch.nn.ReLU(),
        torch.nn.Linear(20, 30),
    )

    print('1. net1 is same with net2:', torch.equal(net1, net2))
    for name, p1 in net1.named_parameters():
        print('(a)', name, p1.sum())
    for name, p2 in net2.named_parameters():
        print('(b)', name, p2.sum())


# Generated at 2022-06-13 20:08:23.888132
# Unit test for function map_structure_zip
def test_map_structure_zip():
    class A(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    a1 = {0: A(0, 0), 1: A(1, 1)}
    a2 = {0: A(11, 11), 1: A(12, 12)}
    a3 = {0: A(21, 21), 1: A(22, 22)}
    a4 = {0: A(31, 31), 1: A(32, 32)}
    a5 = {0: A(41, 41), 1: A(42, 42)}
    a6 = {0: A(51, 51), 1: A(52, 52)}
    a7 = {0: A(61, 61), 1: A(62, 62)}

# Generated at 2022-06-13 20:08:27.708903
# Unit test for function no_map_instance
def test_no_map_instance():
    num = no_map_instance(5)
    assert hasattr(num, _NO_MAP_INSTANCE_ATTR)

    list1 = [1, 2, 3, 4]
    list2 = no_map_instance(list1)
    assert hasattr(list2, _NO_MAP_INSTANCE_ATTR)
    assert list2 == list1


# Generated at 2022-06-13 20:08:44.196699
# Unit test for function map_structure
def test_map_structure():
    l1 = [1, [2, 3], 4]
    l2 = ["a", "b", "c", "d"]
    l3 = [6, 7, 8]
    d = {'a': 'A', 'b': {'c': 'C', 'd': 'D'}}

    def _do_map_structure(fn, *objs):
        return map_structure(fn, objs)

    assert _do_map_structure(lambda x: x, l1) == l1
    assert _do_map_structure(lambda x: x, d) == d

    assert _do_map_structure(lambda x, y: [x[0], y[0]], l1, l2) == [1, 'a']

# Generated at 2022-06-13 20:08:53.318081
# Unit test for function map_structure_zip
def test_map_structure_zip():
    assert map_structure_zip(lambda *x: x, [1, 2], [3, 4], [5, 6]) == [(1, 3, 5), (2, 4, 6)]
    assert map_structure_zip(lambda x: x, 1) == 1
    assert map_structure_zip(lambda x: x, no_map_instance(1)) == 1
    assert map_structure_zip(lambda x: x, [1]) == [1]
    assert map_structure_zip(lambda x: x, no_map_instance([1])) == [1]
    assert map_structure_zip(lambda x: x, [1], no_map_instance([2])) == [1]
    assert map_structure_zip(lambda *x: x, [1], [2]) == [(1, 2)]


# Generated at 2022-06-13 20:08:58.570359
# Unit test for function no_map_instance
def test_no_map_instance():
    obj = no_map_instance([[1,2,3]])
    assert(not hasattr(obj, _NO_MAP_INSTANCE_ATTR))

    obj = no_map_instance([no_map_instance(1)])
    assert(hasattr(obj[0], _NO_MAP_INSTANCE_ATTR))

# Generated at 2022-06-13 20:09:04.186315
# Unit test for function no_map_instance
def test_no_map_instance():
    li = [1, 2, [3, 4], no_map_instance([5, 6])]
    mapped_li = map_structure(lambda x: x + 10, li)
    assert mapped_li == [11, 12, [13, 14], [5, 6]]

    a = no_map_instance([1])
    b = no_map_instance([2, 3])
    mapped_ab = map_structure_zip(lambda x, y: x + y, [a, b])
    assert mapped_ab == [1, 2, 3]

# Generated at 2022-06-13 20:09:15.814690
# Unit test for function map_structure
def test_map_structure():
    def double(x):
        return 2 * x

    def check_all(fn, objs, target):
        print("1. level:")
        assert (fn(objs) == target)
        print("2. level:")
        assert (fn(objs) == target)
        assert (map_structure(double, objs) == target)

    objs = [1, 2, 3, 4]
    check_all(sum, objs, 10)

    objs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    check_all(sum, objs, [22, 26, 30])


# Generated at 2022-06-13 20:09:27.056367
# Unit test for function map_structure
def test_map_structure():
    def add_one(x):
        return x + 1

    test_dict = {
        "a": 1,
        "b": {
            "c": 2,
            "d": 3,
            "e": [1, 2, 3, {
                "f": 3,
                "g": ["i", 2, 3],
            }]
        }
    }

    test_dict_result = {
        "a": 2,
        "b": {
            "c": 3,
            "d": 4,
            "e": [2, 3, 4, {
                "f": 4,
                "g": ["i", 3, 4],
            }]
        }
    }

    assert (map_structure(add_one, test_dict) == test_dict_result)

# Generated at 2022-06-13 20:09:37.837325
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def test_fn(xs: int, x: int, y: int) -> int:
        return x + y

    test_list_a = [[1, 2], [3, 4]]
    test_list_b = [[2, 3], [4, 5]]
    test_list_c = [[3, 4], [5, 6]]
    test_result = [[6, 9], [12, 15]]

    test_tensor_a = torch.rand([2, 2])
    test_tensor_b = torch.rand([2, 2])
    test_tensor_c = torch.rand([2, 2])

    test_dict_a = {'a': [1, 2], 'b': [3, 4]}
    test_dict_b = {'a': [2, 3], 'b': [4, 5]}


# Generated at 2022-06-13 20:09:48.802079
# Unit test for function no_map_instance
def test_no_map_instance():
    from functools import reduce
    from operator import add
    a = [[1, 2], [3, 4], [5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    c = [[13, 14], [15, 16], [17, 18]]
    no_map = no_map_instance([a, b])
    expected = [190]
    assert map_structure_zip(reduce, [no_map, c]) == expected

# Generated at 2022-06-13 20:09:55.754310
# Unit test for function no_map_instance
def test_no_map_instance():
    # inputs
    a_list = [1,2,3]
    a_dict = {'a': 1, 'b': 2}

    # call function
    no_map_list = no_map_instance(a_list)
    no_map_dict = no_map_instance(a_dict)

    # tests
    assert not hasattr(no_map_list, _NO_MAP_INSTANCE_ATTR)
    assert not hasattr(no_map_dict, _NO_MAP_INSTANCE_ATTR)

    assert not hasattr(a_list, _NO_MAP_INSTANCE_ATTR)
    assert a_list is no_map_list
    assert not hasattr(a_dict, _NO_MAP_INSTANCE_ATTR)
    assert a_dict is no_map_dict

# Unit test

# Generated at 2022-06-13 20:09:59.494595
# Unit test for function no_map_instance
def test_no_map_instance():
    a = list([1, 2, 3])
    assert a == map_structure(lambda x: x + 1, a)
    assert no_map_instance(a) == map_structure(lambda x: x + 1, a)

# Generated at 2022-06-13 20:10:08.826713
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def inc(x): return x+1
    def sum3(x, y, z): return x + y + z
    # test list
    objs = [[1,2,3], [4,5,6], [7,8,9]]
    truth = [12, 15, 18]
    result = map_structure_zip(sum3, objs)
    assert result == truth
    
    # test tuple
    objs = [("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i")]
    truth = [("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i")]
    result = map_structure_zip(inc, objs)
    assert result == truth

    # test dict

# Generated at 2022-06-13 20:10:15.326050
# Unit test for function no_map_instance
def test_no_map_instance():
    assert no_map_instance('123')=='123'
    assert no_map_instance((1,2,3))==(1,2,3)
    #assert no_map_instance(set([1,2,3]))==set([1,2,3])
    assert no_map_instance({1,2,3})=={1,2,3}
    assert no_map_instance({1:1, 2:2, 3:3})=={1:1, 2:2, 3:3}

# Generated at 2022-06-13 20:10:25.570628
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [{0: 1, 1: 2}, {0: 1, 1: 2}]
    b = [{0: {0: 1, 1: 2}, 1: {0: 1, 1: 2}}, {0: {0: 1, 1: 2}, 1: {0: 1, 1: 2}}]
    c = [{0: {0: 1, 1: 2}, 1: {0: 1, 1: 2}}, {0: {0: 1, 1: 2}, 1: {0: 1, 1: 2}}]
    d = map_structure_zip(lambda x, y, z: x + y + z, a, b, c)
    print("map_structure_zip", a, b, c, "=", d)

# Generated at 2022-06-13 20:10:35.427760
# Unit test for function no_map_instance
def test_no_map_instance():
    from hypothesis import given
    from hypothesis.strategies import lists, integers, tuples

    @given(lists(integers()))
    def test_list(l):
        assert map_structure(lambda x: x*2, l) == [2*x for x in l]
        assert map_structure_zip(lambda x, y: x+y, (l, no_map_instance(l))) == l + l

    @given(tuples(integers(), integers()))
    def test_tuple(t):
        assert map_structure(lambda x: x*2, t) == tuple(x*2 for x in t)

# Generated at 2022-06-13 20:10:43.358571
# Unit test for function map_structure
def test_map_structure():
    # test case 1
    def func(x):
        return x + x
    a = [1, 2, 3, 4]
    b = map_structure(func,a)
    print(b)
    # test case 2
    def func2(a, b):
        return a + b
    a = [[1, 2], (3, 4)]
    b = map_structure_zip(func2, a)
    print(b)
    # test case 3
    a = [[1, 2], (3, 4)]
    b = map_structure(func2, a)
    print(b)

# Generated at 2022-06-13 20:10:53.459577
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections import namedtuple

    class MyList(list):
        def __init__(self, data):
            self.data = data

    def f(x):
        raise TypeError("This function should not be called")
    register_no_map_class(MyList)

    l = MyList([1, 2, 3])
    no_map_instance(l) == MyList([1, 2, 3])

    Ordered = namedtuple("ordered", "a b c")
    Ordered._fields = ("c", "b", "a")
    t = Ordered(1, 2, 3)
    no_map_instance(t) == Ordered(1, 2, 3)

    assert isinstance(map_structure(f, l), MyList)

# Generated at 2022-06-13 20:11:05.742960
# Unit test for function map_structure
def test_map_structure():
    import torch
    from collections import OrderedDict

    def test_function(x: float) -> float:
        return x * x

    def test_function_3args(x: float, y: float, z: float) -> float:
        return x + y + z

    # test for tuple
    d = (1, 2.0, 'a', torch.ones(3, 4), [1, 2.0, 'a', torch.ones(3, 4)], {1, 2.0, 'a', torch.ones(3, 4)}, OrderedDict({1: 1, 2.0: 2.0, 'a': 'a', torch.ones(3, 4): torch.ones(3, 4)}))

# Generated at 2022-06-13 20:11:17.972209
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import OrderedDict
    dict = OrderedDict([('a', 0), ('b', 1), ('c', 2)])
    d1 = dict
    d2 = OrderedDict([('a', 3), ('b', 4), ('c', 5)])
    d3 = OrderedDict([('a', 6), ('b', 7), ('c', 8)])
    lists = [d1, d2, d3]
    def func(x, y, z):
        return x + y + z
    o = map_structure_zip(func, lists)
    for k in o.keys():
        print(k, o[k])

# Generated at 2022-06-13 20:11:20.291179
# Unit test for function map_structure
def test_map_structure():
    examples = [1, "2", (3, 4), [5, 6], {"7": 8, 9: 10}]
    result = map_structure(lambda x: x + 1, examples)
    expected = [2, "21", (4, 5), [6, 7], {8: 9, 10: 11}]
    assert result == expected, f"expect {expected} but get {result}"


# Generated at 2022-06-13 20:11:31.145725
# Unit test for function map_structure
def test_map_structure():
    class TestClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    test_list = [1, 2, 3, 4]
    mapped_list = map_structure(lambda x: x + x, test_list)
    assert test_list != mapped_list
    for x, y in zip(test_list, mapped_list):
        assert x + x == y

    test_dict = {'a': 1, 'b': 2}
    mapped_dict = map_structure(lambda x: x + x, test_dict)
    assert test_dict != mapped_dict
    for key in test_dict:
        assert test_dict[key] + test_dict[key] == mapped_dict[key]

    test_tuple = (0, 1, 2)

# Generated at 2022-06-13 20:11:39.515822
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import namedtuple
    t1 = namedtuple("t1", "first second")
    t2 = namedtuple("t2", "third fourth")
    list1 = [1, [[2,3], 4], [5,6]]
    list2 = [7, [[8,9], 10], [11,12]]
    list3 = [13, [[14,15], 16], [17,18]]
    namedtuples = [t1(first = 1, second = t2(third = 2, fourth = 3)), t1(first = 4, second = t2(third = 5, fourth = 6))]
    namedtuples2 = [t1(first = 7, second = t2(third = 8, fourth = 9)), t1(first = 10, second = t2(third = 11, fourth = 12))]
    named

# Generated at 2022-06-13 20:11:50.420383
# Unit test for function map_structure_zip
def test_map_structure_zip():
    A = [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}]
    B = [{'id': 'a'}, {'id': 'b'}, {'id': 'c'}]
    C = [{'gender': 'm'}, {'gender': 'f'}, {'gender': 'f'}]
    D = [{'grade': '1'}, {'grade': '2'}, {'grade': '3'}]
    def func(*collections):
        a, b, c, d = collections
        assert len(a) == len(b) == len(c) == len(d) == 3

# Generated at 2022-06-13 20:11:55.638029
# Unit test for function map_structure
def test_map_structure():
    my_tuple = (
        [1,2,3],
        (1,
         {1: 'one', 2: 'two'},
         no_map_instance([{}]),
         no_map_instance(dict())
        )
    )

    def func_add_one(x):
        return x+1
    expected = (
        [2,3,4],
        (2,
         {2: 'two', 3: 'three'},
         no_map_instance([{}]),
         no_map_instance(dict())
        )
    )
    result = map_structure(func_add_one, my_tuple)
    assert result == expected


# Generated at 2022-06-13 20:11:59.427411
# Unit test for function no_map_instance
def test_no_map_instance():
  register_no_map_class(list)
  a = list()
  assert(hasattr(no_map_instance(a), _NO_MAP_INSTANCE_ATTR))

# Generated at 2022-06-13 20:12:03.030626
# Unit test for function no_map_instance
def test_no_map_instance():
    outer_container = []
    no_map_instance(outer_container).append(no_map_instance(['a', 'b']))
    outer_container.append(['c', 'd'])
    assert map_structure(lambda s: s.upper(), outer_container) == [['A', 'B'], ['C', 'D']]


if __name__ == '__main__':
    test_no_map_instance()

# Generated at 2022-06-13 20:12:10.901551
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test on singles
    ref = 2.
    values_list = [1., 2., 3.]
    fn = lambda x, y: x + y
    result = map_structure_zip(fn, values_list)
    assert(result == ref)
    # Test on list
    ref = [1., 2., 3.]
    values_list = [[1., 2., 3.], [2., 3., 4.], [3., 4., 5.]]
    fn = lambda x, y, z: x + y + z
    result = map_structure_zip(fn, values_list)
    assert(result == ref)
    # Test on tuple
    ref = (1., 2., 3.)
    values_list = [(1., 2., 3.), (2., 3., 4.), (3., 4., 5.)]

# Generated at 2022-06-13 20:12:14.828319
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    assert not hasattr(torch.Size([1,2,3]), _NO_MAP_INSTANCE_ATTR)
    assert hasattr(no_map_instance(torch.Size([1,2,3])), _NO_MAP_INSTANCE_ATTR)

if __name__ == '__main__':
    test_no_map_instance()

# Generated at 2022-06-13 20:12:39.852062
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Example 1:
    # Use map_structure_zip to map a function fn that takes two arguments to elements in two lists of lists of equal structure.
    # This example is taken from:
    # https://www.tensorflow.org/api_docs/python/tf/nest/map_structure_zip

    # 'fn' function to map over two lists of lists
    def multiply(x, y):
        return x * y

    # x and y are lists of lists of equal structure
    x = [[1, 2], [3, 4]]
    y = [[5, 6], [7, 8]]

    # with map_structure_zip, you can multiply the elements at each position of x and y
    # and output will be of the same shape as x and y

# Generated at 2022-06-13 20:12:46.881694
# Unit test for function no_map_instance
def test_no_map_instance():
    from abc import ABC, abstractmethod

    class Base(ABC):
        @abstractmethod
        def foo(self):
            pass

        @abstractmethod
        def bar(self):
            pass

        def __init_subclass__(cls):
            register_no_map_class(cls)

    class A(Base):
        def __init__(self, a: int) -> None:
            self.a = a

        def foo(self):
            return self.a

        def bar(self):
            return self.a * 2

    class B(Base):
        def __init__(self, b: float) -> None:
            self.b = b

        def foo(self):
            return self.b

        def bar(self):
            return self.b * 3


# Generated at 2022-06-13 20:12:54.380386
# Unit test for function no_map_instance
def test_no_map_instance():
    a = [1, 2, 3]
    assert map_structure(lambda x: x, a) == a
    a = no_map_instance(a)
    assert map_structure(lambda x: x, a) == a
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert map_structure(lambda x: x, a) == a
    a = no_map_instance(a)
    assert map_structure(lambda x: x, a) != a

# Generated at 2022-06-13 20:13:05.054178
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = {
        'id': 1,
        'name': 'king',
        'addr': {
            'city': 'beijing',
            'detail': 'jia',
        }
    }

    b = {
        'id': 2,
        'name': 'king2',
        'addr': {
            'city': 'beijing2',
            'detail': 'jia2',
        }
    }

    c = {
        'id': 3,
        'name': 'king3',
        'addr': {
            'city': 'beijing3',
            'detail': 'jia3',
        }
    }

    def fn(x, y, z):
        print(x, y, z)
        return (x, y, z)


# Generated at 2022-06-13 20:13:11.044781
# Unit test for function no_map_instance
def test_no_map_instance():
    l = no_map_instance([1, 2, 3])
    d = no_map_instance({"a": 1, "b": 2})
    t = no_map_instance(tuple([1, 2, 3]))
    assert(map_structure(lambda x: x + 1, l) == l)
    assert(map_structure(lambda x: x + 1, d) == d)
    assert(map_structure(lambda x: x + 1, t) == t)

# Generated at 2022-06-13 20:13:14.909896
# Unit test for function map_structure
def test_map_structure():
    x = {'a': [1, 2, 3], 'b': 2}
    y = map_structure(lambda v: type(v)(np.array(v)), x)
    print (y)

if __name__ == "__main__":
    test_map_structure()

# Generated at 2022-06-13 20:13:23.193280
# Unit test for function map_structure
def test_map_structure():
    import random
    import string
    import torch
    from itertools import product
    from functools import reduce

    def random_choice(xs):
        return xs[random.randint(0, len(xs) - 1)]

    def random_str(n):
        return ''.join(random.choice(string.ascii_letters) for _ in range(n))

    def random_item(n_types=2, n_shapes=2, n_lists=5, max_tensors=5):
        if n_types == 0:
            return torch.tensor(random.uniform(-1.0, 1.0))
        else:
            choice = random_choice('tensor', 'list', 'dict')

# Generated at 2022-06-13 20:13:38.653333
# Unit test for function no_map_instance
def test_no_map_instance():
    import numpy as np
    mylist = [1, 2, 3]
    mylist_no_map = no_map_instance(mylist)
    assert mylist_no_map is not mylist # the original list is preserved
    assert mylist_no_map == mylist # but it has the same content
    assert hasattr(mylist_no_map, _NO_MAP_INSTANCE_ATTR)
    mytuple = (4, 5, 6)
    mytuple_no_map = no_map_instance(mytuple)
    assert mytuple_no_map is not mytuple # the original list is preserved
    assert mytuple_no_map == mytuple # but it has the same content
    assert hasattr(mytuple_no_map, _NO_MAP_INSTANCE_ATTR)


# Generated at 2022-06-13 20:13:46.721856
# Unit test for function no_map_instance
def test_no_map_instance():
    a = no_map_instance(1)
    assert hasattr(a, _NO_MAP_INSTANCE_ATTR) and getattr(a, _NO_MAP_INSTANCE_ATTR)
    assert a == 1

    a = no_map_instance([1, 2, 3])
    assert hasattr(a, _NO_MAP_INSTANCE_ATTR) and getattr(a, _NO_MAP_INSTANCE_ATTR)
    assert a == [1, 2, 3]

    a = no_map_instance((1, 2, 3))
    assert hasattr(a, _NO_MAP_INSTANCE_ATTR) and getattr(a, _NO_MAP_INSTANCE_ATTR)
    assert a == (1, 2, 3)

    a = no_map_instance({1: 2, 3: 4})

# Generated at 2022-06-13 20:13:53.099661
# Unit test for function map_structure
def test_map_structure():
    import torch

    no_map_instance = torch.Size
    map_structure = torch.Size

    a = torch.Size(2)
    b = torch.Size(3)
    c = torch.Size(4)

    abc = [a, b, c]
    cba = [c, b, a]
    abc_abc = [abc, abc]
    abc_cba = [abc, cba]

    def sum_3(a, b, c):
        return a + b + c

    def sum_2_3(a, b):
        return a + b

    def sum_1_2_3(a):
        return a

    assert(map_structure(sum_3, abc) == no_map_instance(9))

# Generated at 2022-06-13 20:14:09.951837
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import OrderedDict
    d1 = OrderedDict()
    d1["a"] = 1
    d1["b"] = (1, 2, 3)
    d1[1] = [1, 2, 3]
    d1["d"] = {"a": 1, "b": 2, "c": 3}

    d2 = OrderedDict()
    d2["a"] = 11
    d2["b"] = (11, 22, 33)
    d2[1] = [11, 22, 33]
    d2["d"] = {"a": 11, "b": 22, "c": 33}

    d3 = OrderedDict()
    d3["a"] = 111
    d3["b"] = (111, 222, 333)

# Generated at 2022-06-13 20:14:16.308950
# Unit test for function no_map_instance
def test_no_map_instance():
    l = list(range(10))
    nl = no_map_instance(l)
    assert l == nl
    assert hasattr(nl, "--no-map--")

if __name__=='__main__':
    l = list(range(10))
    nl = no_map_instance(l)
    assert l == nl
    assert hasattr(nl, "--no-map--")

# Generated at 2022-06-13 20:14:27.070236
# Unit test for function map_structure
def test_map_structure():
    a = [[1, 2, 3], [[4], [5, 6]]]
    b = map_structure(lambda x: x + 2, a)
    assert b == [[3, 4, 5], [[6], [7, 8]]]
    a = {'a': [1, 2], 'b': [[4], [5, 6]]}
    b = map_structure(lambda x: x + 2, a)
    assert b == {'a': [3, 4], 'b': [[6], [7, 8]]}
    a = [[1, 2, 3], [[4], [5, 6]]]
    b = map_structure(lambda x, y: x + y, [a, a])
    assert b == [[2, 4, 6], [[8], [10, 12]]]

# Generated at 2022-06-13 20:14:31.283875
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    a = no_map_instance(torch.Size((1, 2, 3, 4)))
    assert(type(a) == torch.Size)
    assert(a == torch.Size((1, 2, 3, 4)))


if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

# Generated at 2022-06-13 20:14:42.294151
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch

    d = {'a': {'b': {1, 2, 3}}, 'c': 'd'}
    d['a']['b'] = no_map_instance(d['a']['b'])
    assert d == map_structure(lambda x: x, d)
    assert [1, 2, 3] == list(d['a']['b'])
    # Named tuple
    size = torch.Size((1, 2, 3, 4))
    size_instance = no_map_instance(size)
    assert size == map_structure(lambda x: x, size_instance)
    assert size_instance == map_structure_zip(lambda x, y: x, [size_instance, size])



# Generated at 2022-06-13 20:14:47.137865
# Unit test for function no_map_instance
def test_no_map_instance():
    # print("Start testing no_map_instance ...")
    l = [1, 2, 3]
    m = no_map_instance(l)
    assert m is not l
    # print("End testing no_map_instance ...")


# Generated at 2022-06-13 20:14:55.694564
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # basic test
    objs = [{'a':0, 'b':1, 'c':2, 'd':3, 'e':4}, {'a':5, 'b':6, 'c':7, 'd':8, 'e':9}]
    test_result = {'a': 5, 'b': 7, 'c': 9, 'd': 11, 'e': 13}
    assert map_structure_zip(lambda x, y: x+y, objs) == test_result

    # test tuple computation
    objs = [[(1,2,3), (4,5,6)], [(7,8,9), (10,11,12)]]
    test_result = [(8,10,12), (14,16,18)]

# Generated at 2022-06-13 20:15:05.854829
# Unit test for function no_map_instance
def test_no_map_instance():
    v = torch.as_tensor(10)
    v1 = no_map_instance(v)
    assert(v is v1)
    v2 = no_map_instance(torch.tensor(10))
    assert(v2.tolist() == 10)
    assert(v2 is not v)
    v3 = no_map_instance(10)
    assert(v3 == 10)
    assert(v3 is not v)

    v = torch.as_tensor(range(3))
    v1 = no_map_instance(v)
    assert(v is v1)
    v2 = no_map_instance(torch.tensor(range(3)))
    assert(v2.tolist() == [0, 1, 2])
    assert(v2 is not v)
    v

# Generated at 2022-06-13 20:15:14.261849
# Unit test for function map_structure
def test_map_structure():
    print(map_structure(lambda x:x, "a"))
    print(map_structure(lambda x:x, [1, 2]))
    print(map_structure(lambda x:x, (1, 2)))
    print(map_structure(lambda x:x, {"a": 1, "b": 2}))
    print(map_structure(lambda x:x, {1: "a", 2: "b"}))

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    print(map_structure(lambda x:x, Point(3, 4)))
