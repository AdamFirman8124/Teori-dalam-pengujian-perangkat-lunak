

# Generated at 2022-06-13 19:52:27.832680
# Unit test for function take
def test_take():
    t = [0,1,2,3,4,5,6,7,8,9]
    t_str = ['a', 'b', 'c', 'd']
    arr1 = take(5, t)
    assert [x for x in arr1] == [0,1,2,3,4]
    assert [x for x in take(2, t_str)] == ['a', 'b']
    # Test throw exception
    try:
        arr2 = [x for x in take(-1, t)]
    except:
        assert True
    try:
        arr2 = [x for x in take(1, t)]
    except:
        assert False
    assert [x for x in take(100, t)] == t
    assert [x for x in take(0, t)] == []


# Generated at 2022-06-13 19:52:38.677014
# Unit test for function take
def test_take():
    assert list(take(5, range(1000000))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(1000000))) == []
    assert list(take(5, range(0))) == []
    assert list(take(5, range(3))) == [0, 1, 2]
    with pytest.raises(ValueError):
        list(take(-5, range(10)))
            
test_take()



# Generated at 2022-06-13 19:52:47.923670
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [0, 5, 0, 6])) == [6]
    assert list(drop_until(lambda x: x > 5, [])) == []
    assert list(drop_until(lambda x: x > 0, [0, 5, 6])) == [5, 6]
    assert list(drop_until(lambda x: x > 0, [0])) == []



# Generated at 2022-06-13 19:52:56.418368
# Unit test for function take
def test_take():
    # Iterable should yield the first n elements of the iterable
    assert list(take(3, range(10))) == [0, 1, 2]
    assert list(take(5, chain(range(5), map(lambda x: x*x, range(5, 10))))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(100))) == []

    # If n < 0, an exception is raised
    with pytest.raises(ValueError):
        list(take(-1, range(100)))

    # Take is lazy
    with pytest.raises(ValueError):
        list(take(15, (x for x in (i - 20 for i in range(20)) if x > 0)))



# Generated at 2022-06-13 19:52:59.196183
# Unit test for function take
def test_take():
    assert list(take(5, range(1000000))) == [0, 1, 2, 3, 4]
test_take()



# Generated at 2022-06-13 19:53:01.709082
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]



# Generated at 2022-06-13 19:53:10.226819
# Unit test for function split_by
def test_split_by():
    def assertEqual(it1: Iterator[List[int]], it2: Iterator[List[int]]):
        l1 = list(it1)
        l2 = list(it2)
        assert l1 == l2

    assertEqual(split_by(range(10), criterion=lambda x: x % 3 == 0),
                [[1, 2], [4, 5], [7, 8]])
    assertEqual(split_by(" Split by: ", empty_segments=True, separator='.'),
                [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []])



# Generated at 2022-06-13 19:53:15.061113
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x == 'a', [])) == []
    assert list(drop_until(lambda x: x == 'a', ['b', 'c', 'c', 'a', 'd'])) == ['a', 'd']
    assert list(drop_until(lambda x: x > 2, [1, 2, 3, 4, 5])) == [3, 4, 5]



# Generated at 2022-06-13 19:53:24.785476
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) \
           == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) \
           == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]



# Generated at 2022-06-13 19:53:29.434705
# Unit test for function drop
def test_drop():
    for n in range(4):
        for xs in ([], list(range(4)), [None] * 4):
            assert list(drop(n, xs)) == (xs[n:] if n <= len(xs) else [])



# Generated at 2022-06-13 19:54:02.022175
# Unit test for function scanl
def test_scanl():
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd'])) == ['a', 'ba', 'cba', 'dcba']


# Generated at 2022-06-13 19:54:04.226218
# Unit test for function chunk
def test_chunk():
    assert list(chunk(2, range(5))) == [[0, 1], [2, 3], [4]]



# Generated at 2022-06-13 19:54:12.269161
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    # Test basic function
    item = LazyList([1, 2, 3, 4, 5])[2]
    assert item == 3

    item = LazyList([1, 2, 3, 4, 5])[-1]
    assert item == 5

    # Test index out of bounds
    with pytest.raises(IndexError):
        LazyList([1, 2, 3])[3]

    # Test iterating through slice
    l = LazyList(range(1000))
    assert list(l[:100]) == list(range(100))

    # Test iterating through list with an iterator
    it = l.__iter__()
    for i in range(100):
        assert next(it) == i


