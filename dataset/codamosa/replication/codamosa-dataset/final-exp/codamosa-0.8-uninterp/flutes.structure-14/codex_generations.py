

# Generated at 2022-06-13 20:05:31.965944
# Unit test for function map_structure_zip
def test_map_structure_zip():
    l1 = [1,2,3]
    l2 = [2,3,4]
    l3 = [3,4,5]
    l_return = map_structure_zip(lambda x,y,z:x+y+z, [l1, l2, l3])
    assert(l_return == [6,9,12])

    d1 = {'a':5, 'b':6}
    d2 = {'a':5, 'b':7}
    d3 = {'a':5, 'b':8}
    d_return = map_structure_zip(lambda x,y,z:x+y+z, [d1, d2, d3])
    assert(d_return == {'a':15, 'b':21})

# Generated at 2022-06-13 20:05:33.724229
# Unit test for function no_map_instance
def test_no_map_instance():
    registered = no_map_instance([1, 2, 3])
    assert hasattr(registered, _NO_MAP_INSTANCE_ATTR)

# Generated at 2022-06-13 20:05:41.681832
# Unit test for function map_structure
def test_map_structure():
    from copy import copy
    from itertools import count
    from random import choice, randint, random, uniform
    from collections import OrderedDict
    from typing import NamedTuple

    def random_nested_list():
        l = []
        for _ in range(randint(0, 5)):
            if random() < 0.75:
                l.append(random_nested_list())
            else:
                l.append(randint(0, 100))
        return l

    def random_nested_dict():
        ks = [next(c) for _ in range(randint(0, 5))]
        d = OrderedDict()
        for k in ks:
            if random() < 0.75:
                d[k] = random_nested_dict()

# Generated at 2022-06-13 20:05:53.977779
# Unit test for function map_structure
def test_map_structure():

    # test for a list of ints
    ori_list = [1,2,3]
    new_list = map_structure(lambda x: x + 10, ori_list)
    assert ori_list == [1,2,3]
    assert new_list == [11,12,13]

    # test for a list of strings
    ori_list = ["1", "2", "3"]
    new_list = map_structure(lambda x: int(x) + 10, ori_list)
    assert ori_list == ["1", "2", "3"]
    assert new_list == [11, 12, 13]

    # test for a list of lists
    ori_list = [[1,2], [3,4]]
    new_list = map_structure(lambda x: x + 10, ori_list)


# Generated at 2022-06-13 20:05:58.239936
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def test_fn(first, second, third):
        return first, second, third

    a = {'a': 0, 'b': 1}
    b = {'a': 2, 'b': 3}
    c = {'a': 4, 'b': 5}

    a_b_c = map_structure_zip(test_fn, [a, b, c])

    print(a_b_c)

    assert a_b_c == {'a': (0, 2, 4), 'b': (1, 3, 5)}

# Generated at 2022-06-13 20:06:05.469962
# Unit test for function map_structure_zip
def test_map_structure_zip():
  class foo():
      def __init__(self, a, b):
          self.a = a
          self.b = b

  def fn(*args):
      print('args[0]: {}'.format(args[0]))
      print('args[1]: {}'.format(args[1]))
      return (args[0] +args[1])

  obj1 = foo(2, 3)
  obj2 = foo(4, 5)
  list_objs = [obj1, obj2]
  print(map_structure_zip(fn, list_objs))

if __name__== "__main__":
  test_map_structure_zip()

# Generated at 2022-06-13 20:06:16.645569
# Unit test for function map_structure_zip

# Generated at 2022-06-13 20:06:26.063400
# Unit test for function map_structure_zip
def test_map_structure_zip():
    d1 = {"first": 1, "second": 2}
    d2 = {"first": 10, "second": 20}
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]
    l3 = [3, 4, 5]
    d_sum = map_structure_zip(lambda a, b: a + b, [d1, d2])
    d_sum_expected = {"first": 11, "second": 22}
    # Make sure `d_sum` has the same type as `d1` and `d2`.
    assert isinstance(d_sum, type(d1))
    assert d_sum == d_sum_expected
    # Ensure that the function is working for iterables other than dicts.

