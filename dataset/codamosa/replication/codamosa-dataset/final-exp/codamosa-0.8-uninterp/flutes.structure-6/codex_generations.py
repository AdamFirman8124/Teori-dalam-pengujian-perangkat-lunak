

# Generated at 2022-06-13 20:05:21.351984
# Unit test for function map_structure_zip
def test_map_structure_zip():
    assert map_structure_zip(lambda x, y, z: x + y + z, [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z']]) == ['a1x', 'b2y', 'c3z']
    assert map_structure_zip(lambda x, y, z: x + y + z, [['a', 'b'], [1, 2], ['x', 'y']]) == ['a1x', 'b2y']
    assert map_structure_zip(lambda x, y, z: x + y + z, [['a', 'b'], [1, 2, 3], ['x', 'y']]) == ['a1x', 'b2y']

# Generated at 2022-06-13 20:05:28.818190
# Unit test for function no_map_instance
def test_no_map_instance():
    class TestType(list):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Using no_map_instance on a non-container type such as list would
            # raise an exception.
            no_map_instance(self)

    register_no_map_class(TestType)

    x = TestType(['a'])

    # map_structure should not traverse into the TestType instance.
    assert list(map_structure(lambda y: y, x)) == x

# Generated at 2022-06-13 20:05:36.079825
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    import types
    import inspect

    list_instance = [0]
    torch_tensor = torch.FloatTensor([1.0])
    named_tuple_instance = torch.Size([2, 3])
    list_subclass_instance = types.SimpleNamespace([1])
    # Check that the list_subclass_instance was converted to a no_map_instance
    assert(isinstance(list_subclass_instance, _no_map_type(type(list_subclass_instance))))
    # Check that the attributes of the list_subclass_instance were preserved
    assert(len(list_subclass_instance) == 1 and list_subclass_instance[0] == 1)

    # Check that the correct builtin types are considered for no_map_instance

# Generated at 2022-06-13 20:05:42.384470
# Unit test for function no_map_instance
def test_no_map_instance():
    class ListNoMap(list):
        def __init__(self, list_x):
            super(ListNoMap, self).__init__(list_x)

    lnm = ListNoMap([1,2,3])
    lnm_mapped = no_map_instance(lnm)
    assert lnm_mapped.__class__.__name__ == '_no_mapListNoMap'
    assert lnm_mapped[1] == 2
    assert lnm_mapped._NO_MAP_INSTANCE_ATTR == True


# Generated at 2022-06-13 20:05:53.977902
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # case 1: list
    test_objs_1 = [[1, 2], [3, 4]]
    test_fn_1 = lambda x, y: x + y
    test_output_1 = [4, 6]
    assert map_structure_zip(test_fn_1, test_objs_1) == test_output_1

    # case 2: dict
    namedtuple = lambda *x: collections.namedtuple('X', x)(*x)
    test_objs_2 = [{"a": namedtuple(1, 2, 3), "b": namedtuple(4, 5, 6)},
                   {'a': namedtuple(7, 8, 9), 'b': namedtuple(10, 11, 12)}]

# Generated at 2022-06-13 20:05:57.076455
# Unit test for function map_structure
def test_map_structure():
    a = {"a": [[1, 2], [3, 4]]}
    b = map_structure(lambda x: x ** 2, a)
    assert (b == {"a": [[1, 4], [9, 16]]})


# Generated at 2022-06-13 20:06:02.369013
# Unit test for function map_structure_zip
def test_map_structure_zip():
    t1 = {'h': {'nest': 'key'}, 'hello': 3}
    t2 = {'h': {'nest': 'key'}, 'hello': 4}
    t3 = map_structure_zip(lambda x, y: x + y, [t1, t2])
    assert(t3 == {'h': {'nest': 'keykey'}, 'hello': 7})

# Generated at 2022-06-13 20:06:08.080215
# Unit test for function no_map_instance
def test_no_map_instance():
    test_dict = {1: 1, 2: 2}
    no_mapped_dict = no_map_instance(test_dict)
    print(no_mapped_dict)
    print(isinstance(no_mapped_dict, dict))

if __name__ == "__main__":
    test_no_map_instance()

# Generated at 2022-06-13 20:06:19.536914
# Unit test for function map_structure_zip
def test_map_structure_zip():
    
    # First element in the list is a dictionary, the rest are lists
    lst = [
        {'a': [1, 2, 3], 'b': [4, 5, 6]},
        [5, 10, 15],
        [6, 12, 18]
     ]
    
    # This function should be applied to each of the values in the dictionary,
    # i.e. [1, 2, 3], [4, 5, 6], [5, 10, 15], [6, 12, 18]
    zipped = map_structure_zip(lambda x, y, z: [x*y*z, x+y+z], lst)
    
    assert zipped == [
        {'a': [30, 9], 'b': [120, 15]},
        [90, 21]
    ]

# Generated at 2022-06-13 20:06:25.452133
# Unit test for function map_structure
def test_map_structure():
    a = [1,2,3]
    b = [1,2,3]
    c = {'a':1,'b':2}
    d = {'a':1,'b':2}
    e = {'a':1,'b':2,'c':3}
    f = {'a':1,'b':2,'c':3}

    def fn(x):
        return 2*x

    assert map_structure(fn, a) == [2,4,6]
    assert map_structure(fn, c) == {'a':2,'b':4}

    assert map_structure_zip(lambda a,b:a+b, [a,b]) == [2,4,6]
    assert map_structure_zip(lambda c,d: c == d, [c,d]) == True

# Generated at 2022-06-13 20:06:49.004900
# Unit test for function map_structure
def test_map_structure():
    from .func import compose
    import torch
    import random
    import copy

    def add1(v):
        return v + 1

    def get_random_integer(v):
        return random.randint(0, 1)

    def add_random_integer(v, r):
        return v + r

    #   Test 1:
    #       input: list
    #       fn: add1()
    list_1 = [1, 2, 3, 4, 5]
    list_2 = map_structure(add1, list_1)

    #   Test 2:
    #       input: list with list
    #       fn: add1()
    list_1 = [1, 2, [3, 4, 5], 4, 5]
    list_2 = map_structure(add1, list_1)

   

# Generated at 2022-06-13 20:07:00.084585
# Unit test for function no_map_instance
def test_no_map_instance():
    seq_list = [
        2,
        2.2,
        "2.2",
        [2] * 2,
        ["2"] * 2,
        [2, 2.2, "2.2"],
        (2, 2.2, "2.2"),
        {2, 2.2, "2.2"},
        (2,),
        {"2"},
        {2: 2.2},
        {2, 1, 2.2, 2.1},
    ]

    for seq in seq_list:
        assert(map_structure(lambda x: 2, no_map_instance(seq)) == seq)

# Generated at 2022-06-13 20:07:11.113101
# Unit test for function no_map_instance
def test_no_map_instance():
    # Test for arguments 'instance' of different types
    print("Test for argument 'instance' of type {}".format(type(1)))
    test = no_map_instance(1)
    print("Result: {}\n".format(test))
    print("Test for argument 'instance' of type {}".format(type([1, 2])))
    test = no_map_instance([1, 2])
    print("Result: {}\n".format(test))
    print("Test for argument 'instance' of type {}".format(type((1, 2))))
    test = no_map_instance((1, 2))
    print("Result: {}\n".format(test))
    print("Test for argument 'instance' of type {}".format(type({1, 2})))
    test = no_map_instance({1, 2})

# Generated at 2022-06-13 20:07:20.362811
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # test1
    class Test1:
        def __init__(self, x:int):
            self.x = x
    list1 = [Test1(i) for i in range(4)]
    list2 = [Test1(i) for i in range(4)]
    def fn(a:Test1, b:Test1):
        return a.x + b.x
    result = map_structure_zip(fn, [list1, list2])
    expected = [0,2,4,6]
    assert result == expected

    # test2
    list1 = [[1,2,3],[4,5,6]]
    list2 = [[7,8,9], [10,11,12]]

# Generated at 2022-06-13 20:07:31.655112
# Unit test for function no_map_instance
def test_no_map_instance():
    def fn(x):
        return x + 1

    a = no_map_instance([1, 2, 4])
    assert a == [1, 2, 4]

    b = map_structure(fn, a)
    assert (a == b) == False
    assert b == [2, 3, 5]
    assert id(a) == id(b)

    c = no_map_instance([1, 2, no_map_instance([4, 5])])
    assert c == [1, 2, [4, 5]]

    d = map_structure(fn, c)
    assert (c == d) == False
    assert d == [2, 3, [5, 6]]
    assert id(c) == id(d)

    e = no_map_instance(no_map_instance(1))
    assert e

# Generated at 2022-06-13 20:07:42.925308
# Unit test for function no_map_instance
def test_no_map_instance():
    from contextlib import contextmanager
    from types import SimpleNamespace
    from collections import OrderedDict
    from functools import partial

    def custom_list_class(*args, **kwargs):
        return list(*args, **kwargs)

    @contextmanager
    def assert_raises_non_mappable(*exceptions):
        with pytest.raises(Exception) as err:
            yield
        assert isinstance(err.value, tuple(exceptions))

    def list_equal(list1, list2):
        return len(list1) == len(list2) and all(x == y for x, y in zip(list1, list2))

    def test_raise_exception(obj, fn, expected_exception):
        custom_list = custom_list_class([obj])

        fn(obj)
       

# Generated at 2022-06-13 20:07:50.510570
# Unit test for function map_structure
def test_map_structure():
    list1 = [['a', 'a', 'a'], ['b', 'b', 'b'], ['c', 'c', 'c']]
    list2 = [['1', '1', '1'], ['2', '2', '2'], ['3', '3', '3']]
    list3 = [['{', '{', '{'], ['}', '}', '}'], ['!', '!', '!']]
    list4 = [['0', '0', '0'], ['1', '1', '1'], ['2', '2', '2']]
    list5 = [['a', 'a', 'a'], ['b', 'b', 'b'], ['c', 'c', 'c']]

    test = lambda l: ''.join(l)
    #test = lambda l,

# Generated at 2022-06-13 20:07:59.816652
# Unit test for function no_map_instance
def test_no_map_instance():
    import torch
    # test torch.Size
    size = torch.Size((1,))
    assert size._no_map_Size__no_map_ == False
    assert no_map_instance(size)._no_map_Size__no_map_ == True
    # test list
    list_ = [1, 2, 3]
    assert list_._no_map_list__no_map_ == False
    assert no_map_instance(list_)._no_map_list__no_map_ == True

# Generated at 2022-06-13 20:08:02.663522
# Unit test for function map_structure_zip
def test_map_structure_zip():
    assert map_structure_zip(sum, [{1: 2, 3: 4}, {1: 3, 3: 5}]) == {1: 5, 3: 9}
    assert map_structure_zip(sum, [[1, 2], [3, 4]]) == [4, 6]
    assert map_structure_zip(sum, [(1, 2), (3, 4)]) == (4, 6)

test_map_structure_zip()

# Generated at 2022-06-13 20:08:17.745199
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = {'a': [1, 2, 3], 'b': "abcd", 'c': (1.0, 1.2, 3.4)}
    b = {'a': [2, 3, 4], 'b': "efgh", 'c': (5.0, 6.2, 7.4)}
    pairs = [a, b]

    def func(dict1, dict2):
        dict3 = {}
        for key in list(dict1.keys()):
            if isinstance(dict1[key], list):
                dict3[key] = [dict1[key][i] + dict2[key][i] for i in range(len(dict1[key]))]

# Generated at 2022-06-13 20:08:26.574341
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import namedtuple
    in_list_a = [1, {'x': 2, 'y': 3}, [4, 5]]
    in_list_b = [1, {'y': 3, 'x': 2}, [5, 4]]
    in_list_c = [1, {'y': 4, 'x': 2}, [1, 4]]

    in_tuple_a = (3, 3)
    in_tuple_b = (1, 1)
    in_tuple_c = (2, 2)

    in_dict_a = {'y': 1, 'x': 2}
    in_dict_b = {'y': 2, 'x': 1}
    in_dict_c = {'y': 3, 'x': 1}

    in_namedtuple_a = namedt

# Generated at 2022-06-13 20:08:35.831700
# Unit test for function no_map_instance
def test_no_map_instance():
    @register_no_map_class
    class C(list):
        pass

    test_list = [1, 2, 3]
    test_list_class = C([1, 2, 3])
    test_list_instance = no_map_instance([1, 2, 3])
    test_list_instance_class = no_map_instance(C([1, 2, 3]))
    test_list_instance_class_dict = no_map_instance(
        C([1, 2, 3]), {'name': 'tester'})
    assert isinstance(test_list_instance_class, C)
    assert isinstance(test_list_instance, list)
    assert isinstance(test_list_instance_class_dict, C)


# Generated at 2022-06-13 20:08:44.090012
# Unit test for function map_structure_zip
def test_map_structure_zip():
    assert map_structure_zip(lambda *xs: [x for x in xs], [1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert map_structure_zip(lambda *xs: {x for x in xs}, [1, 2, 3], [1, 2, 3]) == [{1, 2, 3}]
    assert map_structure_zip(lambda *xs: {x for x in xs}, [1, 2, 3], [4, 5, 6]) == [{1, 4}, {2, 5}, {3, 6}]

# Generated at 2022-06-13 20:08:53.222390
# Unit test for function map_structure
def test_map_structure():
    assert map_structure(lambda x: x - 1, [1,2,3]) == [0,1,2]
    assert map_structure(lambda x: x - 1, [[1,2],[2,1],[1,1]]) == [[0,1],[1,0],[0,0]]
    assert map_structure(lambda x: x - 1, ([1,2],[3,4])) == ([0,1],[2,3])
    assert map_structure(lambda x: x - 1, ([1,2],[2,1])) == ([0,1],[1,0])
    assert map_structure(lambda x: x - 1, {'a': [1,2], 'b': [3,4]}) == {'a': [0,1], 'b': [2,3]}
    assert map_st

# Generated at 2022-06-13 20:09:04.827822
# Unit test for function map_structure
def test_map_structure():
    def times(a: int) -> int:
        return a * 2

    def plus(b: int) -> int:
        return b + 3

    # single element
    assert(map_structure(times, 3) == 6)
    assert(map_structure(plus, 3) == 6)

    # multiple elements
    assert(map_structure(times, [3, 4, 5]) == [6, 8, 10])
    assert(map_structure(plus, [3, 4, 5]) == [6, 7, 8])

    # mixed elements
    assert(map_structure(lambda x, y: x * y, [3, 4, [5, 6]]) == [9, 16, [25, 36]])

    # nested list

# Generated at 2022-06-13 20:09:16.393390
# Unit test for function map_structure
def test_map_structure():
    input1 = [1, 2, [3, 4, 5]]
    input2 = [[1, 2, 3], 4, 5]
    input3 = [[1, 2, [3, 4]], 4, [5, 9]]

    output1 = map_structure(lambda x: x*x, input1)
    print(output1)
    assert(output1 == [1, 4, [9, 16, 25]])

    output2 = map_structure(lambda x: x * x * x, input2)
    output2 = list(output2)
    print(output2)
    assert (output2 == [1, 8, 125])

    output3 = map_structure(lambda x: x*x + x, input3)
    output3 = list(output3)
    print(output3)

# Generated at 2022-06-13 20:09:27.577012
# Unit test for function map_structure
def test_map_structure():
    def add1(x):
        return x + 1
    obj = [[1],
           {'a': 1, 'b': [2]},
           (1, 2, {'a': 3})]

    mapped = map_structure(add1, obj)

    assert mapped == [[2],
                      {'a': 2, 'b': [3]},
                      (2, 3, {'a': 4})]

    def sum_tuples(x, y):
        return x + y

    obj1 = (1, 2, {'a': 3})
    obj2 = (4, 5, {'a': '6'})
    mapped = map_structure_zip(sum_tuples, [obj1, obj2])

    assert mapped == (5, 7, {'a': '36'})

# Generated at 2022-06-13 20:09:33.607280
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [1, 2]
    b = [3, 4]
    c = [5, 6]
    
    def func(x, y, z):
        return x[0] + y[0] + z[0]
    
    print(map_structure_zip(func, [a, b, c]))
    
#test_map_structure_zip()

# Generated at 2022-06-13 20:09:41.752968
# Unit test for function no_map_instance
def test_no_map_instance():
    class A:
        def __init__(self, a):
            self.a = a
    
    def f(x):
        return x
    def ff(x):
        if isinstance(x, A):
            return f(x.a)
        else:
            return f(x)
    a = A(1)
    b = A(2)
    c = A(3)
    
    # Test that A is treated as a single object (non_mappable)
    tree = [[a, b], c]
    expected = map_structure(f, tree)
    actual = map_structure(ff, tree)
    print(expected)
    print(actual)
    assert expected == actual

    # Test that A is treated as a normal object

# Generated at 2022-06-13 20:09:51.820404
# Unit test for function map_structure
def test_map_structure():
    """Unit test for function map_structure."""
    @no_type_check
    def square_fraction_list(x):
        return [i**2/sum(x) for i in x]

    @no_type_check
    def square_fraction_dict(x):
        if x:
            total = sum(x.values())
            return {k: v**2/total for k, v in x.items()}
        else:
            return {}

    @no_type_check
    def add(*x):
        return sum(x)

    test_list = [[[0, 1, 2, 3], [3, 4, 5, 6]], [[10, 9, 8, 7], [7, 6, 5, 4]], [[11, 12], [13, 14]]]

# Generated at 2022-06-13 20:10:05.197484
# Unit test for function map_structure_zip
def test_map_structure_zip():
    dict1 = {'a': 1, 'b': 2, 'b': [3, 4]}
    dict2 = {'a': 1, 'b': 2, 'b': [3, 5]}
    dict3 = {'a': 1, 'b': 2, 'b': [6, 5]}
    dict_zip = map_structure_zip(lambda x, y, z: x + y + z, (dict1, dict2, dict3))
    assert(dict_zip == {'a': 3, 'b': [12, 14]})

# Generated at 2022-06-13 20:10:11.585390
# Unit test for function map_structure_zip
def test_map_structure_zip():
    obj1 = [1, [2, 3], {"今天": "星期日"}]
    obj2 = [4, [5, 6], {"今天": "星期一"}]
    obj3 = [7, [8, 9], {"今天": "星期二"}]
    
    real = [12, [15, 18], {"今天": "星期三"}]
    test = map_structure_zip(sum, [obj1, obj2, obj3])
    assert all(a == b for a, b in zip(real, test))

# Generated at 2022-06-13 20:10:22.007414
# Unit test for function map_structure_zip
def test_map_structure_zip():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    a_dict = {'a': a, 'b': b, 'c': c}
    a_tuple = (a, b, c)

    assert [i+j+k for i, j, k in zip(a, b, c)] == map_structure_zip(lambda x, y, z: x+y+z, [a, b, c])
    assert [i+j+k for i, j, k in zip(a, b, c)] == map_structure_zip(lambda x, y, z: x+y+z, (a, b, c))
    assert [i+j+k for i, j, k in zip(a, b, c)] == map_

# Generated at 2022-06-13 20:10:29.163333
# Unit test for function map_structure
def test_map_structure():
    import random
    import torch
    from torch.utils.data import Dataset
    from torch.utils.data import Dataset, IterableDataset, ConcatDataset, Subset, RandomSampler, BatchSampler
    from torch.utils.data import DataLoader as TorchDataLoader
    from torch.utils.data.dataloader import _SingleProcessDataLoaderIter, DataLoaderIter
    import multiprocessing

    class MyDataset(IterableDataset):
        def __iter__(self):
            return self

        def __next__(self):
            return random.randint(0,100), random.randint(0,100)

    def my_collate_fn(batch_data):
        num_gpu = torch.cuda.device_count()

        # "names" and "batch_sizes

# Generated at 2022-06-13 20:10:38.243239
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def fun(a,b,c):
        return a+b+c

    a = [[1,2],[3,4]]
    b = [[5,6],[7,8]]
    c = [[9,10],[11,12]]
    assert map_structure_zip(fun, (a,b,c)) == [[15,18],[21,24]]

    a = [1,2]
    b = [[5,6],[7,8]]
    c = [9,10]
    assert map_structure_zip(fun, (a,b,c)) == [[15,16],[17,18]]

    a = [[1,2],[3,4]]
    b = [[5,6],[7,8]]
    c = {'a':9,'b':10}

# Generated at 2022-06-13 20:10:49.087129
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from torch.nn import ModuleList, ModuleDict

    list_of_list = list(range(3))
    list_of_tuple = [(i, i*2, i*3) for i in range(3)]
    list_of_dict = [{i: i*2, i+1: i*3} for i in range(3)]
    list_of_set = [{i, i*2, i*3} for i in range(3)]
    list_of_nnmodule = [ModuleList([ i, i*2, i*3 ]), ModuleDict({i: i*2, i+1: i*3})]

    assert ([0, 1, 2] == map_structure_zip(lambda x: x, list_of_list))

# Generated at 2022-06-13 20:10:57.625140
# Unit test for function map_structure_zip
def test_map_structure_zip():

    def fn(x, y):
        return x * y

    def fn2(x: int, y: int) -> int:
        return x * y

    x1 = [1, 2, 3]
    x2 = [1, 4, 9]
    assert map_structure_zip(fn, (x1, x2)) == [1, 8, 27]
    assert map_structure_zip(fn2, (x1, x2)) == [1, 8, 27]

    # namedtuple
    from typing import NamedTuple
    x1 = (1,2)
    x2 = (2,4)
    assert map_structure_zip(fn, (x1, x2)) == (2,8)

# Generated at 2022-06-13 20:11:07.623832
# Unit test for function map_structure_zip
def test_map_structure_zip():
    # Test list
    to_string = lambda x: str(x)
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    result = map_structure_zip(to_string, [list1, list2])
    assert result == ['1', '2', '3'], \
        "map_structure_zip did not do a element-by-element map. The result should be ['1', '2', '3'] but it is {}".format(result)

    # Test dict
    to_string = lambda x: str(x)
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 'a', 'b': 'b', 'c': 'c'}

# Generated at 2022-06-13 20:11:16.240747
# Unit test for function no_map_instance
def test_no_map_instance():
    assert map_structure(lambda x: x + 1, no_map_instance([1,2,3])) == no_map_instance([1,2,3])
    assert map_structure(lambda x: x + 1, no_map_instance((1,2,3))) == no_map_instance([1,2,3])  # namedtuple
    assert map_structure(lambda x: x + 1, no_map_instance({'a': 1, 'b': 2, 'c':3})) == no_map_instance({'a': 1, 'b': 2, 'c':3})
    assert map_structure(lambda x: x + 1, no_map_instance(set([1,2,3]))) == no_map_instance(set([1,2,3]))

# Generated at 2022-06-13 20:11:26.317270
# Unit test for function no_map_instance
def test_no_map_instance():
    list_with_set = no_map_instance(['1', ['2', set([3])]])
    assert no_map_instance(list_with_set) == list_with_set
    assert list_with_set == ['1', ['2', {3}]]
    dict_with_set = no_map_instance({'list': ['1', ['2', set([3])]], 'set': {'4', '5'}})
    assert no_map_instance(dict_with_set) == dict_with_set
    assert dict_with_set == {'list': ['1', ['2', {3}]], 'set': {'4', '5'}}
    tuple_with_set = no_map_instance((1, (2, 3, set([4, 5]))))

# Generated at 2022-06-13 20:11:40.091329
# Unit test for function map_structure
def test_map_structure():
    r"""Test for function map_structure"""
    test_case_1 = {1:[1,1], 2:[2,2]}
    test_case_2 = [{1:[1,1], 2:[2,2]}, {1:[1,1], 2:[2,2]}]
    test_case_3 = [{1:[1,1], 2:[2,2]}, [{1:[1,1], 2:[2,2]}]]
    assert map_structure(lambda x: x * 2, test_case_1) == {1: [2, 2], 2: [4, 4]}
    assert map_structure(lambda x: [y * 2 for y in x], test_case_1) == {1: [2, 2], 2: [4, 4]}


# Generated at 2022-06-13 20:11:51.021919
# Unit test for function map_structure
def test_map_structure():
    import collections
    def fn(x):
        if isinstance(x, collections.Sequence):
            return list(x)
        return x

    def test_for_type(t, value):
        test_dict = (
            map_structure(fn, t({"a": 1})),
            map_structure(fn, t({"a": 1, "b": 2})),
            map_structure(fn, t({})),
            map_structure(fn, t({})),
            map_structure(fn, t({})),
        )
        if value:
            assert next(iter(test_dict[0].keys())) == "a"
            assert next(iter(test_dict[1].keys())) == "a"
            assert len(test_dict[1]) == 2

# Generated at 2022-06-13 20:12:01.482641
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import numpy as np
    # 1-d test
    lst1 = [1, 2, 3]
    lst2 = [3, 4, 5]
    lst3 = [5, 6, 7]
    fn = lambda x, y, z: x + y + z
    test1 = map_structure_zip(fn, [lst1, lst2, lst3])
    assert test1 == [9, 12, 15]
    # 2-d test
    lst1 = [[1,2],[3,4]]
    lst2 = [[3,4],[5,6]]
    lst3 = [[5,6],[7,8]]
    fn = lambda x, y, z: x + y + z

# Generated at 2022-06-13 20:12:08.650418
# Unit test for function map_structure
def test_map_structure():
    from torch.nn import Module
    l = no_map_instance([1, 2, 3])

    class TestModule(Module):
        def __init__(self):
            super().__init__()
            self.l = l

        def forward(self, x):
            return x + self.l

    class TestModule2(Module):
        def __init__(self):
            super().__init__()
            self.net = TestModule()

        def forward(self, x):
            return x * self.net(x)

    test_net = TestModule2()
    new_test_net = map_structure(lambda x: x + 1, test_net)

    assert id(new_test_net.net.l) == id(test_net.net.l)

# Generated at 2022-06-13 20:12:13.113993
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from collections import namedtuple
    A = namedtuple('A', ['a', 'b', 'c'])
    a = A(a=1,b=2,c=3)
    a1 = A(a=11,b=22,c=33)
    a2 = A(a=111,b=222,c=333)
    def f(a,b,c):
        return a+b+c
    a_new = map_structure_zip(f, [a,a1,a2])
    print(a_new)
    assert a_new == A(a=123,b=246,c=369)

if __name__ == '__main__':
    test_map_structure_zip()

# Generated at 2022-06-13 20:12:18.647864
# Unit test for function no_map_instance
def test_no_map_instance():
    # Use a class to simulate built-in class
    class list_subclass(list):
        pass
    lst = list_subclass([1, 2, 3])
    lst_no_map_instance = no_map_instance(lst)
    assert hasattr(lst_no_map_instance, _NO_MAP_INSTANCE_ATTR)


# Generated at 2022-06-13 20:12:30.291543
# Unit test for function map_structure_zip
def test_map_structure_zip():
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    def fn(*xs):
        return sum(xs)

    assert map_structure_zip(fn, [my_list, my_tuple, my_dict]) == 6
    assert map_structure_zip(fn, [my_tuple, my_list]) == 3
    assert map_structure_zip(fn, [my_dict, my_tuple]) == 6


if __name__ == "__main__":
    test_map_structure_zip()

# Generated at 2022-06-13 20:12:41.124096
# Unit test for function map_structure_zip
def test_map_structure_zip():
    def f1(a, b, c):
        return a+b+c
    def f2(a, b, c):
        return a*b*c
    def f3(a, b, c):
        return a/b/c
    d1 = dict(a=[1,2],b={1:1,2:2},c=torch.Size([1,2]))
    d2 = dict(a=[4,5],b={3:3,4:4},c=torch.Size([3,4]))
    d3 = dict(a=[7,8],b={5:5,6:6},c=torch.Size([5,6]))
    d = map_structure_zip(f1, [d1,d2,d3])
    print(d)
    d = map

# Generated at 2022-06-13 20:12:47.523438
# Unit test for function no_map_instance
def test_no_map_instance():
    from collections import namedtuple
    from functools import partial
    from copy import copy
    from pytest import raises

    ins1 = no_map_instance([1, 2, 3])
    ins2 = no_map_instance({"a": 1, "b": 2})
    ins3 = no_map_instance((1, 2, 3))
    tup_ins1 = no_map_instance(namedtuple("tup1", "x,y,z")(1, 2, 3))
    ins4 = no_map_instance({1, 2, 3})
    fn1 = partial(map_structure, lambda x: x + 1)
    fn2 = partial(map_structure_zip, lambda *x: x)

    assert fn1(ins1) == fn1([1, 2, 3])
    assert fn1

# Generated at 2022-06-13 20:12:54.141099
# Unit test for function no_map_instance
def test_no_map_instance():
    class Inner(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class Outer(object):
        def __init__(self, i, j):
            self.i = i
            self.j = j

    outer = Outer(Inner(1, 2), Inner(3, 4))
    outer_new = no_map_instance(outer)
    assert hasattr(outer_new, _NO_MAP_INSTANCE_ATTR)

    def f(x):
        return x

    outer_new = no_map_instance(outer)
    assert outer_new == map_structure(f, outer)

# Generated at 2022-06-13 20:13:20.851950
# Unit test for function no_map_instance
def test_no_map_instance():
    obj_list = [torch.ones(10), torch.zeros(10)]
    assert map_structure(lambda x: x.sum().item(), obj_list) == [10, 0]
    obj_list = [no_map_instance(torch.ones(10)), torch.zeros(10)]
    assert map_structure(lambda x: x.sum().item(), obj_list) == [10, 0]
    obj_list = [no_map_instance(torch.ones(10)), torch.zeros(10), no_map_instance(torch.ones(10))]
    assert map_structure(lambda x: x.sum().item(), obj_list) == [10, 0, 10]

# Generated at 2022-06-13 20:13:28.117156
# Unit test for function map_structure_zip
def test_map_structure_zip():
    data = [[1,2],[1,2],[1,2]]
    expected = lambda x: x[0]+x[1]+x[2]
    actual = map_structure_zip(lambda x,y,z : x+y+z, data)
    for i in range(len(expected(data))):
        assert expected(data) == actual


# EOF

# Generated at 2022-06-13 20:13:42.121413
# Unit test for function no_map_instance
def test_no_map_instance():

    from collections import namedtuple
    from pytorch_transformers.tokenization_utils import BatchEncoding
    from pytorch_transformers.tokenization_bert import BertTokenizer

    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')


# Generated at 2022-06-13 20:13:49.469097
# Unit test for function map_structure_zip
def test_map_structure_zip():
    from zerogercrnn.lib.random_utils import get_random_state
    from torch.autograd import Variable
    from math import sqrt

    def test_map_structure_zip_fn(a, b, c):
        return sqrt(a ** 2 + b ** 2 + c ** 2)
    
    def check_that_map_structure_applied_correctly(x):
        # print('x:', x)
        assert not isinstance(x, dict)
        assert not isinstance(x, list)
        assert not isinstance(x, set)
        assert isinstance(x, tuple)
        a, b, c = x
        return a ** 2 + b ** 2 + c ** 2

    rand_state = get_random_state(seed=1234)

# Generated at 2022-06-13 20:14:01.041986
# Unit test for function no_map_instance
def test_no_map_instance():
    import pytest
    from .util import create_random_tensors

    a, _b, _c = create_random_tensors(3, (1,))

    # `a` is an instance of `torch.Size`
    assert type(a) == torch.Size

    # We avoid map_structure (and map_structure_zip) to map over Size instances:
    assert no_map_instance(a) == a

    # TODO: we should test that the contents of `a` is not mapped

    # Test that we can register torch.Size as a type that is treated as no-map
    with pytest.raises(ValueError):
        map_structure(lambda x: x + 1, a)

    register_no_map_class(torch.Size)
    # `map_structure` does not

# Generated at 2022-06-13 20:14:09.637151
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import numpy as np
    data = dict(a=[1, 2, 3], b=[4, 5, 6], c=[7, 8, 9])
    data1 = dict(a=[2, 3, 4], b=[5, 6, 7], c=[8, 9, 10])

    def f(aa, *args):
        return aa + sum(*args)

    expected = dict(a=2, b=6, c=10)

    result = map_structure_zip(f, [data, data1])
    assert result == expected

    data2 = dict(a=[1, 2], b=[4, 5], c=[7, 8])
    expected = dict(a=np.nan, b=np.nan, c=np.nan)

# Generated at 2022-06-13 20:14:20.951425
# Unit test for function map_structure
def test_map_structure():
    # Test using `named_tuple`
    test_tuple = namedtuple("test", "a b")
    a = test_tuple(1, 3)
    b = test_tuple(2, 4)
    # Map with not nested
    assert map_structure(lambda x: x-1, a) == tuple((0, 2))
    assert map_structure(lambda x: x-1, b) == tuple((1, 3))
    # Map with nested
    assert map_structure(lambda x: x-1, (a, b)) == tuple((tuple((0, 2)), tuple((1, 3))))
    # Func receive 2 variables
    assert map_structure_zip(lambda x, y: x-y, (a, b)) == tuple((-1, -1))

# Generated at 2022-06-13 20:14:30.721653
# Unit test for function map_structure_zip
def test_map_structure_zip():
    import unittest
    
    class TestMapStructureZip(unittest.TestCase):

        def test_map_structure_zip(self):
            self.assertEqual(map_structure_zip(sum, [[1, 2], [1, 3], [2, 4]]), [[4, 9]])
            self.assertEqual(map_structure_zip(sum, [[1, 2], [1, 3], [2, 4]]), [[4, 9]])
            self.assertEqual(map_structure_zip(sum, ([1, 2], [1, 3], [2, 4])), (4, 9))
            self.assertEqual(map_structure_zip(sum, [(1, 2), (1, 3), (2, 4)]), tuple(zip(4, 9)))

# Generated at 2022-06-13 20:14:42.612183
# Unit test for function no_map_instance
def test_no_map_instance():

    @register_no_map_class(list)
    def mydecorator(fn):
        return fn

    @mydecorator
    def add_one(x):
        return x + 1

    @mydecorator
    def add_one_more(x):
        return x + 1

    original_data = [[1, 2], [[3, 4], [5, [6, 7], [8]]]]
    chained_data = []

    def chained_add(x):
        chained_data.append(x)
        return add_one(x)

    def chained_add_one_more(x):
        chained_data.append(x)
        return add_one_more(x)

    # Sanity check for the functions
    assert add_one([1, 2]) == [2, 3]
    assert add

# Generated at 2022-06-13 20:14:46.083997
# Unit test for function map_structure
def test_map_structure():
    def add(x):
        return x+1
    obj1 = {'a': [1, 2, 3], 'b': 4}
    #obj2 = map_structure(add, obj1)
    #print(obj2)
    #print(type(obj2))

#test_map_structure()

# Generated at 2022-06-13 20:15:15.540907
# Unit test for function map_structure_zip
def test_map_structure_zip():
    lis = [2,3,5,7]
    def fn(x,y,z):
        return str(x+y+z)

    print(type(fn(2,2,2)))
    print(type(map_structure_zip(fn, [lis,lis,lis])))