# Generated at 2022-06-13 19:54:15.313900
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
test_chunk()


# Generated at 2022-06-13 19:54:24.526940
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(1, range(10))) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(chunk(0, range(10))) == []
    assert list(chunk(10, range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(chunk(100, range(10))) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]


# Generated at 2022-06-13 19:54:37.145533
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    _0_0 = LazyList(((i,) for i in range(5)))
    assert _0_0[0] == 0
    _0_1 = LazyList(((i,) for i in range(5)))
    assert _0_1[0:2] == [0, 1]
    _0_2 = LazyList(((i,) for i in range(5)))
    assert _0_2[0:1:2] == [0]
    _0_3 = LazyList(((i,) for i in range(5)))
    assert _0_3[-1] == 4
    _0_4 = LazyList(((i,) for i in range(5)))
    assert _0_4[:] == [0, 1, 2, 3, 4]

# Generated at 2022-06-13 19:54:40.567019
# Unit test for function chunk
def test_chunk():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]



# Generated at 2022-06-13 19:54:48.252884
# Unit test for function drop
def test_drop():
    """

    :return:
    """
    assert list(drop(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == [6, 7, 8, 9, 0]
    assert list(drop(5, [1, 2, 3, 4, 5])) == []
    assert list(drop(0, [1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]



# Generated at 2022-06-13 19:54:53.566553
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    map_list = MapList(lambda i: i * i, list(range(10)))
    print(map_list[0], map_list[2], map_list[4])
    assert map_list[:2] == [0, 1]
    # print(map_list.__getitem__(slice(2)))
    return



# Generated at 2022-06-13 19:55:00.031731
# Unit test for function chunk
def test_chunk():
    test_chunk_passed = \
      (list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]])

    test_chunk_failed = \
      not test_chunk_passed

    print("Test chunk - Passed" if test_chunk_passed else "Test chunk - Failed")
    return not test_chunk_failed


# Generated at 2022-06-13 19:55:11.303712
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
  len = None
  for i in range(20):
    if random.random() < 0.5:
      len = i
    mpl = MapList(lambda x: 2 * x, list(range(len)))
    mpl.__getitem__(slice.__getitem__(slice(None, None, 2), 0))
    mpl.__getitem__(slice.__getitem__(slice(None, None, 2), 1))
    mpl.__getitem__(slice.__getitem__(slice(None, None, -1), 1))
    for j in range(len):
      if random.random() < 0.5:
        mpl.__getitem__(j)
        if j >= 1:
          mpl.__getitem__(slice.__getitem__(slice(None, j), 1))


# Generated at 2022-06-13 19:55:17.885947
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    class TestRange:
        def __init__(self, *args):
            pass
        def __len__(self):
            pass
        def __iter__(self):
            pass
        def __getitem__(self, item):
            pass

    # Overload 1 raises
    with raises(NotImplementedError):
        TestRange[int](1).__getitem__(1)
    # Overload 2 raises
    with raises(NotImplementedError):
        TestRange[slice](1).__getitem__(slice(1, 2))



# Generated at 2022-06-13 19:55:21.689137
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 10, range(10))) == []
    assert list(drop_until(lambda x: x == 10, [])) == []



# Generated at 2022-06-13 19:55:34.230519
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    lazy_list = LazyList(range(100))
    assert lazy_list[-1] == 99
    assert lazy_list[99] == 99
    assert lazy_list[:10] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert lazy_list[10:15] == [10, 11, 12, 13, 14]
    assert lazy_list[10:45] == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
    assert lazy_list[:2] == [0, 1]
    assert lazy_list[2:]

# Generated at 2022-06-13 19:55:42.389322
# Unit test for function drop_until
def test_drop_until():
    import pytest
    from itertools import count, chain
    from math import sqrt

    # Test pass
    assert "".join(drop_until(lambda x: x > 5, range(10))) == "6789"
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert "".join(drop_until(lambda x: x > 5, chain(range(3), range(10, 15)))) == "6789"
    assert list(drop_until(lambda x: x > 5, chain(range(3), range(10, 15)))) == [6, 7, 8, 9]
    assert "".join(drop_until(lambda x: x > 10, range(10))) == ""