# Generated at 2022-06-13 20:06:39.130405
# Unit test for function map_structure
def test_map_structure():
    class SubclassList(list):
        pass

    class SubclassDict(dict):
        pass

    def double(x):
        return 2 * x

    def add(x, y):
        return x + y

    # assert map_structure(double, [1, 2, 3]) == [2, 4, 6]
    # assert map_structure((lambda x: 2 * x), [1, 2, 3]) == [2, 4, 6]
    # assert map_structure(double, (1, 2, 3)) == (2, 4, 6)
    # assert map_structure(double, {1: 10, 2: 20, 3: 30}) == {1: 20, 2: 40, 3: 60}
    # assert map_structure(double, {1: 10, 2: 20, 3: 30}) == {

# Generated at 2022-06-13 20:06:47.762957
# Unit test for function no_map_instance
def test_no_map_instance():
    class MyList(list):
        def __init__(self):
            super(MyList, self).__init__([1,2,3])
    
    l = MyList()
    new_l = no_map_instance(l)
    print(new_l)
    print(l)
    print(new_l[1])
    print(type(l) is type(new_l))
    print(type(l) is not type(new_l))
    print(l is new_l)
    print(l == new_l)
    
    
test_no_map_instance()

# Generated at 2022-06-13 20:06:54.983030
# Unit test for function no_map_instance
def test_no_map_instance():
    l = [1, 2, 3, 4]
    no_map_type = no_map_instance(l)
    assert(isinstance(no_map_type, no_map_instance.cache_info().currsize))

# Generated at 2022-06-13 20:07:04.574837
# Unit test for function map_structure_zip
def test_map_structure_zip():

    def structure_zip_test_function(a, b):
        return a + b

    # 1. Testing standard list
    test_list = [[0, 1], [2, 3]]
    assert(map_structure_zip(structure_zip_test_function, test_list) == [[0, 2], [1, 3]])

    # 2. Testing standard tuple
    test_tuple = ((0, 1), (2, 3))
    assert(map_structure_zip(structure_zip_test_function, test_tuple) == ((0, 2), (1, 3)))

    # 3. Testing standard dict
    test_dict = {'a': [0, 1], 'b': [2, 3]}

# Generated at 2022-06-13 20:07:11.688104
# Unit test for function map_structure_zip
def test_map_structure_zip():
    class CustomObject:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class CustomObject2:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    def test(x: float, y: float) -> float:
        return x + y

    a = [1, 2, 3]
    b = [4, 5, 6]
    actual = map_structure_zip(test, [a, b])
    expected = [5, 7, 9]
    assert actual == expected

    a = {'a': 1, 'b': 2, 'c': 3}
    b = {'a': 4, 'b': 5, 'c': 6}

# Generated at 2022-06-13 20:07:14.689218
# Unit test for function map_structure
def test_map_structure():
    def fn(x):
        return x + 1
    test = list(map_structure(fn, [(1, 2), (3, 4, 5)]))
    print(test)

test_map_structure()

# Generated at 2022-06-13 20:07:22.165095
# Unit test for function map_structure
def test_map_structure():
    a = [[1, 2], [[1, 2], [1, 2]]]
    b = [2, 3]
    c = [{"a": 1}, {"b": 2}]
    d = [[1], [2], [3]]
    e = map_structure(lambda x: x + 1, a)
    print(e)
    assert e == [[2, 3], [[2, 3], [2, 3]]]
    f = map_structure(lambda x, y: x * y, a, b)
    print(f)
    assert f == [[2, 6], [[2, 6], [2, 6]]]
    g = map_structure(lambda x, y: x * y, a, b)
    print(g)

# Generated at 2022-06-13 20:07:28.385946
# Unit test for function map_structure
def test_map_structure():
    d = {"1": [1,2],"2" : 3}
    print(map_structure(lambda x: x+1,d))
    d = [[1,2,3],["a","b","c"],(3,3,3),{"1":"a","2":"b"},{"1":"a","2":"b"}]
    print(map_structure(lambda x: x+1,d))