# Generated at 2022-06-13 19:55:49.854249
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    # variable 'test' should be iterable
    for i in range(10):
        for j in range(10):
            for k in range(10):
                try:
                    test = Range(i, j, k)
                    temp = test.__getitem__(random.randint(-10, 10))
                except IndexError:
                    pass
                except TypeError:
                    pass
                except ValueError:
                    pass


# Generated at 2022-06-13 19:55:55.477188
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    func = lambda x: x + 1
    lst = [1, 2, 3, 4, 5]
    ml = MapList(func, lst)
    assert ml[1] == func(lst[1]) # Evaluate MapList[T]
    assert ml[0:2:1] == [func(x) for x in lst[0:2:1]] # Evaluate MapList[slice]

# Generated at 2022-06-13 19:56:00.641353
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    val = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    assert val[:] == [1, 4, 9, 16, 25]
    assert val[2:4] == [9, 16]
    assert val[:2] == [1, 4]
    assert val[-1] == 25

# Generated at 2022-06-13 19:56:15.904254
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    import random
    import sys
    import time

    seq = random.choices(range(100), k=10 ** 5)

    lst_lazy = LazyList(seq)

    assert lst_lazy[-20] == seq[-20]

    # test __getitem__ with a slice of type `slice`
    lst_lazy = LazyList(seq)
    assert lst_lazy[:] == seq

    # test __getitem__ with a slice of type `slice`
    lst_lazy = LazyList(seq)
    assert lst_lazy[20:40] == seq[20:40]

    # test __getitem__ with a slice of type `slice`
    lst_lazy = LazyList(seq)
    assert lst_lazy[20:40:2]

# Generated at 2022-06-13 19:56:18.671463
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]

# Generated at 2022-06-13 19:56:32.879142
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [1, 3, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [1, 3, 5])) == []
    assert list(drop_until(lambda x: x > 5, [])) == []
test_drop_until()



# Generated at 2022-06-13 19:56:44.950290
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    data = list(range(20))
    check_data = lambda a, idx: a[idx] == data[idx]
    check_list = lambda a, idx: data[idx.start: idx.stop: idx.step] == a[idx]

    def test_normal_getitem(data):
        a = LazyList(data)
        idx = random.randint(0, len(data) - 1)
        assert check_data(a, idx)
        idx = random.randint(0, len(data) - 1)
        assert check_data(a, idx)
        idx = random.randint(0, len(data) - 1)
        assert check_data(a, idx)

    def test_slice_getitem(data):
        a = L

# Generated at 2022-06-13 19:56:53.078468
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # MapList.__getitem__(0) # Constructor call(s)
    # MapList.__getitem__(0) # Type assertion
    # MapList.__getitem__(1) # Type assertion
    # MapList.__getitem__(2) # Type assertion
    # MapList.__getitem__(3) # Type assertion
    # List.__getitem__(2) # Function call
    # List.__getitem__(3) # Function call
    result = MapList(lambda x: x * x, [1, 2, 3, 4])[2] # Function call
    # MapList.__getitem__(0) # Constructor call(s)
    # MapList.__getitem__(0) # Type assertion
    # MapList.__getitem__(1) # Type assertion
    # MapList

# Generated at 2022-06-13 19:56:57.513597
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = MapList(lambda x: x * x, [1, 2, 3, 4])
    assert (a[0], a[2]) == (1, 9)
    assert a[::-1] == [16, 9, 4, 1]



# Generated at 2022-06-13 19:57:03.709465
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
test_split_by()



# Generated at 2022-06-13 19:57:07.244666
# Unit test for function drop_until
def test_drop_until():
    l=[1,2,3,4,5,6,5,5,5,5]
    result=drop_until(lambda x: x>5,l)
    print(type(result))
    print(list(result))

test_drop_until()


# Generated at 2022-06-13 19:57:16.310343
# Unit test for function drop_until
def test_drop_until():
    test_cases = [
        ([1], lambda x: x > 0, []),
        ([], lambda x: x > 0, []),
        ([1, 2, 3], lambda x: x > 0, [1, 2, 3]),
        ([-1, 2, 3], lambda x: x > 0, [2, 3]),
        ([-1, -2, 3], lambda x: x > 0, [3]),
        ([-1, -2, -3], lambda x: x > 0, []),
    ]
    for data, pred, ans in test_cases:
        res = list(drop_until(pred, data))
        assert res == ans



# Generated at 2022-06-13 19:57:28.144378
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import os
    import sys

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    import unittest

    class Test(unittest.TestCase):
        def test(self):
            out = StringIO()
            sys.stdout = out

# Generated at 2022-06-13 19:57:38.022746
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    print()


# Generated at 2022-06-13 19:57:44.875086
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r1 = Range(1, 10 + 1)
    print(r1[2], r1[4], r1[-1])
    print(r1[0:4])
    print(r1[4:])
    print(r1[:4])
    print(r1[:])

# Generated at 2022-06-13 19:58:04.864216
# Unit test for function drop_until
def test_drop_until():
    x = [1, 2, 3, 4, 5, 6, 7]
    x_expect = [1, 2, 3, 4, 5, 6, 7]
    res_itr = drop_until(lambda i: i > 3, x)
    res_list = [i for i in res_itr]
    assert all(x == y for x, y in zip(x_expect, res_list))

    x = [1, 2, 3, 4, 5, 6, 7]
    x_expect = [4, 5, 6, 7]
    res_itr = drop_until(lambda i: i > 3, x)
    res_list = [i for i in res_itr]
    assert all(x == y for x, y in zip(x_expect, res_list))


# Generated at 2022-06-13 19:58:16.136337
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(11)
    assert r[0] == 0
    assert r[10] == 10
    assert r[2] == 2
    assert r[-1] == 10
    assert r[-11] == 0
    try:
        r[11]
        assert False
    except IndexError:
        pass
    try:
        r[-12]
        assert False
    except IndexError:
        pass
    assert r[1:3] == [1, 2]
    assert r[-10:-3] == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert r[:4:2] == [0, 2]
    assert r[3:] == [3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-13 19:58:22.716748
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    func1 = lambda x: x + 1
    a = [1, 2, 3, 4, 5]
    lst1 = MapList(func1, a)
    assert lst1[3] == 5
    assert lst1[:3] == [2, 3, 4]
    assert lst1[1:4] == [3, 4, 5]
    assert lst1[::2] == [2, 4, 6]


test_MapList___getitem__()

# Generated at 2022-06-13 19:58:29.195469
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():

    assert(MapList(lambda x: x, (1, 2, 3))[1] == 2)
    assert(MapList(lambda x: x, (1, 2, 3))[-1] == 3)
    assert(MapList(lambda x: x + 1, (1, 2, 3))[1:][0] == 3)
    assert(MapList(lambda x: x + 1, (1, 2, 3))[:2][0] == 2)
    assert(MapList(lambda x: x + 1, (1, 2, 3))[::2][0] == 2)


# Generated at 2022-06-13 19:58:39.187604
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 7, range(10))) == [8, 9]
    assert list(drop_until(lambda _: False, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: True, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: False, range(0))) == []
    assert list(drop_until(lambda x: True, range(0))) == []



# Generated at 2022-06-13 19:58:44.326510
# Unit test for function drop_until
def test_drop_until():
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    func_with_predicate = lambda x: x > 5
    assert list(drop_until(func_with_predicate, lis)) == [6, 7, 8, 9, 10]

test_drop_until()



# Generated at 2022-06-13 19:58:51.375115
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    a = LazyList([])
    assert_equal(a[0:], [])
    a = LazyList(range(5))
    assert_equal(a[2:], [2,3,4])
    assert_equal(a[0:3], [0,1,2])
    assert_equal(a[2:2], [])
    assert_equal(a[2:4], [2,3])
    assert_equal(a[4:4], [])
    assert_equal(a[4:5], [4])
    assert_equal(a[4:6], [4])
    assert_equal(a[4:7], [4])
    assert_equal(a[4:-1], [4])
    assert_equal(a[4:-2], [4])