# Generated at 2022-06-13 20:07:34.912613
# Unit test for function map_structure_zip
def test_map_structure_zip():
    l1 = [1, 6, 7, 0, 4]
    l2 = [2, 5, 8, 4]
    l3 = [4, 8, 0]

    l_res = map_structure_zip(lambda x, y, z: x + y + z, l1, l2, l3)
    print(l_res)

    t1 = (1, 6, 7, 0, 4)
    t2 = (2, 5, 8, 4)
    t3 = (4, 8, 0)

    t_res = map_structure_zip(lambda x, y, z: x + y + z, t1, t2, t3)
    print(t_res)

    s1 = {1, 2, 3}
    s2 = {3, 2, 1}

# Generated at 2022-06-13 20:07:45.026616
# Unit test for function map_structure
def test_map_structure():
    from collections import namedtuple
    a = [1, [2, 3], (1, [2, 3], {'a': 1})]
    b = [[2, 3], (1, [2, 3], {'a': 1}), {'a': 1}]
    c = namedtuple('c', 'a b c')(a, b, [1, 2, 3])
    assert map_structure(sum, [[1, 2], [3, 4]]) == [3, 7]
    assert map_structure(sum, [[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
    assert map_structure(sum, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == [25, 30]


# Generated at 2022-06-13 20:07:49.252338
# Unit test for function no_map_instance
def test_no_map_instance():
    """
    Test if the no_map_instance can wrap the whole object and not
    traverse into any of the object's object.
    """
    import torch
    obj = torch.Size([1, 2, 3])
    # Test for the first run
    obj_new = no_map_instance(obj)
    # Test if the no_map_instance makes a new instance
    assert id(obj) != id(obj_new)
    # Test if the no_map_instance can deal with list
    obj_list = [obj_new, obj]
    obj_list_new = no_map_instance(obj_list)
    # Test if the obj_list is a new object
    assert id(obj_list) != id(obj_list_new)
    # Test if the nested objects are not changed

# Generated at 2022-06-13 20:08:01.796582
# Unit test for function map_structure_zip
def test_map_structure_zip():
    print("---------------test map_structure_zip--------------------")
    ret1 = map_structure_zip(lambda x, y: x+y, [(1,2,3), (1.1, 2.2, 3.3)])
    print(ret1)
    ret2 = map_structure_zip(lambda x, y: x+y, [(1,2,3), (1.1, 2.2, 3.3)])
    print(ret2)
    ret3 = map_structure_zip(lambda x, y: x+y, [(1,4,3), (1.1, 2.2, 3.3)])
    print(ret3)
    print("---------------test map_structure_zip--------------------")


# Generated at 2022-06-13 20:08:09.645313
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test with dicts
    a1 = {'a': 1, 'b': 2, 'c': 3}
    a2 = {1: 'a', 2: 'b', 3: 'c'}

    expected = {(1, 1): ('a', 'a'), (2, 2): ('b', 'b'), (3, 3): ('c', 'c')}

    assert expected == map_structure_zip(tuple, (a1, a2))
    assert expected == map_structure_zip(tuple, (a2, a1))

    # Test with lists
    a1 = [1, 2, 3]
    a2 = ['a', 'b', 'c']

    expected = [(1, 'a'), (2, 'b'), (3, 'c')]


# Generated at 2022-06-13 20:08:12.338695
# Unit test for function map_structure
def test_map_structure():
    A = [(1,2,3), {'a': 1, 'b': 2}]
    B = map_structure(lambda x: x**2, A)
    C = [(1,4,9), {'a': 1, 'b': 4}]
    assert B == C


# Generated at 2022-06-13 20:08:17.748476
# Unit test for function map_structure_zip
def test_map_structure_zip():
    assert map_structure_zip(lambda x, y: x * 2 + y, [[1, 3, 2], [2, 3, 4]]) == [5, 11, 10]
    assert map_structure_zip(lambda x, y: x * 2 + y, [[[1, 2], [3, 4]], [[2, 3], [4, 5]]]) == [[5, 8], [11, 14]]
    assert map_structure_zip(lambda x, y: x * 2 + y, [[{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], [{'a': 2, 'b': 3}, {'a': 4, 'b': 5}]]) == [{'a': 5, 'b': 8}, {'a': 11, 'b': 14}]
    assert map_st

# Generated at 2022-06-13 20:08:25.274312
# Unit test for function no_map_instance
def test_no_map_instance():
    from torch.nn.utils.rnn import PackedSequence
    from kmeans_pytorch.utils import map_structure

    packed = PackedSequence(data=[1, 2, 3, 4], batch_sizes=[4, 3, 2, 1])
    mapped = map_structure(lambda x: x + 1, packed)
    nmaped = no_map_instance(packed)

    assert all(x.grad == y.grad for x, y in zip(packed.data, mapped.data))
    assert all(x == y for x, y in zip(packed.data, nmaped.data))

# Generated at 2022-06-13 20:08:34.432327
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import defaultdict
    from copy import copy
    from operator import add, mul
    from torch.testing._internal.common_utils import run_tests
    import torch
    import unittest

    def _func_add(*args):
        return sum(args)

    def _func_mul(*args):
        return torch.tensor(1).prod(*args)

    def _func_mean_to_tensors(*args):
        return [torch.tensor(x).mean() for x in args]

    def _func_mean_to_lists(*args):
        return [list(x) for x in zip(*args)]


# Generated at 2022-06-13 20:08:43.743490
# Unit test for function map_structure_zip
def test_map_structure_zip():
    obj1 = [(1, 2), [3, 4], 3]
    obj2 = [(10, 20), [30, 40], 30]
    obj3 = [(100, 200), [300, 400], 300]

    def sum_fn(x, y, z):
        return x + y + z

    assert map_structure_zip(sum_fn, [obj1, obj2, obj3]) == [(111, 222), [333, 444], 333]

# Generated at 2022-06-13 20:08:53.059362
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def test_func(a, b):
        return a - b

    test_instances = [1, 2, 3, 4]
    test_instance_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}, {'a': 7, 'b': 8}]
    test_instance_nested = [{'a': 1, 'b': [2, 3]}, {'a': 4, 'b': [5, 6]}, {'a': 7, 'b': [8, 9]}, {'a': 10, 'b': [11, 12]}]
    test_instance_tuple = [tuple([1, 2]), tuple([3, 4]), tuple([5, 6]), tuple([7, 8])]

    # test list


# Generated at 2022-06-13 20:09:01.704023
# Unit test for function map_structure
def test_map_structure():
    t1 = no_map_instance([1,2,3])
    t2 = map_structure(lambda x: x+1, t1)
    print(t2)
    t3 = map_structure(lambda x,y: x+y, [3,2,1], [1,1,1])
    print(t3)

    t4 = ["a", "b", "c"]
    t5 = map_structure(lambda x, y: (x, y), [1,2,3], t4)
    print(t5)

test_map_structure()

# Generated at 2022-06-13 20:09:11.145795
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    import torch.distributed.rpc as rpc
    from torch._C import _set_default_context
    from torch.distributed import rpc
    from torch.distributed.rpc import RRef
    from torch.distributed.rpc.api import _cleanup_python_rpc_handler
    from torch.distributed.rpc.internal import _callsite_to_string
    from torch.distributed.rpc.utils import _parent_location_from_process_group_agent
    from torch.distributed.rpc.worker_service import WorkerService
    objs = [1, 2, 3, 4]
    torch_test = [torch.ones(3), torch.zeros(3), torch.ones(3)]
    obj = objs[0]

# Generated at 2022-06-13 20:09:16.352880
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [[1,2,3],[4,5,6]]
    b = [[3,2,1],[6,5,4]]
    c = map_structure_zip(lambda x,y: x+y, a, b)
    assert c == [[4,4,4],[10,10,10]]

# Generated at 2022-06-13 20:09:28.415954
# Unit test for function no_map_instance
def test_no_map_instance():
    a = list(range(100))
    a_ = no_map_instance(a)
    assert(a_ == a)
    a_.append(1)
    assert(a_ != a)
    assert(a_[-1] == a[-1])
    a_.clear()
    assert(a_ != a)

# Generated at 2022-06-13 20:09:35.645142
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [10, 20, 30]

    assert map_structure_zip(lambda x, y: x + y, a) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    assert map_structure_zip(lambda x, y: x + y, a, b) == [[11, 22, 33], [24, 35, 46], [37, 48, 59]]

# Generated at 2022-06-13 20:09:40.045216
# Unit test for function map_structure_zip
def test_map_structure_zip():
    l1 = [[1,2,3],[1,0,1]]
    l2 = [[1,0,0],[0,1,0]]
    l_result = map_structure_zip(lambda x,y: x+y, l1,l2)
    assert l_result == [[2,2,3],[1,1,1]]
    print("Failed to pass map_structure_zip test!")

# Generated at 2022-06-13 20:09:45.120106
# Unit test for function map_structure_zip
def test_map_structure_zip():
    t = (1, (1, 2))
    tree = (1, (2, 3))
    trees = [tree, tree, tree]

    def flatten(tree):
        if isinstance(tree, int):
            return tree
        else:
            ls, rs = tree
            return flatten(ls) + flatten(rs)

    def mul(x, y):
        return x * y

    res = map_structure_zip(mul, trees)
    res = map_structure(flatten, res)
    print(res)


if __name__ == '__main__':
    test_map_structure_zip()

# Generated at 2022-06-13 20:09:53.803088
# Unit test for function no_map_instance
def test_no_map_instance():
    # Initialize thre instances of list with same value
    l_t = [1,2,3]
    m_t = [1,2,3]
    n_t = [1,2,3]

    # Convert each instance to no map instance
    l_t = no_map_instance(l_t)
    m_t = no_map_instance(m_t)
    n_t = no_map_instance(n_t)

    # Use map_structure to map function fn 
    # Function fn will increase input by 1
    # The result should be the same as the input
    def fn(x):
        return x+1
    list_t = map_structure(fn, [l_t, m_t, n_t])

# Generated at 2022-06-13 20:10:03.680610
# Unit test for function no_map_instance
def test_no_map_instance():
    x = no_map_instance([1, 2])
    y = no_map_instance({"a": ["b"]})
    z = no_map_instance(x)
    assert x is z
    assert y.__class__ is dict
    assert z.__class__ is list
    x[3] = 1
    assert y["a"] == ["b"]
    assert x == [1, 2, 3]
    assert x[2] == 3
    assert no_map_instance(x)[2] == 3
    assert no_map_instance(x).__class__ is not list
    assert no_map_instance(no_map_instance(x)) is x
    assert no_map_instance(x)[2] is 3
    assert no_map_instance(y)["a"] == ["b"]
    assert no_map_

# Generated at 2022-06-13 20:10:08.939409
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import torch
    import numpy as np
    x = np.random.randint(10, size=(2, 3))
    y = torch.randint(10, (2, 3), dtype=torch.int)
    z = [x, y]
    a = map_structure_zip(lambda a, b, c: a + b + c, z)
    print(a)

if __name__ == "__main__":
    test_map_structure_zip()

# Generated at 2022-06-13 20:10:19.311496
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def test_func(*tuple_inputs):
        return [xi + yi for xi, yi in tuple_inputs]

    label_test = {
        0: {'a': 1, 'b': 2},
        1: {'c': 1, 'd': 2},
        2: {'e': 1, 'f': 2},
    }

    logits_test = {
        0: {'a': 1.3, 'b': 2.2},
        1: {'c': 1.3, 'd': 2.2},
        2: {'e': 1.3, 'f': 2.2},
    }

    out_test = map_structure_zip(test_func, (label_test, logits_test))
    print(out_test)

    din_test = map_st

# Generated at 2022-06-13 20:10:34.749670
# Unit test for function no_map_instance
def test_no_map_instance():
    # If a ndarray has shape (1,1) and is not no_map, it is flattened when mapped
    # If a ndarray has shape (1,1) and is no_map, it is not flattened when mapped
    import numpy as np
    shape = (1,1)
    arr = np.ones(shape)
    no_map_arr = no_map_instance(arr)
    arr = np.reshape(arr,shape)
    no_map_arr = np.reshape(no_map_arr,shape)
    assert np.array_equal(arr,no_map_arr)
    def f(x):
        x = np.squeeze(x)
        return x+1
    assert np.array_equal(f(arr),f(no_map_arr))

# Generated at 2022-06-13 20:10:45.032992
# Unit test for function map_structure
def test_map_structure():
    from typing import NamedTuple

    # Simple example of map_structure with a single tuple
    def plus_one(x: int) -> int:
        return x + 1

    tup = (1, 2, 3, 4)
    assert map_structure(plus_one, tup) == (2, 3, 4, 5)

    # Named tuple example
    class NamedTuple(NamedTuple):
        b: int
        c: str

    def plus_one_named_tuple(named_tuple: NamedTuple) -> NamedTuple:
        return NamedTuple(named_tuple.b + 1, named_tuple.c)

    named_tuple = NamedTuple(1, "Hello")
    assert map_structure(plus_one_named_tuple, named_tuple) == NamedTuple

# Generated at 2022-06-13 20:11:04.064263
# Unit test for function no_map_instance
def test_no_map_instance():
    class A:
        pass
    a = A()
    # test no error
    no_map_instance(a)
    no_map_instance([a])
    no_map_instance({a: 5})

# Generated at 2022-06-13 20:11:18.372013
# Unit test for function map_structure
def test_map_structure():
    def test_list(x):
        return [x, x]
    l = [1, 2, 3]
    assert map_structure(test_list, l) == [[1, 1], [2, 2], [3, 3]]

    def test_dict(x):
        return {x: x}
    d = {0: 0, 1: 1}
    b = map_structure(test_dict, d)
    assert b[0] == {0: 0}
    assert b[1] == {1: 1}

    def test_simple(x):
        return x
    b = map_structure(test_simple, [[1, 2], {3, 4}, (1, 2)])
    assert b[0] == [1, 2]
    assert b[1] == {3, 4}

# Generated at 2022-06-13 20:11:28.296802
# Unit test for function map_structure_zip
def test_map_structure_zip():
    l = [1, 2, 3, 4]
    t = (1, 2, 3, 4)
    d = {'a': 3, 'b': 4}
    ll = [[1, 2, 3], [4, 5, 6]]
    tl = [(1, 2, 3), (4, 5, 6)]
    dl = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    tt = [(1, 2), (3, 4)]
    lt = [1, (2, 3)]
    fl = [1, 2.0, 3.0]
    l3 = [[[1]], [2, [[3]]], 4]
    l4 = [[[1]], [[2]], [3], [[4]]]


# Generated at 2022-06-13 20:11:33.188802
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test different types of data structures
    list_1 = ["a","b","c"]
    list_2 = [1,2,3]
    list_3 = [0.1, 0.2, 0.3]
    print(map_structure_zip(lambda x, y, z: (x, y, z),
                            [list_1, list_2, list_3]))

    tuple_1 = (1,2,3)
    tuple_2 = (2,3,4)
    tuple_3 = (3,4,5)
    print(map_structure_zip(lambda x, y, z: (x, y, z),
                             [tuple_1, tuple_2, tuple_3]))


# Generated at 2022-06-13 20:11:40.214960
# Unit test for function map_structure
def test_map_structure():
    def foo(x):
        return 1
    test_list = [1, 2, 3]
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    test_namedtuple = collections.namedtuple('test', ['x', 'y'])
    test_tuple = (1, 2, 3)
    test_set= set(1, 2, 3)
    test_obj = test_namedtuple(1, test_list)
    test_list = [test_namedtuple(1, test_dict), test_namedtuple(2, test_tuple), test_namedtuple(3, test_list), test_namedtuple(4, test_set), test_namedtuple(5, test_tuple), test_obj]

# Generated at 2022-06-13 20:11:51.130026
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    import numpy as np
    # Register torch.Size as no-map instance
    register_no_map_class(torch.Size)

    def get_sum(*xs):
        ret = 0
        for x in xs:
            if isinstance(x, list):
                ret += get_sum(*x)
            elif isinstance(x, tuple):
                ret += get_sum(*x)
            elif isinstance(x, dict):
                ret += get_sum(*x.values())
            else:
                ret += x
        return ret

    list_0 = [1, 2, 3, 4, 5]
    list_1 = [6, 7, 8, 9, 10]

# Generated at 2022-06-13 20:12:01.514924
# Unit test for function map_structure
def test_map_structure():
    assert map_structure(lambda x: x, [1, 2, 3]) == [1, 2, 3]
    assert map_structure(lambda x: x+1, [1, 2, 3]) == [2, 3, 4]
    assert map_structure(lambda x: x, (1, 2, 3)) == (1, 2, 3)
    assert map_structure(lambda x: x+1, (1, 2, 3)) == (2, 3, 4)

    assert map_structure(lambda x: x, {'a':1, 'b':2}) == {'a':1, 'b':2}
    assert map_structure(lambda x: x+1, {'a':1, 'b':2}) == {'a':2, 'b':3}

    # Test tuple
    assert map_

# Generated at 2022-06-13 20:12:14.418186
# Unit test for function no_map_instance
def test_no_map_instance():
    from ..tokenizers import get_tokenizer
    from ..tokenizers.bert_wordpiece import BertWordPieceTokenizerOptimized
    from ..tokenizers.char_tokenizer import CharTokenizer
    from ..tokenizers.sentencepiece_tokenizer import SentencePieceTokenizerOptimized
    import numpy as np
    a = no_map_instance(get_tokenizer('bert-base-chinese'))
    assert isinstance(a, BertWordPieceTokenizerOptimized)
    b = no_map_instance([a])
    assert isinstance(b[0], BertWordPieceTokenizerOptimized)
    c = no_map_instance({a: b})
    assert isinstance(c[a], list)
    d = no_map_instance((a,))

# Generated at 2022-06-13 20:12:18.961443
# Unit test for function map_structure
def test_map_structure():
    x = [[1, 2, [3]], [4, 5, [6, 7]]]
    y = [[1, 2, [3]], [4, 5, [6, 7]]]
    z = [[1, 2, [3]], [4, 5, [6, 7]]]
    a = [[1, 2, [3]], [4, 5, [6, 7]]]
    fn = lambda x: x+1
    xy = map_structure_zip(fn, [x, y])
    xyz = map_structure_zip(fn, [x, y, z])
    xyza = map_structure_zip(fn, [x, y, z, a])
    # print(x, y, xy, xyz, xyza)

# Generated at 2022-06-13 20:12:26.822665
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import defaultdict
    from typing import List, Dict, Tuple

    def fn(str_tuple: Tuple[str, str]):
        return tuple([x.upper() for x in str_tuple])

    obj1 = ['1', '2', '3']

    obj2 = ['a', 'b', 'c']

    objs = [obj1, obj2]
    mapped_objs = map_structure_zip(fn, objs)
    print(mapped_objs)

    # test ResidualBlock
    obj3 = [{'conv_name' : 'conv_1', 'bn_name' : 'bn_1'},
            {'conv_name' : 'conv_2', 'bn_name' : 'bn_2'}]


# Generated at 2022-06-13 20:13:05.166825
# Unit test for function no_map_instance
def test_no_map_instance():
    assert no_map_instance([1,2,3]) == [1,2,3]
    assert no_map_instance([1,2,3]) is not [1,2,3]


# Generated at 2022-06-13 20:13:09.143794
# Unit test for function map_structure_zip
def test_map_structure_zip():
    list1 = [[1,1],[2,2],[3,3]]
    list2 = [[2,2],[3,3],[4,4]]
    def func(a,b):
        return a+b
    result = map_structure_zip(func,(list1,list2))
    print(result)

test_map_structure_zip()

# Generated at 2022-06-13 20:13:19.838436
# Unit test for function map_structure_zip
def test_map_structure_zip():
    objs = [
        [0, 1],
        (2, 3)
    ]
    assert map_structure_zip(lambda x, y: x, objs) == [0, 1]

    objs = [
        [0, 1],
        [2, 3]
    ]
    assert map_structure_zip(lambda x, y: x + y, objs) == [2, 4]

    objs = [
        [0, 1],
        [2, 3, 4, 5]
    ]
    assert map_structure_zip(lambda x, y: x + y, objs) == [2, 4]

    objs = [
        [0, 1],
        [2, 3, 4, 5]
    ]

# Generated at 2022-06-13 20:13:28.607190
# Unit test for function map_structure
def test_map_structure():
    import numpy as np

    def myfn(x):
        return x*2

    a = 'a'
    b = np.array([0, 1, 2, 3, 4, 5])
    c = {'a': 1, 'c': 3}
    d = ['a', 1, 'c', 3]
    e = {'a': {'b': 'c'}, 'd': {'e': 'f'}}

    print(map_structure(myfn, a))
    print(map_structure(myfn, b))
    print(map_structure(myfn, c))
    print(map_structure(myfn, d))
    print(map_structure(myfn, e))

# test_map_structure()

# Generated at 2022-06-13 20:13:42.367317
# Unit test for function map_structure
def test_map_structure():
    word_to_id ={'a':1,'b':2,'c':3}
    id_to_word = reverse_map(word_to_id)
    assert id_to_word == ['a', 'b', 'c']
    assert map_structure(lambda x:x, [1,2]) == [1,2]
    assert map_structure(lambda x:x+1, [1,2]) == [2,3]
    assert map_structure(lambda x:x, [1,2]) != [1,2,3]
    assert map_structure(lambda x:x+1, [1,2,3]) == [2,3,4]

    class A:
        def __init__(self, a, b):
            self.a = a
            self.b = b

# Generated at 2022-06-13 20:13:44.039343
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch.nn as nn
    no_map_instance(nn.Sequential(nn.Linear(1, 2)))

# Generated at 2022-06-13 20:13:49.261543
# Unit test for function map_structure
def test_map_structure():
    class A:
        def __init__(self, x):
            self.x = x
    class B:
        def __init__(self, y, z=None):
            self.y = y
            self.z = z
    a = A(5)
    b = B(4, 3)
    def func1(x):
        return x + 1
    def func2(x, y):
        return x + y
    print(map_structure(func1, a))
    print(map_structure(func2, b))



# Generated at 2022-06-13 20:14:00.997751
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # test 2d list
    a = [[1,2],[3,4]]
    b = [[3,4],[5,6]]
    result = map_structure_zip(lambda x, y: x + y, a, b)
    assert(result == [[4,6],[8,10]])
    # test 2d tuple
    a = ((1,2),(3,4))
    b = ((3,4),(5,6))
    result = map_structure_zip(lambda x, y: x + y, a, b)
    assert(result == ((4,6),(8,10)))

    # test 2d dict
    a = {"a":[1,2],"b":[3,4]}
    b = {"a":[3,4],"b":[5,6]}

# Generated at 2022-06-13 20:14:09.604276
# Unit test for function no_map_instance
def test_no_map_instance():

    def test_list():
        test_list = [1,2,3]
        fn = lambda x: x + 5
        test_list = no_map_instance(test_list)
        out = map_structure(fn, test_list)
        assert out == [1,2,3]

    def test_list_nested_list():
        test_list = [[1,2,3]]
        fn = lambda x: x + 5
        test_list = no_map_instance(test_list)
        out = map_structure(fn, test_list)
        assert out == [[1,2,3]]

    def test_list_nested_tuple():
        test_list = [(1,2,3)]
        fn = lambda x: x + 5

# Generated at 2022-06-13 20:14:20.912530
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections import namedtuple
    from typing import Dict, List

    a = [1,2,3]
    b = [4,5,6]
    c = (1, 2, 3)
    d = (4,5,6)
    e = {1,2,3}
    f = {4,5,6}
    g = {'a':'A','b':'B','c':'C'}
    h = {'d':'D','e':'E','f':'F'}
    i = [1,2,3,4,5,6]
    j = namedtuple('j','x')
    z = j(x = [1,2,3])
    input_list = [a,b,c,d,e,f,g,h,i,z]
   