# Generated at 2022-06-13 19:58:59.844186
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    import pytest
    o = Range(1, 11) # (start, end)
    assert o[0] == 1
    assert o[2] == 3
    assert o[-1] == 10
    assert o[::2] == [1, 3, 5, 7, 9]
    assert o[1::2] == [2, 4, 6, 8, 10]
    assert o[::-1] == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert o[3:6] == [4, 5, 6]
    assert o[-3:-1] == [8, 9]
    assert o[10:1:-1] == [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Generated at 2022-06-13 19:59:03.570240
# Unit test for function drop_until
def test_drop_until():
    l = list(drop_until(lambda x: x > 5, range(10)))
    if len(l) != 4:
        assert False
    for i in range(6, 10):
        if l[i - 6] != i:
            assert False
    assert True



# Generated at 2022-06-13 19:59:09.475638
# Unit test for method __getitem__ of class LazyList
def test_LazyList___getitem__():
    print("Testing __getitem__ of class LazyList")
    lst = LazyList(range(10))
    assert 0 == lst[0]
    assert 10 == len(lst)
    assert 7 == lst[7]
    assert 10 == len(lst)
    assert [5, 6, 7] == lst[5:8]
    assert 10 == len(lst)
    assert [5, 6, 7, 8, 9] == lst[5:]
    assert 10 == len(lst)
    return True

# Generated at 2022-06-13 19:59:29.551515
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    assert (list(MapList(lambda x: x[0], [('a', 1), ('b', 2), ('c', 3)])) == ['a', 'b', 'c'])
    assert (MapList(lambda x: x[-1], [('a', 1), ('b', 2), ('c', 3)]).list == [('a', 1), ('b', 2), ('c', 3)])
    assert (MapList(lambda x: x[0], [('a', 1), ('b', 2), ('c', 3)])[0] == 'a')
    assert (MapList(lambda x: x[0], [('a', 1), ('b', 2), ('c', 3)])[2] == 'c')

# Generated at 2022-06-13 19:59:40.155181
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x, range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(drop_until(lambda x: x, map(lambda x: x == 5, range(10)))) == [True, False, False, False, False, False, False, False, False, False]
    assert list(drop_until(lambda x: x, [False, False, False, False, True, False, False])) == [True, False, False]
    assert list(drop_until(lambda x: x, iter([False, False, False, False, True, False, False]))) == [True, False, False]
    assert list

# Generated at 2022-06-13 19:59:51.309186
# Unit test for function split_by
def test_split_by():
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by(" Split by: ", empty_segments=True, separator='.')) == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    try:
        list(split_by(range(10)))
        assert False, "Invalid split_by call must throw exception"
    except ValueError:
        pass
    try:
        list(split_by(range(10), criterion=lambda x: x % 3 == 0, separator=1))
        assert False, "Invalid split_by call must throw exception"
    except ValueError:
        pass



# Generated at 2022-06-13 19:59:59.123728
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    def func(x):
        if x == 1:
            raise ValueError
        return x * 2

    mpl = MapList(func, [1, 2, 3])
    assert mpl[0] == 2
    assert mpl[1] == 4
    assert mpl[2] == 6
    assert mpl[-1] == 6
    assert mpl[-2] == 4
    assert mpl[-3] == 2

    assert mpl[0:1] == [2]
    assert mpl[0:2] == [2, 4]
    assert mpl[-2:] == [4, 6]



# Generated at 2022-06-13 20:00:01.206364
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r0 = Range(-1)
    assert r0[0] == 0



# Generated at 2022-06-13 20:00:11.110547
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert r[-1] == 9
    assert r[-10] == 0
    assert tuple(r) == tuple(range(10))

    r = Range(1, 10 + 1)
    assert r[-1] == 10
    assert r[-9] == 2
    assert tuple(r) == tuple(range(1, 10 + 1))

    r = Range(1, 11, 2)
    assert r[-1] == 9
    assert r[-4] == 3
    assert tuple(r) == tuple(range(1, 11, 2))

    assert tuple(Range(0, 1)[:]) == (0,)
    assert tuple(Range(0, 10)[::2]) == tuple(range(0, 10, 2))

# Generated at 2022-06-13 20:00:14.990462
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
test_drop_until()



# Generated at 2022-06-13 20:00:23.488559
# Unit test for function drop_until
def test_drop_until():
    result = drop_until(lambda x: x > 5, [1,2,3,4,5,6,7,8,9])
    result = list(result)
    assert result == [6, 7, 8, 9]
    result = drop_until(lambda x: x > 5, [1,2,3,4,5,6])
    result = list(result)
    assert result == [6]
    result = drop_until(lambda x: x > 5, [1,2,3,4,5])
    result = list(result)
    assert result == []
    result = drop_until(lambda x: x > 5, [])
    result = list(result)
    assert result == []



# Generated at 2022-06-13 20:00:27.071050
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    def f(i):
        return a[i]*b[i]
    pos = bisect.bisect_left(MapList(f, Range(len(a))), 10)
    assert pos == 2


# Generated at 2022-06-13 20:00:28.361397
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    assert Range(10)[5] == 5


# Generated at 2022-06-13 20:01:07.091219
# Unit test for function drop_until
def test_drop_until():
    import io
    from contextlib import redirect_stdout

    # Test without printing
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))

    # Test with printing
    buf = io.StringIO()
    with redirect_stdout(buf):
        # buf will write the printed items
        list(drop_until(lambda x: print(x) or x > 5, range(10)))
        list(drop_until(lambda x: print(x) or x > 5, range(10)))  # repeat for detecting memory leak

# Generated at 2022-06-13 20:01:11.827113
# Unit test for function drop_until
def test_drop_until():
    assert tuple(drop_until(lambda x: x > 5, range(10))) == (6, 7, 8, 9)
    assert tuple(drop_until(lambda x: x > 5, range(5))) == tuple()
    assert tuple(drop_until(lambda x: x > 5, range(5, 10))) == tuple(range(5, 10))



# Generated at 2022-06-13 20:01:21.201012
# Unit test for function drop_until
def test_drop_until():
    # Case 1: drop all
    assert list(drop_until(lambda x: x > 5, range(10))) == list(range(6, 10))
    # Case 2: drop none
    assert list(drop_until(lambda x: x < 10, range(10))) == list(range(10))
    # Case 3: drop some
    assert list(drop_until(lambda x: x%2==1, range(10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Case 4: empty iterable
    assert list(drop_until(lambda x: x < 5, range(0))) == []



# Generated at 2022-06-13 20:01:23.903421
# Unit test for function drop_until
def test_drop_until():
    it = drop_until(lambda x: x < 7, range(10))
    assert next(it) == 7
    assert list(it) == [8, 9]



# Generated at 2022-06-13 20:01:26.852822
# Unit test for method __getitem__ of class Range
def test_Range___getitem__():
    r = Range(10)
    assert (r[0] == 0)
    return 'unit_test passed'
print(test_Range___getitem__())


# Generated at 2022-06-13 20:01:39.215043
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    import pytest
    from . import randseq

    tests = [
        (1, 10),
        (10, 10),
        (100, 10),
        (1000, 10),
    ]
    for iters, length in tests:
        for _ in range(iters):
            func = lambda x: x * 2
            lst = randseq(length)
            wrapper = MapList(func, lst)
            for i in range(length):
                assert wrapper[i] == func(lst[i])
            for i in range(length):
                assert wrapper[i : length - i] == list(map(func, lst[i : length - i]))
            assert list(wrapper) == list(map(func, lst))
            wrapper = MapList(lambda x: x, lst)

# Generated at 2022-06-13 20:01:44.546389
# Unit test for function drop_until
def test_drop_until():
    assert drop_until(lambda x: x == 'world', ['hello', 'world']) == ['world']
    assert drop_until(lambda x: x == 'world', ['hello']) == []
    assert drop_until(lambda x: x < 5, [1, 7, 32, 4, 2, 18, 5]) == [7, 32, 4, 2, 18, 5]



# Generated at 2022-06-13 20:01:53.339357
# Unit test for method __getitem__ of class MapList
def test_MapList___getitem__():
    # test __getitem__ of class MapList
    lst = [1, 2, 3, 4]
    map_list_obj = MapList(lambda x: x * x, lst)
    assert map_list_obj.__getitem__(-1) == 16
    assert map_list_obj.__getitem__(2) == 9
    map_list_obj = MapList(lambda x: x * x, lst)
    assert map_list_obj.__getitem__(slice(0, None, 1)) == [1, 4, 9, 16]
    map_list_obj = MapList(lambda x: x * x, lst)
    assert map_list_obj.__getitem__(slice(None, None, None)) == [1, 4, 9, 16]
    pass


# Generated at 2022-06-13 20:01:57.319397
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]



# Generated at 2022-06-13 20:02:01.202284
# Unit test for function drop_until
def test_drop_until():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x > 5, [])) == []

